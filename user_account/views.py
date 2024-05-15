from django.shortcuts import render, redirect
from .forms import user_registration_form
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username} !')
            return redirect('blog-home')
    else:
        form = user_registration_form()

    return render(request, 'user_account/register.html',{'form': form})
