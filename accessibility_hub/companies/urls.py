from django.urls import path
from .views import Register, Login, Research, Question

app_name = 'companies'

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('onderzoek/', Research.as_view()),
    path('vraag/', Question.as_view()),
]
