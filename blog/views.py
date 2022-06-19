from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

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