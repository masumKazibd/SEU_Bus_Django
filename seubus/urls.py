from django.contrib import admin
from django.urls import path
from schedule.views import route_list, route_detail, register_view, login_view, logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', route_list, name='route_list'),
    path('route/<int:route_id>/', route_detail, name='route_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]