from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from munch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
