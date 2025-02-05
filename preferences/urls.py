from django.urls import include, path
from .views import user_preferences, user_login, user_logout, user_status
from .views import account_settings, notification_settings, theme_settings, privacy_settings

urlpatterns = [
    path('api/preferences/', user_preferences),  # this can remain as it is if all preferences are in one model
    path('api/account/', account_settings, name='account_settings'),
    path('api/notifications/', notification_settings, name='notification_settings'),
    path('api/theme/', theme_settings, name='theme_settings'),
    path('api/privacy/', privacy_settings, name='privacy_settings'),
    
    path('api-auth/', include('rest_framework.urls')), 
    path('api/login/', user_login, name='user_login'), 
    path('api/logout/', user_logout, name='user_logout'),
    path("api/status/", user_status),
]
