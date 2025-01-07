from django.urls import path
from django.contrib import admin
from .views import team_list, stadium_list, event_list, ticket_list, register, login_view, buy_ticket, check_ticket

urlpatterns = (
    path('admin/', admin.site.urls),
    path("api/stadiums", stadium_list),
    path('api/teams/', team_list, name='team_list'),
    path('api/stadiums/', stadium_list, name='stadium_list'),
    path('api/events/', event_list, name='event_list'),
    path('api/tickets/', ticket_list, name='ticket_list'),
    path('api/register/', register, name='register'),
    path('api/login/', login_view, name='login'),
    path('api/buy-ticket/', buy_ticket, name='buy_ticket'),
    path('api/check-ticket/<uuid:ticket_id>/', check_ticket, name='check_ticket'),
)
