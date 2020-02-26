from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.dashboard.views import dashboardIndex

urlpatterns = [
    path('', login_required(dashboardIndex), name='dashboard_index'),
]