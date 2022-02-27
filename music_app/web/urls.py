from django.urls import path

from music_app.web.views import show_index, add_album, details_album, edit_album, delete_album, profile_details, \
    profile_delete, profile_create

urlpatterns = (
    path('', show_index, name='show index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', details_album, name='details album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),

)


