from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.organismo.views import OrganismoCreate, OrganismoUpdate, destroyOrganismo, OrganismoIndex

urlpatterns = [
    path('', OrganismoIndex.as_view(), name='organismo_index'),
    path('create', OrganismoCreate.as_view(), name='organismo_create'),
    path('edit/<int:pk>', OrganismoUpdate.as_view(), name='organismo_edit'),
    path('delete/<int:id>', destroyOrganismo, name='organismo_delete'),
]