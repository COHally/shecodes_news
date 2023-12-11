from django.urls import path
from . import views
from .views import SearchView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('search/<str:username>/', SearchView.as_view(), name='search'),
    path('search/', SearchView.as_view(), name='search')
]
