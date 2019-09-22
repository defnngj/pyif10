from django.urls import path
from api import views
from api import more_api
from api import views_sec

urlpatterns = [
    # learning interface test:
    # ex : /api/hello_api/
    path('hello_api/', views.hello_api),
    path('get_events/', views.get_events),
    path('get_event_by_id/', views.get_event_by_id),
    path('get_event_by_name/', views.get_event_by_name),

    path('add_event/', views.add_event),
    path('update_event/', views.update_event),
    path('delete_event/', views.delete_event),

    path('guest_sign/', views.guest_sign),

    # 更多 api的使用
    path('hello/', more_api.hello),
    path('user/<int:uid>/', more_api.user),
    path('post_req/', more_api.post_req),
    path('header/', more_api.header),
    path('upload/', more_api.upload_file),

    # 安全机制
    path("user_auth", views_sec.user_auth),
    path("user_sign", views_sec.user_sign),
    path("user_aes", views_sec.user_aes),
]