from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('', views.index, name="index"),
                  path('kategoriler', views.kategoriler, name="kategoriler"),
                  path('kategoriler/<slug:slug>', views.kategoriler_detay, name="kategoriler_detay"),
                  path('blog_detail/<slug:slug>', views.blog_detail, name="blog_detail")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
