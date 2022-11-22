from django.shortcuts import render

def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'Lgh8JgcYFwM'},
        'projetos-django': {'titulo': 'Video Projetos DJANGO', 'youtube_id': 'l9d4BcwQsbQ'}
    }
    video= videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
