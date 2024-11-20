from django.contrib import admin
from django.urls import path
from app.views import home, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('login/', login)
]
