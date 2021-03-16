from django.views.generic import View


class CustomFormView(View):
    template_name = None
    form_class = None

    def get(self):
        form = self.form_class()

    def post(self):
        pass

    def get_context_data(self, **kwargs):
        return kwargs