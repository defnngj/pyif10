from django.urls import path
from api import views

urlpatterns = [
    # learning interface test:
    # ex : /api/hello_api/
    path('hello_api/', views.hello_api),
    path('get_events/', views.get_events),
    path('get_event/', views.get_event),

]