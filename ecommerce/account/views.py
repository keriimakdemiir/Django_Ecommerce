from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            print('fadsaasdf')
            user = form.save()

            print(user)
            user.save()


    context = {
        'form': form
    }

    return render(request, 'account/register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'account/my-login.html', context=context)


def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            else:
                del request.session[key]
    except KeyError:
        pass

    messages.success(request, 'Logout success')
    return redirect('store')


@login_required(login_url='my-login')
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.info(request, 'Update success!')

            return redirect('dashboard')

    context = {'user_form': user_form}

    return render(request, 'account/profile-management.html', context=context)



@login_required(login_url='my-login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.delete()

        messages.error(request, 'Account deleted')

        return redirect('store')

    return render(request, 'account/delete-account.html')


@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'account/dashboard.html')