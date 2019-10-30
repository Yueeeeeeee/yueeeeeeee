from django.shortcuts import render
from blog.models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )
