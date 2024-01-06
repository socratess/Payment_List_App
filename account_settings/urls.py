from django.urls import path
from . import views
from django.urls import reverse, reverse_lazy

app_name = 'account_settings'


urlpatterns = [
    path('', views.UserInformationView.as_view(), name='UserInformation_all'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='UserUpdate_all'),
    path('<int:pk>/inactive', views.UserInactiveView.as_view(), name='UserInactive_all'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(success_url=reverse_lazy("home:home_all")), name='UserDelete_all'),
]
