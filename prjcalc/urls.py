from django.contrib import admin
from django.urls import path
from appcalc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fnindex),
    path('calc/', views.fncalc),
]
