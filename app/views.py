from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Testimonial, Beautician, Gallery, Stats, FAQ, CarouselItem, BlogPost, Header, Footer, FeaturedService
from .forms import BlogPostForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import requests
import base64
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html') 

def home(request):
    # Fetch necessary data for homepage
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    beauticians = Beautician.objects.all()
    gallery = Gallery.objects.all()
    stats = Stats.objects.all()
    faqs = FAQ.objects.all()
    blog_posts = BlogPost.objects.all()
    carousel_items = CarouselItem.objects.all()  
    header_object = Header.objects.first()
    footer_object = Footer.objects.first()

    return render(request, 'index.html', {
        'services': services,
        'testimonials': testimonials,
        'beauticians': beauticians,
        'gallery': gallery,
        'stats': stats,
        'faqs': faqs,
        'blog_posts': blog_posts,
        'carousel_items': carousel_items,
        'header_object': header_object,
        'footer_object': footer_object
    })

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
    
    return render(request, 'delete_confirm.html', {'blog_post': blog_post})

def submit_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        testimonial_content = request.POST.get('testimonial')
        rating = request.POST.get('rating')

        # Validate inputs
        if name and testimonial_content and rating:
            testimonial = Testimonial(name=name, content=testimonial_content, rating=rating)

            try:
                testimonial.save()  # Attempt to save the testimonial
                return redirect('home')  # Redirect to home after saving
            except Exception as e:
                print(f"Error saving testimonial: {e}")

    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def initiate_payment(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        message = request.POST.get('message')

        # Payment amount
        amount = 200  # Ksh 200

        # Get access token
        access_token = get_access_token()

        # Initiate STK Push
        response = initiate_stk_push(access_token, phone_number, amount)

        # Check response and process accordingly
        if response['ResponseCode'] == '0':
            # Redirect user to M-Pesa payment
            return JsonResponse({'status': 'success', 'message': 'Payment initiated. Please complete on M-Pesa.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Payment initiation failed. Please try again.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

def get_access_token():
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(api_url, auth=(settings.M_PESA_CONSUMER_KEY, settings.M_PESA_CONSUMER_SECRET))
    return response.json()['access_token']

def initiate_stk_push(access_token, phone_number, amount):
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {'Authorization': f'Bearer {access_token}'}
    payload = {
        "BusinessShortCode": settings.M_PESA_SHORTCODE,
        "Password": base64.b64encode(f"{settings.M_PESA_SHORTCODE}{settings.M_PESA_PASSKEY}{timezone.now().strftime('%Y%m%d%H%M%S')}").encode('utf-8'),
        "Timestamp": timezone.now().strftime('%Y%m%d%H%M%S'),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.M_PESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.M_PESA_CALLBACK_URL,
        "AccountReference": "AppointmentPayment",
        "TransactionDesc": "Payment for Appointment"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        data = request.body  # Get the incoming data from M-Pesa
        # Process the payment response
        # Perform validation and update appointment status accordingly
        # Extract details from the data and confirm the transaction

        # Example: Log or process the payment confirmation
        print(data)  # For debugging purposes, log the incoming data

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

def featured_services(request):
    featured_services_list = FeaturedService.objects.all()  # Fetch all featured services from the database
    return render(request, 'index.html', {'featured_services': featured_services_list})

