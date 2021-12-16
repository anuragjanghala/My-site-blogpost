from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.http import HttpResponse
# from datetime import date

# all_posts = [
        
# ]

# def get_date(post):
#     return post['date']

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })

def single_post(request, slug):
    indentified_post = get_object_or_404(Post, slug=slug)
    # indentified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': indentified_post,
        'post_tags': indentified_post.tags.all(),
    })