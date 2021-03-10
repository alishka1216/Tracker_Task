from django.contrib import admin
from django.urls import path

from webapp.views import (
    IndexView,
    ArticleView,
    RedirectView,
    article_create_view,
    article_update_view,
    article_delete_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='tracker-list'),  # URL для отображения списка статей
    path('articles/add/', tracker_create_view, name='tracker-add'),  # URL для создания статьи
    path('article/<int:pk>/', TrackerleView.as_view(), name='tracker-view'),  # URL для просмотра деталей статьи
    path('article/update/<int:pk>/', tracker_update_view, name='tracker-update'),
    path('article/delete/<int:pk>/', tracker_delete_view, name='tracker-delete')
]
