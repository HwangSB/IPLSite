from django.shortcuts import render, redirect


def redirect_home(request):
    return redirect('home')


def home(request):
    return render(request, 'home.html')


def members(request):
    return render(request, 'members.html', {"undergraduates": range(5), "graduates": range(2)})

    
def projects(request):
    return render(request, 'projects.html')
