from django import forms
from django.contrib.auth.forms import AuthenticationForm

from cmp_admin.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('place_id', 'contact_email', 'sector_id', 'contact_phone',
                  'description', 'subject_id', 'service_id', 'requester')
        
        widgets = {
          'place_id': forms.Select(attrs = {'class': 'select'}),
          'contact_email': forms.EmailInput(attrs = {'class': 'input', 'placeholder': 'Digite o seu e-mail de contato'}),
          'sector_id': forms.Select(attrs = {'class': 'select'}),
          'contact_phone': forms.TextInput(attrs = {'class': 'input', 'placeholder': 'Digite aqui o telefone de contato'}),
          'description': forms.Textarea(attrs = {'class': 'textarea', 'placeholder': 'Descreva aqui o problema encontrado'}),
          'subject_id': forms.Select(attrs = {'class': 'select'}),
          'service_id': forms.Select(attrs = {'class': 'select'}),
          'requester': forms.TextInput(attrs = {'class': 'input', 'placeholder': 'Digite aqui o seu nome'})
        }

class LoginForm(AuthenticationForm):
  username = forms.CharField(label = 'Usuário:', widget = forms.TextInput(attrs = {'class': 'input'}))
  password = forms.CharField(label = 'Senha:', widget = forms.PasswordInput(attrs = {'class': 'input'}))