from django.views.generic import View, TemplateView, ListView
from django.shortcuts import render, redirect


class CustomFormView(View):
    template_name = None
    form_class = None
    redirect_url = None

    def get(self, request):
        form = self.form_class()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request,
                      self.template_name,
                      context={
                            **self.get_context_data(),
                            "form": form
                      }
                      )

    def get_context_data(self, **kwargs):
        return kwargs

    def get_redirect_url(self):
        return self.redirect_url


class CustomListView(TemplateView):
    model = None
    context_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_name] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()
