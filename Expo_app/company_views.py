from django.shortcuts import render

from Expo_app.models import CreateExpo


def View_expo(request):
    data = CreateExpo.objects.all()
    return render(request,'company/expolist.html',{'data':data})
