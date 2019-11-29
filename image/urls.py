from django.urls import path
from image import views

app_name = 'image'
urlpatterns = [
    path('image_upload/', views.image_upload, name='image_upload'),
    path('image_list/', views.image_list, name='image_list'),
    path('<int:id>/<slug:slug>/', views.image_detail, name='image_detail'),
    path('like/<int:id>/', views.image_like, name='image_like'),
    path('unlike/<int:id>/', views.image_unlike, name='image_unlike'),
]