from behave import when, then, given
from nose.tools import assert_equal

from pages.google_page import GooglePage

# Instanciando Page
googlePage = GooglePage()


@given('que acesso a pagina do Google')
def step_impl(context):
    googlePage.acessar_pagina('https://www.google.com.br/')


@given('que preencho o campo de pesquisa com Python')
def step_impl(context):
    googlePage.preenche_campo_pesquisa('Python')


@when('clico no botao de pesquisar')
def step_impl(context):
    googlePage.clica_botao_pesquisar()


@then('devo visualizar os resultados')
def step_impl(context):
    assert_equal(googlePage.get_texto_resultado(), 'Python')
