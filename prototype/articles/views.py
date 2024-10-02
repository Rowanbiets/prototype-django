from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article

# Artikelen

def articles(request):
 myarticles = Article.objects.all().values()
 template = loader.get_template('all_articles.html')
 context = {
    'myarticles': myarticles,
}
 return HttpResponse(template.render(context,request))

def details(request, id):
 myarticle = Article.objects.get(id=id)
 template = loader.get_template('details.html')
 context = {
  'myarticle': myarticle
 }
 return HttpResponse(template.render(context,request))

def main(request):
 template = loader.get_template('main.html')
 return HttpResponse(template.render())



