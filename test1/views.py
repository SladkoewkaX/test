from django.shortcuts import render
from .models import Just

def show_text(request):
    txt = Just.objects.all()
    return render(request, 'test.html', {'name':txt})