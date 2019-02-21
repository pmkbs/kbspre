from django.conf.urls import url
from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    url(
        "all/", 
        view=views.ListAllImages.as_view(),
        name="all_images"
    ),
    
    url(
        "comments/sf",
        view=views.ListSfComments.as_view(),
        name="sf_comments"
    ),
    
    url(
        "comments/rf",
        view=views.ListRfComments.as_view(),
        name="sf_comments"
    ),
    
    url(
        "comments/ss",
        view=views.ListSsComments.as_view(),
        name="ss_comments"
    ),
    
    url(
        "comments/rs",
        view=views.ListRsComments.as_view(),
        name="ss_comments"
    ),
    
    url(
        "comments/st",
        view=views.ListStComments.as_view(),
        name="st_comments"
    ),
    
    url(
        "comments/rt",
        view=views.ListRtComments.as_view(),
        name="st_comments"
    ),
    
    url(
        "comments/",
        view=views.ListAllComments.as_view(),
        name="all_comments"
    ),

    url(
        "likes/", 
        view=views.ListAllLikes.as_view(),
        name="all_likes"
    ),
]
