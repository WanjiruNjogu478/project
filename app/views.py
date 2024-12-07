# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Testimonial, Beautician, Gallery, Stats, FAQ, Slider, BlogPost
from .forms import BlogPostForm
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    beauticians = Beautician.objects.all()
    gallery = Gallery.objects.all()
    stats = Stats.objects.all()
    faq = FAQ.objects.all()
    slider = Slider.objects.all()
    blog_posts = BlogPost.objects.all()
    
    return render(request, 'index.html', {
        'services': services,
        'testimonials': testimonials,       
        'beauticians': beauticians,
        'gallery': gallery,
        'stats': stats,
        'faq': faq,
        'slider': slider,
        'blog_posts': blog_posts,
    })

def home(request):
    # Fetch necessary data for homepage
    blog_posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'index.html', {'blog_posts': blog_posts})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the blog post
            return redirect('blog_index')  # Redirect to the blog index after creation
    else:
        form = BlogPostForm()  # Display an empty form

    return render(request, 'create_blog_post.html', {'form': form})

def blog_index(request):
    posts = BlogPost.objects.all()  # Get all blog posts
    return render(request, 'blog_index.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # Get a specific post
    return render(request, 'blog_detail.html', {'post': post})

def delete_blog(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    
    if request.method == 'POST':
        blog_post.delete()
        messages.success(request, 'Blog post deleted successfully.')
        return redirect('blog_index')  # Redirect to the blog index or another page
    
    return render(request, 'blog/delete_confirm.html', {'blog_post': blog_post})

from django.shortcuts import render, redirect
from .models import Testimonial

def submit_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        testimonial = request.POST.get('testimonial')
        rating = request.POST.get('rating')

        # Create a new Testimonial instance
        new_testimonial = Testimonial(name=name, testimonial=testimonial, rating=rating)
        new_testimonial.save()  # Save the instance to the database

        return redirect('home')  # Redirect to a success page or home
    return HttpResponse(status=405)  # Return 405 for non-POST requests
