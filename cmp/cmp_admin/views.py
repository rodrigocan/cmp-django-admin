from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ticket
from .forms import TicketForm, LoginForm

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'cmp_admin/index.html'
  context_object_name = 'earliest_open_ticket_list'

  def get_queryset(self):
    return Ticket.objects.filter(status_id = 1).order_by('created_at')[:3]

class TicketDetailView(generic.DetailView):
  model = Ticket
  template_name = 'cmp_admin/ticket_detail.html'

class OpenTicketSuccessView(generic.CreateView):
  form_class = TicketForm
  template_name = 'cmp_admin/open_ticket_success.html'

class OpenTicketView(generic.CreateView):
  form_class = TicketForm
  template_name = 'cmp_admin/open_ticket.html'
  success_url = '/cmp_admin/open_ticket_success/'

class ShowTicketsView(generic.ListView):
  model = Ticket
  template_name = 'cmp_admin/show_tickets.html'
  context_object_name = 'all_tickets'

  def get_queryset(self):
    return Ticket.objects.all().order_by('created_at')

class LoginView(auth_views.LoginView):
  form_class = LoginForm
  template_name = 'cmp_admin/login.html'