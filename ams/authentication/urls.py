from django.urls import path
from .views import *

urlpatterns = [
    path("org/<service_type>", OrganizationView.as_view()),
    path("cand/<service_type>", CandidateView.as_view())
]