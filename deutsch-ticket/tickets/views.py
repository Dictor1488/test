from django.shortcuts import render, get_object_or_404
from .models import Ticket

def home(request):
    """
    Главная страница с формой ввода ticket_number.
    """
    return render(request, 'tickets/home.html')

def view_ticket(request):
    """
    По ?q=NUMBER ищем тикет и либо показываем, либо 404.
    """
    num = request.GET.get('q', '').strip()
    ticket = get_object_or_404(Ticket, ticket_number=num)
    return render(request, 'tickets/ticket.html', {'ticket': ticket})
