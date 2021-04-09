from django.shortcuts import render, redirect


from accounts.forms import UserRegisterForm

# Create your views here.


def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)

