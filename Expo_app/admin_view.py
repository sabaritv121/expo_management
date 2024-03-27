from django.contrib import messages
from django.shortcuts import render, redirect

from Expo_app.forms import ExpoForm
from Expo_app.models import Company, CreateExpo, OnlineForm


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

def bookings(request):

    data = OnlineForm.objects.all()
    return render(request,'company/bookstatus.html',{"data":data})


def approve_appointment(request, id):
    n = OnlineForm.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('bookings')


def reject_appointment(request, id):
    n = OnlineForm.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('bookings')

