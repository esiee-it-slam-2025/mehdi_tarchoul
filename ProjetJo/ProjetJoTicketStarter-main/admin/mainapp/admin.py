from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.admin import AdminSite
from mainapp.models import Event, Stadium, Team, Ticket

admin.site.register(Event)
admin.site.register(Stadium)
admin.site.register(Team)
admin.site.register(Ticket)

class CustomAdminSite(AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('events/', self.admin_view(self.events_view), name="admin_events"),
        ]
        return custom_urls + urls

    def events_view(self, request):
        if not request.user.is_superuser:
            return redirect('/admin/login/')
        
        events = Event.objects.all()
        return TemplateResponse(request, "admin_view/events.html", {"events": events})
site_header = "Administration Projet JoTicket"
admin_site = CustomAdminSite(name='custom_admin')


