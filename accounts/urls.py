from django.urls import path 


from .views import signup, login, _logout, dashboard



urlpatterns = [

    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('signup/', _logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]