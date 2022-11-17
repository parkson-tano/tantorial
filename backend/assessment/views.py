
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


class CreateAssessmentLanderView(TemplateView):
    template_name = 'create_assessment_lander.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assessments"] = AssessmentType.objects.all()
        return context


class CreateAssessmentView(CreateView):
    template_name = 'create_assessment.html'
    model = TeacherAssessment
    success_url = reverse_lazy('tantorial_assessment:my_assessment')
    form_class = TeacherAssessmentForm

    def form_valid(self, form, **kwargs):
        assessment = AssessmentType.objects.get(slug=self.kwargs['slug'])
        print(assessment)
        form.save(commit=False)
        form.instance.teacher = self.request.user.teacherprofile
        form.instance.assessment_type = assessment
        form.save()
        return super().form_valid(form)


class TeacherAssessmentView(ListView):
    template_name = 'my_created_assessment.html'
    model = TeacherAssessment
    context_object_name = 'my_assessments'

    def get_queryset(self):
        self.teacher = self.request.user.teacherprofile
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
        return redirect('tantorial_assessment:my_assessment')


class TeacherAssessmentUpdateView(UpdateView):
    model = TeacherAssessment
    form_class = TeacherAssessmentForm
    success_url = reverse_lazy('tantorial_assessment:my_assessment')
    template_name = "create_assessment.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if TeacherAssessment.teacher == request.user.teacherprofile:
                pass
            else:
                redirect('tantorial_assessment:my_assessment')
        else:
            return redirect('/accounts/login/?next=/my-assessment/')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return TeacherAssessment.objects.filter(teacher=self.request.user.teacherprofile.id)


class TeacherAssessmentDeleteView(DeleteView):
    model = TeacherAssessment
    success_url = reverse_lazy('tantorial:my_assessment')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if TeacherAssessment.teacher == self.request.user.teacherprofile:
                pass
        else:
            return redirect('/accounts/login/?next=/my-assessment/')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed assessment')
        return super().delete(request, *args, **kwargs)


# question for assessment

class CreateQuestionView(CreateView):
    template_name = 'create_question.html'
    model = Question
    success_url = reverse_lazy('tantorial_assessment:my_assessment')
    form_class = QuestionForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.account_type == 'teacher'):
            pass
        else:
            return redirect('/accounts/login/?next=/feed/assessment/my-assessment/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        assessment = TeacherAssessment.objects.get(id=self.kwargs['id'])
        form.save(commit=False)
        form.instance.assessment = assessment
        form.save()
        return super().form_valid(form)


class QuestionView(TemplateView):
    template_name = 'my_created_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        questions = Question.objects.filter(Q(assessment = pk) &
                                            Q(assessment__teacher = self.request.user.teacherprofile)).order_by('question_no')
        context['pk'] = pk
        context["questions"] = questions
        return context


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "create_question.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if Question.objects.filter(Q(assessment__teacher=self.request.user.teacherprofile.id) & Q(assessment__teacher = self.request.user.teacherprofile)):
                pass
            else:
                return redirect('tantorial_assessment:my_assessment')
        else:
            return redirect('/accounts/login/?next=/my-assessment/')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        quest_id = kwargs['pk']
        ques = Question.objects.get(id= quest_id)
        asse = ques.assessment.id
        if self.success_url:
            url = f'/feed/assessment/my-questions/{asse}'
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    def get_queryset(self):
        return Question.objects.filter(Q(assessment__teacher=self.request.user.teacherprofile))


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('tantorial_assessment:my_assessment')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if Question.assessment == self.request.user.teacherprofile:
                pass
        else:
            return redirect('/accounts/login/?next=/my-question/')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed question')
        return super().delete(request, *args, **kwargs)




class StudentTakeQuestionView(TemplateView):
    template_name = "question_student.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/student/feed')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assessment_id = kwargs['pk']
        assessment_info = TeacherAssessment.objects.get(id= assessment_id)
        try:
            m = StudentMark.objects.get(Q(student= self.request.user.studentprofile) & Q(test = assessment_info))
        except:
            m = False
        if m:
            pass
        else:
            assessment_info.student_count += 1
            assessment_info.save()
            student_mark = StudentMark(student= self.request.user.studentprofile,
                                       test = assessment_info
                                       )
            student_mark.save()
        question = Question.objects.filter(assessment= assessment_id)
        context["questions"] = question
        context['assessment_info'] = assessment_info
        return context

