from django.urls import path
from main.views import CreatorAPIView, CountryAPIView

urlpatterns = [
    path('creator/', CreatorAPIView.as_view()),
    path('country/', CountryAPIView.as_view())
]