from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Contact
from account.forms import YueeeeeeeeUserCreationForm

# Create your views here.
def dashboard(request):
    return render(
        request,
        'account/dashboard.html'
    )

def user_list(request):
    user_list = User.objects.all()
    return render(
        request,
        'account/user_list.html',
        {'user_list': user_list}
    )

def register(request):
    if request.method == 'POST':
        user_form = YueeeeeeeeUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        user_form = YueeeeeeeeUserCreationForm()
        return render(
            request,
            'account/register.html',
            {'user_form': user_form}
        )

@login_required
def profile(request, username):
    user = User.objects.filter(username=username).first()
    return render(
        request,
        {'user': user}
    )

@login_required
def follow(request, username):
    user_following = request.user
    user_followed = User.objects.filter(username=username).first()
    con = Contact(user_following=user_following, user_followed=user_followed)
    con.save()
    return redirect('account:profile', username=username)

@login_required
def unfollow(request, username):
    user_following = request.user
    user_followed = User.objects.filter(username=username).first()
    con = Contact.objects.filter(user_following=user_following, user_followed=user_followed).first()
    if con:
        con.delete()
    return redirect('account:profile', username=username)