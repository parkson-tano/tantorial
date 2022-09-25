from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class RegisterLanderView(TemplateView):
    template_name = 'main\signupLander.html'

class StudentRegister(CreateView):
    pass
    # template_name = 'main/student-signup.html'
    # form_class = UserRegistrationForm
    # success_url = reverse_lazy('tantorial_auth:index')

    # def form_valid(self, form):
    #     password = form.cleaned_data.get('password')
    #     email = form.cleaned_data.get('email')
    #     acc_type = 'student'
    #     first_name = form.cleaned_data.get('first_name')
    #     last_name = form.cleaned_data.get('last_name')
    #     phone_number = form.cleaned_data.get('phone_number')
    #     user = User.objects.create_user(username=first_name, email=email, password=password, account_type = acc_type,
    #      first_name = first_name, last_name=last_name, phone_number=phone_number)
    #     form.instance.user = user
    #     login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
    #     return super().form_valid(form)


class ParentRegister(CreateView):
    pass


class TeacherRegister(CreateView):
    pass


class SchoolRegister(CreateView):
    pass

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('tantorial:index')