from django.urls import path 
from .views import Posts, AddPost,PutPost,index

urlpatterns=[ 
    path("", Posts, name="posts"), 
    path("add/", AddPost, name="add_post"), 
    path("put/", PutPost, name="update"), 
    path("main/", index, name="main")
]