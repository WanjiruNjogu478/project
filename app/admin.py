from django.contrib import admin
from .models import Service, Testimonial, Beautician, Appointment, Contact, Gallery, Stats, FAQ, CarouselItem, BlogPost, Header, Footer, FeaturedService

admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Beautician)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Stats)
admin.site.register(FAQ)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
admin.site.register(CarouselItem, CarouselItemAdmin)
admin.site.register(BlogPost)
admin.site.register(Header)
admin.site.register(Footer)
@admin.register(FeaturedService)
class FeaturedServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')