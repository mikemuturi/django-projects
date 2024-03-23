from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts = [
    {
        'author': 'coreyMs',
        'title': "Blog Post1",
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Mike',
        'title': "Blog Post2",
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'

    }
]

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    #  the right way to call the template is through render which run http response on the background and return the path specified
     context = {
         'posts' : posts
     }
     return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return HttpResponse('<h3>This is contact us Page<h3>')
    
