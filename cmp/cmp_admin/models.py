from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
  name = models.CharField(max_length = 255)
  city = models.CharField(max_length = 255)
  state = models.CharField(max_length = 255)
  address = models.CharField(max_length = 255)
  zip_code = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class Sector(models.Model):
  name = models.CharField(max_length = 255)
  place_id = models.ForeignKey(Place, on_delete = models.SET_NULL, null = True)
  email = models.EmailField()
  phone_number = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class Info(models.Model):
  description = models.TextField()
  user_id = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.description

class Subject(models.Model):
  name: models.CharField(max_length = 255)
  service: models.ManyToManyField('Service')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class Service(models.Model):
  name: models.CharField(max_length = 255)
  subject_id = models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class Ticket(models.Model):
  place_id = models.ForeignKey(Place, on_delete = models.SET_NULL, null = True)
  contact_email = models.EmailField()
  sector_id = models.ForeignKey(Sector, on_delete = models.SET_NULL, null = True)
  contact_phone = models.CharField(max_length = 255)
  service = models.CharField(max_length = 255)
  description = models.TextField(max_length = 255)
  assigned_to_id = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
  infos = models.ManyToManyField('Info')
  status = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  subject_id = models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True)
  service_id = models.ForeignKey(Service, on_delete = models.SET_NULL, null = True)

  def __str__(self):
    return str(self.pk)

  # def get_ticket_infos():
  #   infos = Info.objects.filter

  # Adicionar método para calcular o tempo que o chamado está aberto.