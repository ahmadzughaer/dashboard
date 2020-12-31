from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('quotes', views.quotes),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('quote', views.quote_post),
    path('update', views.update),
    path('myaccount/<user_id>', views.edit),
    path('quote/<quote_id>', views.add_favorite_for_current_user),
    path('remove/<quote_id>', views.remove_from_favourites) ,
    path('users/<user_id>', views.users),
    path('dashboard', views.dashboard),

]