from django.shortcuts import render
from blog.models import BlogPost
import datetime

def post_list(request):
    posts = BlogPost.objects.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, slug):
    post = BlogPost.objects.filter(
        #publish__date__gt=datetime.date(year, month, day),
        #publish__year=year,
        #publish__month=month,
        #publish__day=day,
        publish=datetime.date(year, month, day),
        slug=slug
    ).first()
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )