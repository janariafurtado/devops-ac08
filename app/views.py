"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )
	

def contato(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contato.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def cadastro(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def detalhe_curso(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/detalhe_curso.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def disciplinas(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/disciplinas.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def esquecisenha(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/esquecisenha.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def lista_cursos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/lista_cursos.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def login(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def noticias(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/noticias.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def novadisciplina(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novadisciplina.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )
