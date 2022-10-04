from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
