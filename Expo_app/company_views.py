from django.contrib import messages
from django.shortcuts import render, redirect

from Expo_app.models import CreateExpo, OnlineForm, BookTickets, Company, BoothAllocation


def View_expo(request):
    data = CreateExpo.objects.all()
    return render(request,'company/expolist.html',{'data':data})


def take_appointment(request, id):
    expo_code = CreateExpo.objects.get(id=id)
    u = Company.objects.get(user=request.user)

    appointment = OnlineForm.objects.filter(user=u , expo_code=expo_code)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect("cmp_View_expo")
    else:
        if request.method == 'POST':
            obj = OnlineForm()
            name = request.POST.get("uname")
            number = request.POST.get("num")
            obj.name = name
            obj.number_of_booths = number
            obj.user = u
            obj.expo_code = expo_code
            obj.save()
            messages.info(request, 'Request send Successfully')
            return redirect('cmp_View_expo')
    return render(request, 'company/take_appointment.html', {'schedule': expo_code})


def booking_status(request):

    u = Company.objects.get(user=request.user)
    data = OnlineForm.objects.filter(user=u)

    return render(request,'company/bookstatus.html',{"data":data})


def view_booth_user(request):
    u = Company.objects.get(user=request.user)
    print(u)
    data = BoothAllocation.objects.filter(expocode__user =u)
    print(data)
    return render(request,"company/booth_view.html",{'data':data})


def checkout(request,id):
    n = OnlineForm.objects.get(id=id)
    if request.method == 'POST':
        n = OnlineForm.objects.get(id=id)
        n.status = 3
        n.save()
        messages.info(request, 'payment succesfull')
        return redirect('booking_status')


    return render(request, 'company/checkout.html',{'n':n})



def payment(request, id):
    n = OnlineForm.objects.get(id=id)
    n.status = 3
    n.save()
    messages.info(request, 'payment succesfull')
    return redirect('booking_status')