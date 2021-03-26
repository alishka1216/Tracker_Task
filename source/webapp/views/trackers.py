from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Tracker
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import TrackerForm, SearchForm
from webapp.base_view import CustomFormView, CustomListView


class IndexRedirectView(RedirectView):
    pattern_name = 'tracker-add'


class IndexView(ListView):
    template_name = 'trackers/index.html'
    model = Tracker
    context_object_name = 'trackers'
    ordering = ('title', '-created_ad')
    paginate_by = 10
    paginate_orphans = 3

    def get(self, request):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super().get(request)

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self):
        context = super().get_context_data()
        context['search_form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset


    # def get_context_data(self, **kwargs):
    #     kwargs['trackers'] = Tracker.objects.all())
    #     return super().get_context_data(**kwargs)


class TrackerView(TemplateView):
    template_name = 'trackers/tracker_view.html'

    def get_context_data(self, **kwargs):
        kwargs['tracker'] = get_object_or_404(Tracker, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)



class CreateTrackerView(CustomFormView):
    template_name = 'trackers/create.html'
    form_class = TrackerForm
    redirect_url = 'tracker-list'

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        tracker = Tracker()
        for key, value in form.cleaned_data.items():
            setattr(tracker, key, value)

        tracker.save()
        tracker.type.set(type)

        return super().form_valid(form)

# class TrackerCreateView(TemplateView):
#     template_name = 'tracker_create.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['form'] = TrackerForm()
#         return super().get_context_data(**kwargs)
#
#     def post(self, request, **kwargs):
#         form = TrackerForm(data=request.POST)
#         if form.is_valid():
#             tracker = Tracker.objects.create(
#                 title=form.cleaned_data.get('title'),
#                 status=form.cleaned_data.get('status'),
#                 description=form.cleaned_data.get('description')
#             )
#             tracker.type.set(form.cleaned_data.get('type'))
#             return redirect('tracker-view', pk=tracker.pk)
#
#         return render(request, 'tracker_create.html', {'form': form})
#

#
# class TrackerUpdateView(FormView):
#     form_class = TrackerForm
#     template_name = 'tracker_update.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         self.tracker = self.get_object()
#         return super().dispatch(self, request, *args, **kwargs)
#
#     def get_initial(self):
#         return super().get_initial()
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.tracker
#         return kwargs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tracker'] = self.tracker
#         return context
#
#     def get_object(self):
#         tracker = get_object_or_404(
#             Tracker, id=self.kwargs.get('pk'))
#         return tracker
#
#     def form_valid(self, form):
#         tags = form.cleaned_data.pop('tags')
#         form.save()
#         self.tracker.tags.set(tags)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('tracker-view', kwargs={'pk': self.kwargs.get('pk')})



class TrackerUpdateView(TemplateView):
    template_name = 'trackers/tracker_update.html'

    def get_context_data(self, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(initial={
            'title': tracker.title,
            'description': tracker.description,
            'status': tracker.status,
            'type': tracker.type.all()
        }
        )
        kwargs['form'] = form
        kwargs['tracker'] = tracker
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker.title = form.cleaned_data.get('title')
            tracker.status = form.cleaned_data.get('status')
            tracker.description = form.cleaned_data.get('description')
            tracker.type.set(form.cleaned_data.get('type'))
            tracker.save()

            return redirect('tracker-view', pk=tracker.pk)

        return render(request, 'trackers/tracker_update.html', {'form': form, "tracker": tracker})


class TrackerDeleteView(TemplateView):
    template_name = 'trackers/tracker_delete.html'

    def post(self, request, **kwargs):
        tracker = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        tracker.delete()
        return redirect('tracker-list')




