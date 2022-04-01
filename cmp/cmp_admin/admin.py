from django.contrib import admin

from .models import Sector, Place, Info, Ticket, Subject, Service, Status

admin.site.register([Sector, Place, Info, Ticket, Subject, Service, Status])