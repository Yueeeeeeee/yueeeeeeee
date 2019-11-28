from django.urls import path
from image import views

app_name = 'image'
urlpatterns = [
    path(
        'image_upload',
        views.image_upload,
        name = 'image_upload'
    )
]