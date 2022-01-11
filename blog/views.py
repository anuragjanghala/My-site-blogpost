from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
# from datetime import date

# all_posts = [
        
# ]

# def get_date(post):
#     return post['date']

# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     # sorted_posts = sorted(all_posts, key=get_date)
#     # latest_posts = sorted_posts[-3:]
#     return render(request, 'blog/index.html', {
#         'posts': latest_posts
#     })

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         'all_posts': all_posts,
#     })


class SinglePostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context
        


# def single_post(request, slug):
#     indentified_post = get_object_or_404(Post, slug=slug)
#     # indentified_post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, 'blog/post-detail.html', {
#         'post': indentified_post,
#         'post_tags': indentified_post.tags.all(),
#     })