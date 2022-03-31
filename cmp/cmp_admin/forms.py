from cProfile import label
from django import forms
from cmp_admin.models import Place

class OpenTicketForm(forms.Form):
  places = Place.objects.all()
  place = forms.ChoiceField(label = 'Local', choices = places)