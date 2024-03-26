from django.shortcuts import render

from Expo_app.models import CreateExpo


def View_expo(request):
    data = CreateExpo.objects.all()
    return render(request,'users/expolist.html',{'data':data})
