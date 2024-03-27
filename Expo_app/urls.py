from django.urls import path

from Expo_app import views, admin_view, company_views, users_view
from Expo_app.views import RegistrationView





urlpatterns = [
    # path("",views.home,name="home"),
    path('reg', RegistrationView.as_view(), name='registration'),
    path("",views.home,name="index"),
    path("login_page",views.Login_page,name="login_page"),

    path("logout_view",views.logout_view,name='logout_view'),
    path('admin_dash',views.admin_dash,name='admin_dash'),
    path("company_dash",views.company_dash,name="company_dash"),
    path('shops_dash',views.shops_dash,name='shops_dash'),
    path('visiter_dash',views.visiter_dash,name='visiter_dash'),

    #admin
    path("cmp_view",admin_view.cmp_view,name = "cmp_view"),
    path("users_approval/<int:id>/",admin_view.users_approval,name='users_approval'),
    path('Expo_create',admin_view.Expo_create,name = "Expo_create"),
    path('View_expo',admin_view.View_expo,name = 'View_expo'),
    path('bookings',admin_view.bookings,name='bookings'),
    path('approve_appointment/<int:id>/', admin_view.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', admin_view.reject_appointment, name='reject_appointment'),



    #company
    path('cmp_View_expo',company_views.View_expo, name='cmp_View_expo'),
    path('take_appointment/<int:id>/',company_views.take_appointment,name="take_appointment"),
    path('booking_status',company_views.booking_status,name='booking_status'),

    #users
    path('user_view_expo',users_view.View_expo,name= 'user_view_expo'),
    path("take_tickets/<int:id>/",users_view.take_tickets,name ="take_tickets"),
    path("my_tickets",users_view.my_tickets,name='my_tickets'),
]