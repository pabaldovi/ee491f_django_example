from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('descending/', views.DescendingDateView.as_view(), name='descending'),
    path('today/', views.TodayPostView.as_view(), name='today'),
    path('today_descending/', views.TodayDescendingView.as_view(), name='today_descending'),
    path('search/', views.SearchView.as_view(), name='search'),
]