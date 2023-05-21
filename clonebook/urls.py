from django.contrib import admin
from django.urls import path
from social.views import *
from django.conf.urls.static import static
from clonebook import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='Home'),
    path('createProfile/', CreateProfileView, name='CreateProfile'),
    path('login/', LoginView, name='Login'),
    path('logout/', LogoutView, name='Logout'),
    path('createPost/', CreatePostView, name='CreatePost'),
    path('deletePost/<str:pid>', DeletePostView, name='DeletePost'),
    path('searchProfiles/', SearchProfilesView, name='SearchProfiles'),
    path('profile/<str:username>', ProfileView, name='Profile'),
    path('editProfile/<str:id>', EditProfileView, name='EditProfile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
