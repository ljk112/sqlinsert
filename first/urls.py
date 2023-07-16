from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('upload/', views.upload, name='upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
