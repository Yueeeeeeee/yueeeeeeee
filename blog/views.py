from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogPost
from blog.forms import CommentForm
import datetime

def post_list(request):
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, 10) # how many blogs per page
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
        publish=datetime.date(year, month, day),
        slug=slug
    ).first()
    comments = post.blog_comments.filter(active=True) # retrieve active comments
    new_comment = None
    comment_form = CommentForm() # Create comment form for new comment
    if request.method == 'POST': # For request type 'POST', save comment if valid
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        #else:
            #comment_form = CommentForm()
    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        }
    )