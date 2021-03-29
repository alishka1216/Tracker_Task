from django.contrib import admin
from django.urls import path

from webapp.views.trackers import (
    IndexView,
    TrackerView,
    TrackerUpdateView,
    TrackerDeleteView,
    CreateTrackerView,
    ProjectList,
    ProjectView,
    ProjectCreate
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='tracker-list'),
    path('tracker/add/', CreateTrackerView.as_view(), name='tracker-add'),
    path('tracker/<int:pk>/', TrackerView.as_view(), name='tracker-view'),
    path('tracker/update/<int:pk>/', TrackerUpdateView.as_view(), name='tracker-update'),
    path('tracker/delete/<int:pk>/', TrackerDeleteView.as_view(), name='tracker-delete'),
    path('', ProjectList.as_view(), name='project-list'),
    path('Project/<int:pk>/', ProjectView.as_view(), name='project-view'),
    path('Project/add/', ProjectCreate.as_view(), name='project-add')
    ]
