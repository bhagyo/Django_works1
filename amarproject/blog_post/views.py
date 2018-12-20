from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    all_post = Post.objects.all()
    return render(request, 'post_list.html', {'all_post_list': all_post})
