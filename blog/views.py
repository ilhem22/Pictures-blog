from django.shortcuts import render
from .models import Article

def home(request):
   list_articles=Article.objects.all()
   context = {"liste_articles":list_articles}
   return render(request,"index.html",context)

def detail(request,id_article):

   article=Article.objects.get(id=id_article)
   category=article.category
   articles_en_relation=Article.objects.filter(category=category)

   return render(request,'detail.html',{"article":article,"aer":articles_en_relation})   

def test (request):
   return render(request,'test.html')

def search(request):
   query=request.GET["article"]
   liste_article=Article.objects.filter(title__contains=query)
   return render(request,"search.html",{"liste_article":liste_article})

