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


class IndexView(ListView):
    template_name = 'trackers/index.html'
    model = Tracker
    context_object_name = 'trackers'
    ordering = ('title', '-created_ad')
    paginate_by = 10
    paginate_orphans = 3


class TrackerView(DetailView):
    template_name = 'trackers/view.html'
    model = Tracker
    context_object_name = 'tracker'


class CreateTrackerView(PermissionRequiredMixin, CreateView):
    template_name = 'trackers/create.html'
    model = Tracker
    form_class = TrackerForm
    permission_required = 'webapp.add_tracker'

    # def form_valid(self, form):
    #     project = form.save(commit=False)
    #     project.author = self.request.user
    #     project.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        tracker = form.save(commit=False)
        tracker.project = project
        tracker.save()
        form.save_m2m()

        return redirect('tracker-view', pk=tracker.pk)

    def get_success_url(self):
        return reverse('tracker-view', kwargs={'pk': self.object.pk})


class TrackerUpdateView(PermissionRequiredMixin,UpdateView):
    model = Tracker
    template_name = 'trackers/update.html'
    form_class = TrackerForm
    context_object_name = 'tracker'
    permission_required = 'webapp.change_tracker'

    def has_permission(self):
        return super().has_permission() \
               and self.request.username in self.get_object().author.all()

    def get_success_url(self):
        return reverse('tracker-view', kwargs={'pk': self.object.pk})


class TrackerDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'trackers/delete.html'
    model = Tracker
    context_object_name = 'tracker'
    permission_required = 'webapp.delete_tracker'

    success_url = reverse_lazy('tracker-list')







