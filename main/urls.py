from django.urls import path
from .views import HomeView, ContactView, ContactCreateView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create'),
]