from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post


# Create your views here.


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    #  the right way to call the template is through render which run http response on the background and return the path specified
     context = {
         'posts' : Post.objects.all()
     }
     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return HttpResponse('<h3>This is contact us Page<h3>')
    
