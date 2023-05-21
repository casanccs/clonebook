from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def HomeView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Login"))
    profile = Profile.objects.get(user=request.user)  
    posts = Post.objects.all().order_by('-created')
    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'home.html', context)

def CreateProfileView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Home"))
    if request.method == "POST":
        try:
            form = request.POST
            user = User.objects.create_user(username=form['username'] , password=form['password'])
            user.email = form['email']
            name = form['fullname'].split() #['Cristian', 'Sanchez']
            user.first_name = name[0]
            if not len(name) == 1:
                user.last_name = name[-1]
            user.save()
            profile = Profile(user=user, dob=form['dob'], gender=form['gender'], bio=form['bio'], 
                            city=form['city'], country=form['country'], ppic=request.FILES['ppic'])
            profile.save()
            login(request,user)
            return HttpResponseRedirect(reverse("Home"))
        except:
            return HttpResponseRedirect(reverse("CreateProfile"))

    return render(request, 'createProfile.html')

def LoginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Home"))
    if request.method == "POST":
        form = request.POST
        user = authenticate(username=form['username'], password=form['password'])
        if not user:
            return HttpResponseRedirect(reverse("Login"))
        login(request,user)
        return HttpResponseRedirect(reverse("Home"))
    
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))

def CreatePostView(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = request.POST
        post = Post(title=form['title'], desc=form['desc'], profile=profile)
        if request.FILES:
            post.pic = request.FILES['pic']
        post.save()
        return HttpResponseRedirect(reverse("Home"))
    
    return render(request, 'createPost.html')

def DeletePostView(request, pid):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.get(id=pid)
    if profile ==  post.profile:
        post.delete()

    return HttpResponseRedirect(reverse("Home"))

def SearchProfilesView(request):
    profiles = Profile.objects.all()
    if request.method == "POST":
        form = request.POST
        profiles = Profile.objects.filter(user__username__icontains=form['username'])
    context = {
        'profiles': profiles,
    }
    return render(request, 'searchProfiles.html', context)

def ProfileView(request, username):
    profile = Profile.objects.get(user__username=username)
    posts = Post.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'profile.html', context)

def EditProfileView(request, id):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
    if request.method == "POST":
        form = request.POST
        profile.user.username = form['username']
        profile.user.email = form['email']
        profile.bio = form['bio']
        profile.city = form['city']
        profile.country = form['country']
        if request.FILES:
            profile.ppic = request.FILES['ppic']
        profile.user.save()
        profile.save()
        return HttpResponseRedirect(reverse("Home"))

    return render(request, 'editProfile.html', context)