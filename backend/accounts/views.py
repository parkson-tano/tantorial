from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class RegisterLanderView(TemplateView):
    template_name = 'main\signupLander.html'


class RegisterView(CreateView):
    """
    Serves as a base view for all user registration activities
    It should not be called directly
    """

    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tantorial_auth:index')
    account_type: str  # should be provided by a child class
    template_name: str  # should be provided by a child class

    def form_valid(self, form):
        object = form.save(commit=False)
        object.account_type = self.account_type
        object.save()
        user = authenticate(
            username=form.cleaned_data['email'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class StudentRegister(RegisterView):
    template_name = 'main/student-signup.html'
    account_type = "student"


class ParentRegister(RegisterView):
    template_name = 'main/student-signup.html'
    account_type = "parent"


class TeacherRegister(RegisterView):
    template_name = 'main/student-signup.html'
    account_type = "teacher"


class SchoolRegister(RegisterView):
    template_name = 'main/student-signup.html'
    account_type = "school"
