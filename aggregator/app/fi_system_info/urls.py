from django.urls import path

from . import views


urlpatterns = [
    path("agents/", views.agent_list, name="agent_list"),
    path("agents/<int:pk>/", views.agent_detail, name="agent_detail")
]
