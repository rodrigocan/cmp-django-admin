from django.contrib import admin

from .models import Sector, Place, Info, Ticket

admin.site.register([Sector, Place, Info, Ticket])