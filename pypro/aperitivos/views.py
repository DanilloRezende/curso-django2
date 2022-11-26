from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', youtube_id='Lgh8JgcYFwM'),
    Video(slug='projetos-django', titulo='Video Projetos DJANGO', youtube_id='l9d4BcwQsbQ')
]

videos_dct = {v.slug: v for v in videos}
def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
def video(request, slug):
    video= get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
