from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header = "GAUS Admin"
admin.site.site_title = "GAUS Admin Portal"
admin.site.index_title = "Welcome to GAUS Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]
