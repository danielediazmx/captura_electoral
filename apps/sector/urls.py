from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.sector.views import SectorCreate, SectorUpdate, destroySector, SectorIndex

urlpatterns = [
    path('',SectorIndex.as_view(), name='sector_index'),
    path('create', SectorCreate.as_view(), name='sector_create'),
    path('edit/<int:pk>', SectorUpdate.as_view(), name='sector_edit'),
    path('delete/<int:id>', destroySector, name='sector_delete'),

]