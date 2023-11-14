from django.urls import path

from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

from .views import SignUpView, CustomLoginView

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('aktualnosci/',TemplateView.as_view(template_name='actual.html'), name='aktualnosci'),
    path('opis/',TemplateView.as_view(template_name='project.html'), name='opis'),
    path('zespol/',TemplateView.as_view(template_name='project1.html'), name='zespol'),
    path('kontakt/',TemplateView.as_view(template_name='contact.html'), name='kontakt'),

]