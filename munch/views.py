from django.shortcuts import render, redirect
from .models import Video

def home_view(request):
    db_videos = Video.objects.all().order_by('-created_at')
    
    # फ़ोटो वाले 4 रियल यूज़र्स का स्टेटिक बैकअप डेटा (अगर डेटाबेस खाली हो)
    demo_creators = [
        {"author": "अमित कुमार", "title": "🔥 न्यू ब्लॉग: मिर्ज़ापुर का शानदार सफर!", "time": "2 घंटे पहले", "pfp": "अक"},
        {"author": "विकास यादव", "title": "💡 डिजिटल मार्केटिंग सीखें और पैसे कमाएं (फुल कोर्स)", "time": "5 घंटे पहले", "pfp": "व्य"},
        {"author": "राहुल सिंह", "title": "🎬 विद्यासागर मंच पर पहला टेक वीडियो — जरूर देखें", "time": "1 दिन पहले", "pfp": "रस"},
        {"author": "सतीश कुमार", "title": "🌾 खेती-बारी और नए बिजनेस आइडियाज 2026", "time": "3 दिन पहले", "pfp": "सक"},
    ]
    
    return render(request, 'home.html', {'db_videos': db_videos, 'demo_creators': demo_creators})

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        author = request.POST.get('author_name', 'अविनाश सर')
        video_file = request.FILES.get('video_file')
        
        Video.objects.create(author_name=author, title=title, description=description, video_file=video_file)
    return redirect('/')
