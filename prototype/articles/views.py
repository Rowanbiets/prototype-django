from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment
from .forms import CommentForm
from django.db.models import Q

# Artikelen overzicht
def articles(request):
    myarticles = Article.objects.all().values()
    template = loader.get_template('all_articles.html')
    context = {
        'myarticles': myarticles,
    }
    return HttpResponse(template.render(context, request))

# Artikel details
def details(request, id):
    myarticle = Article.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myarticle': myarticle
    }
    return HttpResponse(template.render(context, request))

# Hoofd pagina
def main(request):
    return render(request, 'main.html') 

# Inloggen
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles')  # Redirect naar artikelenpagina na login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Uitloggen
def logout_view(request):
    logout(request)
    return redirect('main')  # Redirect naar loginpagina na logout


# Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect naar de login pagina na registratie
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Artikelen toevoegen
@login_required
def article_add(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  
            article.author = request.user 
            article.save()  
            return redirect('articles') 
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})

# Artikelen bewerken
@login_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)

    # Controleer of de ingelogde gebruiker de auteur is
    if article.author != request.user:
     return HttpResponse("You are not allowed to edit this article.", status=403)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()  # Auteur blijft hetzelfde; dit slaat de bewerking op
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article_form.html', {'form': form})
    
# Artikelen verwijderen
@login_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)

    # Controleer of de ingelogde gebruiker de auteur is
    if article.author != request.user:
        return HttpResponse("You are not allowed to delete this article.", status=403)

    if request.method == "POST":
        article.delete()
        return redirect('articles')

    return render(request, 'article_confirm_delete.html', {'article': article})

# Artikelen liken

def like_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.likes +=1
    article.save()
    return redirect('articles') 

# Comments
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('details', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'articles/details.html', {'article': article, 'comments': comments, 'form': form})

# Zoekfunctie

def search_articles(request):
    query = request.GET.get('q')  # Haalt de zoekterm op uit de URL
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )  
    else:
        articles = Article.objects.all()  # Als er geen zoekterm is, toon alle artikelen
    return render(request, 'search_results.html', {'articles': articles, 'query': query})