from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPage, Categories, Tag

# Create your views here.
def home(request):
    strAgePython = request.GET.get('ageurl',15) # si non renseigné, la valeur est à 10
    lstBlogPages = BlogPage.objects.all()
    data = {'prenom' : 'Yohann',
            'montres' : ['Rolex', 'Omega', 'Seiko'],
            'age' : int(strAgePython),
            'lstBlogPages' : lstBlogPages
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))