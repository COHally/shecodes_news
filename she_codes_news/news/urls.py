from django.urls import path
from . import views
from .views import like_NewsStory, unlike_NewsStory

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('like/<int:NewsStory_id>/', like_NewsStory, name='like_NewsStory'),
    path('unlike/<int:NewsStory_id>/', unlike_NewsStory, name='unlike_NewsStory'),
]
