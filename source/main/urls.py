from django.contrib import admin
from django.urls import path
from accounts.views import login_view
from webapp.views import (
    IndexView,
    TrackerView,
    TrackerUpdateView,
    TrackerDeleteView,
    CreateTrackerView,
    ProjectList,
    ProjectView,
    ProjectCreate,
    ProjectUpdate,
    ProjectDelete
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', IndexView.as_view(), name='tracker-list'),
    path('tracker/add/<int:pk>/', CreateTrackerView.as_view(), name='tracker-add'),
    path('tracker/<int:pk>/', TrackerView.as_view(), name='tracker-view'),
    path('tracker/update/<int:pk>/', TrackerUpdateView.as_view(), name='tracker-update'),
    path('tracker/delete/<int:pk>/', TrackerDeleteView.as_view(), name='tracker-delete'),
    path('', ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project-view'),
    path('project/add/', ProjectCreate.as_view(), name='project-add'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project-delete'),
    path('accounts/login', login_view, name='login')
    ]
