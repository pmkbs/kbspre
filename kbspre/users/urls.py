from django.urls import path
from . import views

from kbspre.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
'''
app_name = "users"
urlpatterns = [
    path(
        "",
        view=views.UserListView.as_view(),
        name="list"),
    path(
        "~redirect/", 
        view=views.UserRedirectView_as_view(),
        name="redirect"),
    path(
        "~update/", 
        view=views.UserUpdateView_as_view(),
        name="update"),
    path(
        "<str:username>/",
        view=views/UserDetailView_as_view(),
        name="detail"),
]

'''