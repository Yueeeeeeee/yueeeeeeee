from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from image.forms import ImageForm
from image.models import Image

# Create your views here.
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 9)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'image/image_list.html', {'images': images})

@login_required
def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return render(request, 'image/image_upload_done.html')
    else:
        form = ImageForm()
        return render(request, 'image/image_upload.html', {'form': form})

@login_required
def image_detail(request, id, slug):
    image = Image.objects.filter(id=id, slug=slug).first()
    return render(request, 'image/image_detail.html', {'image':image})

@login_required
def image_like(request, id):
    image = Image.objects.get(id=id)
    image.user_liked.add(request.user)
    return redirect('image:image_detail', id=id, slug=image.slug)

@login_required
def image_unlike(request, id):
    image = Image.objects.get(id=id)
    image.user_liked.remove(request.user)
    return redirect('image:image_detail', id=id, slug=image.slug)