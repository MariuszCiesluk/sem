from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

from core.models import Task


class MainView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(MainView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.request.user
        return super(MainView, self).get_context_data(**kwargs)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegistrationView(FormView):
    pass


class TaskListView(ListView):
    model = Task
    template_name = 'task/list.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(MainView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    fields = ('user', 'name', 'priority')
    template_name = 'task/create.html'
    success_url = reverse_lazy('task_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(request, *args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('user', 'name', 'is_realized', 'priority')
    template_name = 'task/edit.html'
    success_url = reverse_lazy('task_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(request, *args, **kwargs)
