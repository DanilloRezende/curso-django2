from django.shortcuts import render


videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'Lgh8JgcYFwM'},
    {'slug': 'projetos-django', 'titulo': 'Video Projetos DJANGO', 'youtube_id': 'l9d4BcwQsbQ'}
]

videos_dct = {dct['slug']: dct for dct in videos}
def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
def video(request, slug):
    video= videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
