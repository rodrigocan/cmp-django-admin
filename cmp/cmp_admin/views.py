from django.views import generic

from .models import Ticket

class IndexView(generic.ListView):
  template_name = 'cmp_admin/index.html'
  context_object_name = 'latest_ticket_list'

  def get_queryset(self):
    return Ticket.objects.order_by('-created_at')[:3]

class TicketDetailView(generic.DetailView):
  model = Ticket
  template_name = 'cmp_admin/ticket_detail.html'

class OpenTicketView(generic.CreateView):
  model = Ticket
  fields = ['contact_email', 'service', 'description']

class ShowTicketsView(generic.ListView):
  model = Ticket