from django.urls import path
from api import views

urlpatterns = [
    # learning interface test:
    # ex : /api/hello_api/
    path('hello_api/', views.hello_api),
    path('get_events/', views.get_events),
    path('get_event/', views.get_event),
    path('get_event_by_name/', views.get_event_by_name),

    path('add_event/', views.add_event),
    path('update_event/', views.update_event),
    path('delete_event/', views.delete_event),

    path('guest_sign/', views.guest_sign),


]