from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

class Beautician(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=120)
    image = models.ImageField(upload_to='beauticians/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.client_name} on {self.appointment_date}"

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

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')  
    title = models.CharField(max_length=200)                
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title   
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

