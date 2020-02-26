from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.organismo.views import OrganismoCreate, OrganismoUpdate, destroyOrganismo, OrganismoIndex

urlpatterns = [
    path('', login_required(OrganismoIndex.as_view()), name='organismo_index'),
    path('create', login_required(OrganismoCreate.as_view()), name='organismo_create'),
    path('edit/<int:pk>', login_required(OrganismoUpdate.as_view()), name='organismo_edit'),
    path('delete/<int:id>', login_required(destroyOrganismo), name='organismo_delete'),
]