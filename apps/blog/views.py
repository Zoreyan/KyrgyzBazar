from django.shortcuts import render
from .models import *


def post_list_view(request):
    posts = Post.objects.all()
    
    search_input = request.GET.get('pq') or ''
    if search_input:
        posts = Post.objects.filter(title__icontains=search_input)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)