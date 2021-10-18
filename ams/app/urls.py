from django.urls import path
from .views import AttendanceView

urlpatterns = [
    path("<slot>",AttendanceView.as_view())
]