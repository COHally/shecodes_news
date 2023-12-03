from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import NewsStory, Like


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def like_NewsStory(request, NewsStory_id):
    NewsStory = get_object_or_404(NewsStory, pk=NewsStory_id)
    Like.objects.get_or_create(user=request.user, NewsStory=NewsStory)
    return redirect('NewsStory_detail', NewsStory_id=NewsStory.id)

@login_required
def unlike_NewsStory(request, NewsStory_id):
    NewsStory = get_object_or_404(NewsStory, pk=NewsStory_id)
    Like.objects.filter(user=request.user, NewsStory=NewsStory).delete()
    return redirect('NewsStory_detail', NewsStory_id=NewsStory.id)   
    
