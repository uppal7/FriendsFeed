from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm


@login_required
def index(request):
	return render(request,'feed/index.html',{})


def signup(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST,request.FILES)
		if form.is_valid():
			user = form.save(commit=False)
			user.photo = request.FILES['photo']
			return redirect(reverse('login'))
		else:
			print(form.error)
	return render(request,'feed/signup.html',{'form':form})

def profile(request,pk):
	user = get_object_or_404(User,pk=pk)
	return render(request,'feed/profile.html',{'user':user})

def friends(request,pk):
	user = get_object_or_404(User,pk=pk)
	friends = user.friend_set.all()
	return render(request,'feed/friends.html',{'friends':friends})

def add_profile(request,user_id):
	user = get_object_or_404(User,pk=user_id)
	form = ProfileForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		profile = form.save(commit=False)
		profile.photo = request.FILES['photo']
		profile.user = user
		profile.save()
		return redirect('profile',user_id)
	return render(request,'feed/profile_form.html',{'form':form})

def fprofile(request,name):
	user = get_object_or_404(User,username=name)
	return render(request,'feed/fprofile.html',{'user':user})