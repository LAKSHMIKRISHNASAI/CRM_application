from django.urls import path 
# from .views import home_view,register_view,login_view
from . import views
urlpatterns = [
    path('', views.home_view,name='home' ),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('create_record/',views.create_record,name='create_record'),
    path('update/<int:id>',views.update_record,name='update_record'),
    path('view_record/<int:id>',views.single_record,name='view_record'),
    path('delete/<int:id>',views.delete_record,name='delete_record'),
]

