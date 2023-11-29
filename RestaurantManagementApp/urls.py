from django.urls import path

from RestaurantManagementApp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.loginfun,name='login'),
    path('logout',views.logoutfun,name='logout'),
    path('register',views.registerfun,name='register'),
    path('add',views.addfun,name='add'),
    path('edit/<int:id>',views.editfun,name='edit'),
    path('delete/<int:id>',views.deletefun,name='delete'),
    path('dummy',views.dummy,name='dummy'),
    path('search',views.searchBar,name='search')

]