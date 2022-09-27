from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .mixins import RedirectAuthenticatedUserMixin

User = get_user_model()


class RegisterLanderView(RedirectAuthenticatedUserMixin, TemplateView):
    template_name = 'main\signupLander.html'


class RegisterBaseView(RedirectAuthenticatedUserMixin, CreateView):
    """
    Serves as a base view for all user registration activities
    It should not be called directly
    """

    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tantorial:index')
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


class StudentRegister(RegisterBaseView):
    template_name = 'main/student-signup.html'
    account_type = "student"


class ParentRegister(RegisterBaseView):
    template_name = 'main/student-signup.html'
    account_type = "parent"


class TeacherRegister(RegisterBaseView):
    template_name = 'main/student-signup.html'
    account_type = "teacher"


class SchoolRegister(RegisterBaseView):
    template_name = 'main/student-signup.html'
    account_type = "school"
