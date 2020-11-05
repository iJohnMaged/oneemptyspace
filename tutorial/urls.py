from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('hello_world.urls')),
    path('admin/', admin.site.urls),
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
