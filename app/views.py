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

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Gerenciador de vestibulares',
            'year':datetime.now().year,
        })
    )

def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
#            'cursos': ['ADS' , 'SI', 'CC'],
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )

