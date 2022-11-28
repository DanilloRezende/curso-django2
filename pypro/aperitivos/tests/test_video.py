import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains

@pytest.fixture
def video(db):
    v = Video(slug='motivacao', titulo='Video Aperitivo: Motivação', youtube_id='Lgh8JgcYFwM')
    v.save()
    return v
@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))

def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404

def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)

def teste_conteudo_video(resp):
    assert_contains(resp, """<iframe
                    width="853"
                    height="480"
                    src="https://www.youtube.com/embed/Lgh8JgcYFwM"
                    title="Como instalar o Docker no Windows"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
            </iframe>""")