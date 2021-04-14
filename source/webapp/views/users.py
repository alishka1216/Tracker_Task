from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker, Project
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import TrackerForm, SearchForm
from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class UserUpdateView(PermissionRequiredMixin,UpdateView):
    model = Project
    template_name = 'tracker/update.html'
    form_class = TrackerForm
    context_object_name = 'tracker'
    permission_required = 'webapp.add_user'