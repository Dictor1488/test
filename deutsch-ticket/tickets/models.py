from django.db import models

class Ticket(models.Model):
    ticket_number  = models.CharField("Ticket-Nr",        max_length=20, unique=True)
    first_name     = models.CharField("Vorname",           max_length=30)
    last_name      = models.CharField("Nachname",          max_length=30)
    qr_code        = models.ImageField("QR-Code",          upload_to='qrcodes/')

    valid_from     = models.DateTimeField("Gültig von")
    valid_to       = models.DateTimeField("Gültig bis")
    territory      = models.CharField("Geltungsbereich",   max_length=100, default="Deutschlandweit")
    ticket_class   = models.CharField("Klasse",            max_length=50,  default="2. Klasse")
    birth_date     = models.DateField("Geburtsdatum",       null=True, blank=True)

    def __str__(self):
        return f"{self.ticket_number} — {self.first_name} {self.last_name}"
