from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogPost
import datetime

def post_list(request):
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, 1) # how many blogs per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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