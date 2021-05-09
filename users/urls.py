from django.urls import path
from .views import login_page, logout_page, profile_page, write_message, get_inbox, all_profiles
urlpatterns = [
     path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('send_message/', write_message, name='send_message'),
    path('inbox/',get_inbox, name='inbox'),
    path('profiles/', all_profiles, name = 'allProfiles'),

 ]