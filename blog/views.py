from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from blog.models import BlogPost
from blog.forms import CommentForm
import datetime


# List view of blogs
def post_list(request, tag_slug=None):
    # find all posts
    if tag_slug:  # request with tag slug
        tag = Tag.objects.filter(slug=tag_slug).first()
        post_list = BlogPost.objects.filter(tags__in=[tag])
    else:  # all posts
        post_list = BlogPost.objects.all()
    
    # retrive tags and divide blogs by pages
    tag_list = Tag.objects.all()
    paginator = Paginator(post_list, 6) # 6 blogs per page
    page = request.GET.get('page')
    
    # prevent page number overflow/underflow
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    # return redered post list
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts, 'tag_list': tag_list}
    )

# Single view of a blog
def post_detail(request, year, month, day, slug):
    # find post
    post = BlogPost.objects.filter(
        publish=datetime.date(year, month, day),
        slug=slug
    ).first()
    
    # retrieve active comments
    comments = post.blog_comments.filter(active=True)
    
    # Create comment form for new comments
    new_comment = None
    comment_form = CommentForm()  # Create comment form for new comment
    if request.method == 'POST':  # For request type 'POST', save comment if valid
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        #else:
            #comment_form = CommentForm()
    
    # return redered post
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