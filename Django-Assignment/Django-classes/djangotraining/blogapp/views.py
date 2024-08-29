from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from blogapp.models import Comment, Post, Category, Tags
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
    # Retrieve all published blog posts
    blogposts = Post.objects.filter(published=True)
    
    # Retrieve all blog categories with post count
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    # Retrieve latest 3 blog posts for the sidebar
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    # Retrieve all tags
    blog_tags = Tags.objects.all()

    # Pagination handling
    paginator_instance = Paginator(blogposts, 1)  # 1 post per page
    page = request.GET.get('page')

    try:
        blogposts = paginator_instance.page(page)
    except PageNotAnInteger:
        blogposts = paginator_instance.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        blogposts = paginator_instance.page(paginator_instance.num_pages)  # If page is out of range, deliver last page.

    context = {
        'blogposts': blogposts,
        'blog_categories': blog_categories,
        'recent_blogs': recent_blogs,
        'blog_tags': blog_tags
    }

    return render(request, 'blog.html', context)

def blog_details(request, url):
    # Retrieve a specific blog post based on its URL
    post = get_object_or_404(Post, url=url)
    
    # Retrieve all blog categories with post count for sidebar
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    # Retrieve latest 3 blog posts for sidebar
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    # Retrieve all tags for sidebar
    blog_tags = Tags.objects.all()
    
    # Retrieve approved comments for the current post
    comments = post.comments.filter(approved=True)

    context = {
        'post': post,
        'blog_categories': blog_categories,
        'recent_blogs': recent_blogs,
        'blog_tags': blog_tags,
        'comments': comments
    }

    return render(request, 'single.html', context)

def postcomment(request):
    # Handle POST request to submit a comment
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        url = request.POST['url']

        # Retrieve the post object based on the provided URL
        post = get_object_or_404(Post, url=url)
        
        # Create a new comment associated with the retrieved post
        Comment.objects.create(post=post, name=name, email=email, message=message)
        
        # Return a JSON response indicating successful comment submission
        return JsonResponse({'message': 'Comment successfully saved!'})

def post_list_by_category(request, category_url):
    # Retrieve posts filtered by a specific category
    selected_blog_category = get_object_or_404(Category, url=category_url)
    blogposts = Post.objects.filter(published=True, category=selected_blog_category)
    
    # Retrieve all blog categories with post count for sidebar
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    # Retrieve latest 3 blog posts for sidebar
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    # Retrieve all tags for sidebar
    blog_tags = Tags.objects.all()

    context = {
        'blogposts': blogposts,
        'blog_categories': blog_categories,
        'recent_blogs': recent_blogs,
        'blog_tags': blog_tags
    }

    return render(request, 'blog.html', context)

def post_list_by_tags(request, tag_url):
    # Retrieve posts filtered by a specific tag
    selected_blog_tag = get_object_or_404(Tags, url=tag_url)
    blogposts = Post.objects.filter(published=True, tags=selected_blog_tag)
    
    # Retrieve all blog categories with post count for sidebar
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    # Retrieve latest 3 blog posts for sidebar
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    # Retrieve all tags for sidebar
    blog_tags = Tags.objects.all()

    context = {
        'blogposts': blogposts,
        'blog_categories': blog_categories,
        'recent_blogs': recent_blogs,
        'blog_tags': blog_tags
    }

    return render(request, 'blog.html', context)

def blog_search(request):
    # Handle blog post search based on query string
    query = request.GET.get('q')
    
    if query:
        blogposts = Post.objects.filter(title__icontains=query, published=True)
    else:
        blogposts = None

    # Retrieve all blog categories with post count for sidebar
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    # Retrieve latest 3 blog posts for sidebar
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    # Retrieve all tags for sidebar
    blog_tags = Tags.objects.all()

    context = {
        'blogposts': blogposts,
        'blog_categories': blog_categories,
        'recent_blogs': recent_blogs,
        'blog_tags': blog_tags
    }

    return render(request, 'blog.html', context)
