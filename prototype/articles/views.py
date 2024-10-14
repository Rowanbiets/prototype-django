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
from .models import UserActivity
from django.db.models import Count, Avg
from articles.models import Article, Comment,UserActivity



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
            
            # Log activiteit van de gebruiker 
            UserActivity.objects.create(
                user=request.user,
                activity_type='created_article',
                description=f'{request.user.username} created a new article: {article.title}' 
            )
            
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
    
    # Log activiteit van de gebruiker
    UserActivity.objects.create(
        user = request.user,
        activity_type = 'liked article',
        description = f'{request.user.username} liked the article: {article.title}'
    )
    
    return redirect('articles') 


# tijdlijn

def user_activity_timeline(request):
    activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'timeline.html', {'activities': activities})


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

# Statistieken

@login_required
def user_statistics(request):
    # Verkrijg artikelen van de ingelogde gebruiker
    articles = Article.objects.filter(author=request.user)

    # Aantal artikelen
    total_articles = articles.count()

    # Totaal aantal likes
    total_likes_received = sum(article.likes for article in articles)

    # Gemiddeld aantal likes per artikel
    average_likes_per_article = total_likes_received / total_articles if total_articles > 0 else 0

    # Meest gelikete artikel
    most_liked_article = articles.order_by('-likes').first()

    # Maak de context aan voor de template
    context = {
        'total_articles': total_articles,
        'total_likes_received': total_likes_received,
        'average_likes_per_article': average_likes_per_article,
        'most_liked_article': most_liked_article,
    }

    return render(request, 'statistics.html', context)