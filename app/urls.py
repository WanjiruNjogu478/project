from django.urls import path
from . import views
from .views import delete_blog


urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog_index, name='blog_index'),  # Blog home page
    path('blog/create/', views.blog_create, name='blog_create'),  # Create blog post
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),  # Blog post detail
    path('blog/delete/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
    
]