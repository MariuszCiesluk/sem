from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelformset_factory
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from reversion import revisions as reversion

from core.models import Task, TaskListElement


class MainView(TemplateView):
    """ Main View, where User has a hiperlink to his Tasks """
    template_name = 'index.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(MainView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.request.user
        return super(MainView, self).get_context_data(**kwargs)


class LoginView(FormView):
    """ Login View, prepared with django builtin form AuthenticationForm
    dispatcher have three decorators:
    * for password
    * csrf mechanism protection
    * not to cache!
    """
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('mainpage')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    Simple logout redirectView, url is for next page
    to logout, used builtin logout function from django
    """
    url = reverse_lazy('mainpage')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegistrationView(FormView):
    """
    Registration View, used builtin form UserCreationForm
    with double matching password check
    """
    form_class = UserCreationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class TaskListView(ListView):
    """
    List View for display Tasks of logged User
    Queryset is limited
    """
    model = Task
    template_name = 'task/list.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.prefetch_related('items').filter(user=self.request.user)


class TaskCreateView(CreateView):
    """
    Create View for new tasks
    """
    model = Task
    fields = ('name', 'priority')
    template_name = 'task/create.html'
    success_url = reverse_lazy('task_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    """
    Update View with formset for items in Tasks
    """
    model = Task
    fields = ('user', 'name', 'is_realized', 'priority')
    template_name = 'task/edit.html'
    success_url = reverse_lazy('task_list')
    item_formset = modelformset_factory(model=TaskListElement, extra=2, can_delete=True, fields=('checked', 'description'))

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        formset = self.item_formset(self.request.POST)
        if formset.is_valid():
            for form_set in formset:
                form_set.instance.task = form.instance
            formset.save()
        return super(TaskUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adding list of previous versions of object and formset with items
        :param kwargs:
        :return: context data
        """
        kwargs['task_versions'] = reversion.get_for_object(self.object).get_unique()
        kwargs['item_formset'] = self.item_formset(queryset=TaskListElement.objects.filter(task=self.object))
        return super(TaskUpdateView, self).get_context_data(**kwargs)


class TaskDeleteView(DeleteView):
    """
    View for delete objects
    """
    model = Task
    success_url = reverse_lazy('task_list')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
