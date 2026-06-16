from django.db import models

class Video(models.Model):
    author_name = models.CharField(max_length=100, default="विद्यासागर क्रिएटर")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
