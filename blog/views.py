from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from datetime import date
from .filters import PostFilter

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    model = Post

class CreateView(generic.edit.CreateView):
    template_name = 'blog/create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:index')

class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Post

class UpdateView(generic.edit.UpdateView):
    template_name = 'blog/update.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'blog/delete.html'
    model = Post
    success_url = reverse_lazy('blog:index')

class DescendingDateView(generic.ListView):
    template_name = 'blog/index.html'
    
    def get_queryset(self):
        return Post.objects.order_by('-published_date')

class TodayPostView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__date=date.today())

class TodayDescendingView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__date=date.today()).order_by('-published_date')

class SearchView(generic.ListView):
    template_name = 'blog/search.html'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context