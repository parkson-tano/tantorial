
import uuid

from django.contrib import messages
# Create your views here.
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView, View)

from accounts.forms import *
from accounts.models import ParentProfile
from assessment.forms import *
from assessment.models import AssessmentType
from subsystem.models import ClassRoom, Subsystem

User = get_user_model()

class IndexView(TemplateView):
    template_name = "index.html"

class FeedView(TemplateView):
    template_name = "feedindex.html"

class ChildCreateView(CreateView):
    template_name = "my_children.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tantorial:child')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.account_type == 'parent':
                pass
        else:
            return redirect('/accounts/login/?next=/feed/all')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.code = f'STD/{uuid.uuid4().hex[:6].upper()}/TAN'
        form.instance.account_type = 'student'
        form.save()
        parent_child = ParentProfile.objects.create(user = self.request.user, child=User.objects.get(email=form.instance.email),
        relation = self.request.POST.get('relationship')
        )
        parent_child.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ChildCreateView, self).get_context_data(**kwargs)
        children = ParentProfile.objects.filter(user = self.request.user)
        context["children"] = children
        return context


# Stduent assessment

class StudentIndexView(TemplateView):
    template_name = 'student_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_class = self.request.user.student_class
        my_assessments = TeacherAssessment.objects.filter(Q(assessment_class = student_class) & Q(publish = True))
        context["my_assessments"] = my_assessments
        return context

class TeacherDashboard(TemplateView):
    template_name = 'dashboard/teacher.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.account_type == 'teacher':
                pass
        else:
            return redirect('/accounts/login/?next=/dashboard/teacher')

        return super().dispatch(request, *args, **kwargs)
class StudentDashboard(TemplateView):
    template_name = 'dashboard/student.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.account_type == 'student':
                pass
        else:
            return redirect('/accounts/login/?next=/dashboard/student')

        return super().dispatch(request, *args, **kwargs)
class ParentDashboard(TemplateView):
    template_name = 'dashboard/parent.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.account_type == 'parent':
                pass
        else:
            return redirect('/accounts/login/?next=/dashboard/parent')

        return super().dispatch(request, *args, **kwargs)
class SchoolDashboard(TemplateView):
    template_name = 'dashboard/school.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.account_type == 'school':
                pass
        else:
            return redirect('/accounts/login/?next=/dashboard/school')

        return super().dispatch(request, *args, **kwargs)
