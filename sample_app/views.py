from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def cabinetView(request):
    return render(request, 'cabinet_page.html')


def homeView(request):
    return render(request, 'home_page.html')
