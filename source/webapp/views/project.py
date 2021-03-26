from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import TrackerForm, SearchForm
from webapp.base_view import CustomFormView, CustomListView


class Project(ListView)