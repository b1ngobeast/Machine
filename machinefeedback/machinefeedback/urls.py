from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from main.views import CreatorAPIView, CountriesAPIView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls'), name='main'),
                  path('api/creator', CreatorAPIView.as_view()),
                  path('api/countries', CountriesAPIView.as_view()),
                  path('api/countries/<str:type>', CountriesAPIView.as_view())
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
