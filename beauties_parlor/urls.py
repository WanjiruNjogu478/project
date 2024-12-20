"""
URL configuration for beauties_parlor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from app import views
from app.views import index, featured_services

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home, name="home"),
path('', index, name='home'),
path('index.html', index, name='index'),
path('', include('app.urls')),
path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
path('register/', views.register, name='register'), # Custom registration view
path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
path('callback/', views.payment_callback, name='payment_callback'),
path('featured-services/', featured_services, name='featured_services'),
path('testimonials/', views.testimonials_view, name='testimonials'),
path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)