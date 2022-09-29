import email
import re
from django.shortcuts import HttpResponseRedirect, redirect, render
import uuid
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View)
from accounts.forms import *
from accounts.models import ParentProfile
from subsystem.models import Subsystem, ClassRoom
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

class IndexView(TemplateView):
    template_name = "index.html"


class FeedView(TemplateView):
    template_name = "feedindex.html"

# class ChildProfileView(TemplateView):
#     template_name = 'my_children.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         children = ParentProfile.objects.filter(user = self.request.user)
#         context["children"] = children
#         return context
    
class ChildCreateView(CreateView):
    template_name = "my_children.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tantorial:child')

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