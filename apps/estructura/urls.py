from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from .views import index, create, update, destroy

urlpatterns = [
    path('', login_required(index.as_view()), name='estructura_index'),
    path('create', login_required(create.as_view()), name='estructura_create'),
    path('edit/<int:pk>', login_required(update.as_view()), name='estructura_edit'),
    path('delete/<int:id>', login_required(destroy), name='estructura_delete'),
]