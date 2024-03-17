from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Events', views.Events, name="Events"),
    path('Gallery', views.Gallery, name="Gallery"),
    path('Team', views.Team, name="Team"),
]