from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Beautician(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=120)
    image = models.ImageField(upload_to='beauticians/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=15)
    appointment_date = models.DateTimeField()
    service = models.CharField(max_length=100)  # Service type
    beautician = models.CharField(max_length=100)  # Beautician's name
    message = models.TextField(blank=True, null=True)  # Optional message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"{self.name} - {self.service} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or "Gallery Image"

class Stats(models.Model):
    beauticians = models.IntegerField(default=0)
    services = models.IntegerField(default=0)      
    awards = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)
    contacts = models.IntegerField(default=0)
    testimonials = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Stats: {self.beauticians} beauticians, {self.services} services"     

class FAQ(models.Model):
    question = models.TextField()  
    answer = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
    
class Header(models.Model):
    logo = models.ImageField(upload_to='logos/')
    phone_number = models.CharField(max_length=15)
    hours = models.CharField(max_length=50)
    services = models.JSONField()

class Footer(models.Model):
    logo_text = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    social_links = models.JSONField()  # Store social links as JSON
    useful_links = models.JSONField()   # Store useful links as JSON
    services = models.JSONField()        # Store services as JSON

    def __str__(self):
        return self.logo_text

class FeaturedService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # Font Awesome icon class name

    def __str__(self):
        return self.title