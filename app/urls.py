from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_,name='login' ),
    path('signup/',views.signup,name='signup'),
    path('todo/',views.todo,name='todo'),
    path('edit/<int:srno>',views.edit,name='edit'),
    path('delete/<int:srno>',views.delete,name='delete'),
    path('logout',views.logout_,name='logout'),
]
