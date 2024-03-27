from django.contrib import messages
from django.shortcuts import render, redirect

from Expo_app.models import CreateExpo, OnlineForm, users, BookTickets


def View_expo(request):
    data = CreateExpo.objects.all()
    return render(request,'users/expolist.html',{'data':data})



def take_tickets(request, id):
    expo_code = CreateExpo.objects.get(id=id)
    u = users.objects.get(user=request.user)
    appointment = BookTickets.objects.filter(user=u , expo_code=expo_code)
    if appointment.exists():
        messages.info(request, 'You Have Already purchased tickets for this expo')
        return redirect("user_view_expo")
    else:
        if request.method == 'POST':
            obj = BookTickets()
            obj.user = u
            ticket = request.POST.get("ticket")
            mobile = request.POST.get("mobile")
            obj.number_of_tickets = ticket
            obj.mobile = mobile
            obj.expo_code = expo_code
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('my_tickets')
    return render(request, 'users/take_tickets.html', {'schedule': expo_code})


def my_tickets(request):
    u= request.user
    user = users.objects.get(user=u)
    ticket = BookTickets.objects.filter(user=user)
    return render(request,'users/my_ticket.html',{'ticket':ticket})