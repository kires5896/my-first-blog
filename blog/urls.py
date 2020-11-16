from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #comentario
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #borradores
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #eliminar_post
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]