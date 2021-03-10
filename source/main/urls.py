from django.contrib import admin
from django.urls import path

from webapp.views import (
    IndexView,
    TrackerView,
    RedirectView,
    TrackerUpdateView,
    TrackerDeleteView,
    TrackerCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='tracker-list'),
    path('tracker/add/', TrackerCreateView.as_view(), name='tracker-add'),
    path('tracker/<int:pk>/', TrackerView.as_view(), name='tracker-view'),
    path('tracker/update/<int:pk>/', TrackerUpdateView.as_view(), name='tracker-update'),
    path('tracker/delete/<int:pk>/', TrackerDeleteView.as_view(), name='tracker-delete')
    ]
