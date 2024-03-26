from django.shortcuts import render, redirect

from Expo_app.forms import ExpoForm
from Expo_app.models import Company, CreateExpo


def cmp_view(request):
    data = Company.objects.all()
    return render(request,'admin/cmp_view.html',{'data':data})




def users_approval(request,id):
    data = Company.objects.get(id=id)
    data.status = True
    data.save()
    return redirect('cmp_view')


def Expo_create(request):
    form = ExpoForm()
    if request.method == 'POST':
        form = ExpoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('View_expo')
    return render(request,'admin/expo_create.html',{'form':form})


def View_expo(request):
    data = CreateExpo.objects.all()
    return render(request,'admin/expo.html',{'data':data})
