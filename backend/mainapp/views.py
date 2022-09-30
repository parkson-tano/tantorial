import email
import re
from django.shortcuts import HttpResponseRedirect, redirect, render
import uuid
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View, UpdateView)
from accounts.forms import *
from accounts.models import ParentProfile
from subsystem.models import Subsystem, ClassRoom
from assessment.forms import *
# Create your views here.
from django.contrib.auth import get_user_model
from assessment.models import AssessmentType
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


class CreateAssessmentLanderView(TemplateView):
    template_name = 'create_assessment_lander.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assessments"] = AssessmentType.objects.all()
        return context
    
class CreateAssessmentView(CreateView):
    template_name = 'create_assessment.html'
    model = TeacherAssessment
    success_url = reverse_lazy('tantorial:my_assessment')
    form_class = TeacherAssessmentForm
    
    def form_valid(self, form, **kwargs):
        assessment = AssessmentType.objects.get(slug=self.kwargs['slug'])
        print(assessment)
        form.save(commit=False)
        form.instance.teacher =  self.request.user.teacherprofile
        form.instance.assessment_type = assessment
        form.save()
        return super().form_valid(form)

class TeacherAssessmentView(ListView):
    template_name = 'my_created_assessment.html'
    model = TeacherAssessment
    context_object_name = 'my_assessments'

    def get_queryset(self):
        self.teacher =  self.request.user.teacherprofile
        return TeacherAssessment.objects.filter(teacher=self.teacher)


class ManageAssessmentView(View):
    def get(self, request, **kwargs):
        assessment_id = self.kwargs['id']
        action = request.GET.get('action')
        assessment = TeacherAssessment.objects.get(id=assessment_id)
        assessment.save()

        if action == 'publish':
            assessment.publish = True
            assessment.save()
        elif action == 'unpublish':
            assessment.publish = False
            assessment.save()
        return redirect('tantorial:my_assessment')

class TeacherAssessmentUpdateView(UpdateView):
    model = TeacherAssessment
    form_class = TeacherAssessmentForm
    success_url = reverse_lazy('tantorial:my_assessment')
    template_name = "create_assessment.html"