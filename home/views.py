from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Member


def redirect_home(request):
    return redirect('home')


def home(request):
    return render(request, 'home.html')


def members(request):
    professor = Member.objects.filter(position='0').get()
    professor_description = Member.objects.filter(position='0').get().description.split('{!x!}')[0]
    professor_books = Member.objects.filter(position='0').get().description.split('{!x!}')[1].split(';')
    professor_history = Member.objects.filter(position='0').get().description.split('{!x!}')[2].split(';')
    undergraduates = Member.objects.filter(Q(position='1') | Q(position='2') | Q(position='3')).order_by('position')
    graduates = Member.objects.filter(position='4')
    return render(request, 'members.html', {'professor': professor, 'professor_description': professor_description, 'professor_books': professor_books, 'professor_history': professor_history, 'undergraduates': undergraduates, 'graduates': graduates})

    
def projects(request):
    return render(request, 'projects.html')
