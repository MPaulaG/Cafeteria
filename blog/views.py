from django.shortcuts import render, get_object_or_404
from.models import Blog,Category

# Create your views here.
def blog(request):
    blogs= Blog.objects.all()
    return render(request,"blog/blog.html",{'blogs':blogs} )

#vista para ver las entradas por cada categoria 
def category(request,categoryId ):
    #cargar categorias
    category= get_object_or_404(Category, id=categoryId)
    #cargar las entradas enlazadas a esa categoria es decir filtrar
    #blogs= Blog.objects.filter(categories=category)
    #return render(request,"blog/category.html", {'categ':category, 'blogs':blogs })
    return render(request,"blog/category.html", {'categ':category})