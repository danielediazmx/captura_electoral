from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.sector.views import SectorCreate, SectorUpdate, destroySector, SectorIndex

urlpatterns = [
    path('',login_required(SectorIndex.as_view()), name='sector_index'),
    path('create', login_required(SectorCreate.as_view()), name='sector_create'),
    path('edit/<int:pk>', login_required(SectorUpdate.as_view()), name='sector_edit'),
    path('delete/<int:id>', login_required(destroySector), name='sector_delete'),

]