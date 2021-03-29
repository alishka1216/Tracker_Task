from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker, Project
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import TrackerForm, SearchForm, ProjectForm
from webapp.base_view import CustomFormView, CustomListView


class ProjectList(ListView):
    template_name = 'projects/project_index.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('title',)
    paginate_by = 10
    paginate_orphans = 3


class ProjectView(DetailView):
    template_name = 'projects/project_view.html'
    model = Project
    context_object_name = 'project'


class ProjectCreate(CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm

    # success_url = 'project-view'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})
