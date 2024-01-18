from customadmin import views
from django.urls import path

urlpatterns = [
    path("", views.admin_login, name="admin_login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.Logoutpage, name="logout"),
    path("globalsetting/", views.globalsetting, name="globalsetting"),
    path("main_navigation/<int:parent_id>/", views.main_navigation, name="main_navigation"),
    path("main_navigation/", views.main_navigation, name="main_navigation"),
    path("navigation/", views.navigation_list, name="navigation"),
    path("navigation/<int:parent_id>/", views.navigation_list, name="navigation"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete_nav/<int:pk>/", views.delete_nav, name="delete_nav"),
    
    
    
]