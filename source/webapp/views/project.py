from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker, Project
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import TrackerForm, SearchForm, ProjectForm
from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProjectList(ListView):
    template_name = 'projects/project_index.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('title',)
    paginate_by = 5



class ProjectView(DetailView):
    template_name = 'projects/project_view.html'
    model = Project
    context_object_name = 'project'


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.add_project'


    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'webapp.change_project'


    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'projects/project_delete.html'
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.delete_project'

    success_url = reverse_lazy('project-list')



