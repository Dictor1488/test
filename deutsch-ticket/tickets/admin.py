from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display  = ('ticket_number','first_name','last_name','valid_from','valid_to')
    search_fields = ('ticket_number','first_name','last_name')
    fields = (
        'ticket_number','first_name','last_name','qr_code',
        ('valid_from','valid_to'),
        'territory','ticket_class',
        'birth_date',
    )
