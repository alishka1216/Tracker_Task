from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from accounts.models import Profile
from webapp.models import BaseModel, Tracker, Project
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            form.save()
            return redirect('project-list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserListView(PermissionRequiredMixin, ListView):
    template_name = 'user_list.html'
    model = Profile
    context_object_name = 'profiles'
    permission_required = 'accounts.view_profile'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        user_form = self.get_form()
        profile_form = self.get_profile_form()

        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)

        return self.form_invalid(user_form, profile_form)


    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = kwargs.get('profile_form')
        if context['profile_form'] is None:
            context['profile_form'] = self.get_profile_form()

        return context

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(
            form=user_form,
            profile_form=profile_form)
        return self.render_to_response(context)

    def form_valid(self, user_form, profile_form):
        responce = super().form_valid(user_form)
        profile_form.save()
        return responce

    def get_profile_form_class(self):
        return self.profile_form_class

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return self.get_profile_form_class()(**form_kwargs)

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': self.object.pk})


class UserChangePasswordView(LoginRequiredMixin, UpdateView):
    template_name = 'user_change_password.html'
    model = get_user_model()
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super(UserChangePasswordView, self).form_valid(form)
        update_session_auth_hash(self.request, self.request.user)
        return response

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': self.object.pk})