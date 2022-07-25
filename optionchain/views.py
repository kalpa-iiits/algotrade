from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect


def optionchain(request):
    return render(request, 'hello.html')
