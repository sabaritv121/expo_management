from django.contrib import messages
from django.shortcuts import render, redirect

from Expo_app.forms import ExpoForm, BoothAllocationForm
from Expo_app.models import Company, CreateExpo, OnlineForm, Feedback, BookTickets, BoothAllocation


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
    return render(request,'admin/bookstatus.html',{"data":data})


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

def feedbacks(request):
    n = Feedback.objects.all()
    return render(request,'admin/feedbacks.html',{'feedbacks':n})


def reply_feedback(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedbacks')
    return render(request, 'admin/admin_feedback.html', {'feedback': feedback})


def bookings_tkt(request):
    ticket = BookTickets.objects.all()
    bookings = ticket.count()
    return render(request, 'admin/bookings.html', {'ticket': ticket,'bookings':bookings})


def add_booth(request):
    form = BoothAllocationForm()
    if request.method == 'POST':
        form = BoothAllocationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_booth')
    return render(request,'admin/Booth.html',{'form':form})

def view_booth(request):
    data = BoothAllocation.objects.all()
    return render(request,"admin/booth_view.html",{'data':data})