from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    all_post = Post.objects.all()
    return render(request, 'post_list.html', {'all_post_list': all_post})


def post_list(request):
    all_list = Post.objects.all()
    return render(request, 'all_post.html', {'all_list': all_list})


def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    return render(request, 'single-post.html', {'post': post})
