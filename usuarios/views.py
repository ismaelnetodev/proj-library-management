from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request, "cadastro.html")