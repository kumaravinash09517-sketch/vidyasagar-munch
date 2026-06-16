from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video

@login_required
def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video_file')
        
        if video_file:
            # सीधे मॉडल में डेटा सेव करना ताकि क्लाउडिनरी बैकएंड में हैंडल करे
            video = Video(title=title, video_file=video_file, author=request.user)
            video.save()
            return redirect('home')
            
    return render(request, 'munch/upload.html')
