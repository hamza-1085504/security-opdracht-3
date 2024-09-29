from django.urls import path
from experiential_experts import views

app_name = 'ervaringsdeskundige'

# Create your views here.

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('overzicht_afkeuring/<int:deskundige_id>', views.overzicht_afkeuring, name='overzicht_afkeuring'),
    path('overzicht_ervaringsdeskundige/', views.overzicht_ervaringsdeskundige, name='overzicht_ervaringsdeskundige'),
    path('aanpassen_ervaringsdeskundige/', views.aanpassen_ervaringsdeskundige, name='aanpassen_ervaringsdeskundige'),
    path('onderzoek_overzicht/', views.onderzoek_overzicht, name='onderzoek_overzicht'),
    path('inschrijven/<int:onderzoek_id>', views.inschrijven, name='inschrijven'),
    path('uitschrijven/<int:onderzoek_id>', views.uitschrijven, name='uitschrijven'),
    path('logout', views.logout_view, name='logout')
]
