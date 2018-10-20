from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from .models import Profile,Company
from .forms import ProfileForm, CompanyFormset



def signup(request):
    if request.method == "POST":
        if request.POST['Password1'] == request.POST['Password2']:
            try:
                User.objects.get(username=request.POST['UserName'])
                return render(request, 'poles/signup.html', {'err': "User-Id already exist"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['UserName'], password=request.POST['Password1'])
                login(request, user)
                return redirect(create_profile)
        else:
            return render(request, "poles/signup.html", {'err': "Please confirm password"})
    else:
        return render(request, "poles/signup.html")


def logins(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['UserName'], password=request.POST['Password'])
        if user is not None:
            login(request, user)
            if request.POST.get('next1'):
                return redirect(request.POST["next1"])

            return redirect('create_profile')
        else:
            return render(request, "poles/login.html", {'err': "Invalid Id password"})
    else:
        return render(request, "poles/login.html")


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def create_profile(request):
    instance = Profile.objects.filter(user=request.user).last()
    if request.method == "GET":
        pform = ProfileForm(instance=instance)
        formset = CompanyFormset(queryset=Company.objects.filter(profile__user=request.user))

    elif request.method == 'POST':
        pform = ProfileForm(request.POST, instance=instance)
        formset = CompanyFormset(request.POST)
        if pform.is_valid() and formset.is_valid():
            profile = pform.save(commit=False)
            profile.user = request.user
            profile.save()
            for form in formset:
                company = form.save(commit=False)
                company.profile = profile
                company.save()
            #return redirect('create_profile')
    return render(request, 'poles/Profile.html', {'pform': pform, 'formset': formset})

