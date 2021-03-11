from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker
from django.views.generic import View, TemplateView, RedirectView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from webapp.forms import TrackerForm


class IndexRedirectView(RedirectView):
    pattern_name = 'tracker-add'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['trackers'] = Tracker.objects.all()
        return super().get_context_data(**kwargs)


class TrackerView(TemplateView):
    template_name = 'tracker_view.html'

    def get_context_data(self, **kwargs):
        kwargs['tracker'] = get_object_or_404(Tracker, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class TrackerCreateView(TemplateView):
    template_name = 'tracker_create.html'

    def get_context_data(self, **kwargs):
        form = TrackerForm()
        kwargs['form'] = form
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker = Tracker.objects.create(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status'),
                type=form.cleaned_data.get('type'),
                description=form.cleaned_data.get('description')
            )
            return redirect('tracker-view', pk=tracker.pk)

        return render(request, 'tracker_create.html', {'form': form})


class TrackerUpdateView(TemplateView):
    template_name = 'tracker_update.html'

    def get_context_data(self, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(initial={
            'title': tracker.title,
            'description': tracker.description,
            'status': tracker.status,
            'type': tracker.type
        }
        )
        kwargs['form'] = form
        kwargs['tracker'] = tracker
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker.title = form.cleaned_data.get('title'),
            tracker.status = form.cleaned_data.get('status'),
            tracker.description = form.cleaned_data.get('description'),
            tracker.type = form.cleaned_data.get('type')
            tracker.save()

            return redirect('tracker-view', pk=tracker.pk)

        return render(request, 'tracker_update.html', {'form': form, "tracker": tracker})


class TrackerDeleteView(TemplateView):
    template_name = 'tracker_delete.html'

    def post(self, request, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        tracker.delete()
        return redirect('tracker-list')
