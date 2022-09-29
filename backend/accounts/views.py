from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect

from .mixins import RedirectAuthenticatedUserMixin
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View)
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, PasswordResetForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.db.models import Q
import uuid 
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterLanderView(RedirectAuthenticatedUserMixin, TemplateView):
    template_name = 'signupLander.html'


class RegisterBaseView(RedirectAuthenticatedUserMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tantorial:feed_index')
    code: str
    account_type: str  # should be provided by a child class
    template_name: str  # should be provided by a child class

    def form_valid(self, form):
        object = form.save(commit=False)
        object.account_type = self.account_type
        object.code = self.code
        object.save()
        user = authenticate(
            username=form.cleaned_data['email'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

register_page =  'registration.html'
student_register_page = 'student_register.html'

class StudentRegister(RegisterBaseView):
    template_name =  student_register_page
    account_type = "student"
    code = f'STD/{uuid.uuid4().hex[:6].upper()}/TAN'


class ParentRegister(RegisterBaseView):
    template_name =  register_page
    account_type = "parent"
    code = f'PRT/{uuid.uuid4().hex[:6].upper()}/TAN'


class TeacherRegister(RegisterBaseView):
    template_name = register_page
    account_type = "teacher"
    code = f'TUT/{uuid.uuid4().hex[:6].upper()}/TAN'


class SchoolRegister(RegisterBaseView):
    template_name =  register_page
    account_type = "school"
    code = f'SCH/{uuid.uuid4().hex[:6].upper()}/TAN'

class LoginView(FormView):
	template_name = 'login.html'
	form_class =  LoginForm
	success_url = reverse_lazy('tantorial:index_feed')

	def form_valid(self, form):
		email = form.cleaned_data.get('email')
		pword = form.cleaned_data.get('password')
		usr = authenticate(email = email, password=pword)
		if usr is not None:
			login(self.request, usr)
		else:
			return render(self.request, self.template_name, {'form': self.form_class, 'error':'invalid creditials'})	
		return super().form_valid(form)

	def get_success_url(self):
		if 'next' in self.request.GET:
			next_url = self.request.GET.get('next')
			print(next_url)
			return next_url 	
		else:
			return self.success_url
@login_required
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change')
            return redirect('ecommerceapp:customerprofile')
        else:
            return render(request, 'forgotpassword/password_change.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'forgotpassword/password_change.html', {'form':form})

def password_reset_request(request):
    password_reset_form = PasswordResetForm()
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "forgotpassword/reset_subject.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=True)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message has been sent to your email')
                    return redirect ("/")
            messages.error(request, 'Email address in invalid')
            return render(request=request, template_name="forgotpassword/password_reset.html", context={"password_reset_form":password_reset_form})
    return render(request=request, template_name="forgotpassword/password_reset.html", context={"password_reset_form":password_reset_form})
class LogoutView(View):
	
	def get(self, request):
		logout(request)
		return redirect('tantorial:index')
