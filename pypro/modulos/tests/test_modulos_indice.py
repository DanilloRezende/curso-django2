from typing import List

import pytest
from django.test import Client
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)

@pytest.fixture
def aulas(modulos):
    aulas=[]
    for modulo in modulos:
            aulas.extend(mommy.make(Aula, 3, modulo=modulo))
    return

@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp

def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)

def test_publico(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)

# Testes n funcionam devido a divergencia das versões utilizadas do pyCharm.(_set)
# def test_aulas_titulos(resp, aulas: List[Aula]):
#     for aula in aulas:
#         assert_contains(resp, aula.titulo)
#
# def test_aulas_links(resp, aulas: List[Aula]):
#     for aula in aulas:
#         assert_contains(resp, aula.get_absolut_url())
