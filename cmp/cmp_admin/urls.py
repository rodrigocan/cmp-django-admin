from django.urls import path

from . import views

app_name = 'cmp_admin'
urlpatterns = [
  path('', views.IndexView.as_view(), name = 'index'),
  path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name = 'ticket_detail'),
  path('open_ticket/', views.OpenTicketView.as_view(), name = 'open_ticket'),
  path('show_tickets/', views.ShowTicketsView.as_view(), name = 'show_tickets'),
  path('open_ticket_success/', views.OpenTicketSuccessView.as_view(), name = 'open_ticket_success'),
  path('login/', views.LoginView.as_view(), name = 'login')
]