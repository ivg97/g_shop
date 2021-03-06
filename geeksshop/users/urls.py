from django.urls import path



from .views import LoginListView, RegisterListView, ProfileFormView, RegisterListView, Logout, verify

app_name = 'users'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),

    path('verify/<str:email>/<str:activation_key>/', verify, name='verify')

]
