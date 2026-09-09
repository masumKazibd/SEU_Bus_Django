from django.contrib import admin
from django.urls import path
from schedule.views import route_list, route_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', route_list, name='route_list'),
    path('route/<int:route_id>/', route_detail, name='route_detail'),
]