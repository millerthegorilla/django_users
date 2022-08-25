import uuid  # used as custom salt

from django import forms, http, shortcuts, urls
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django_email_verification import send_email

from . import forms as users_forms


class Register(generic.edit.CreateView):
    http_method_names = ["get", "post"]
    template_name = "django_users/register.html"
    form_class = users_forms.CustomUserCreation
    success_url = urls.reverse_lazy("confirmation_sent")
    model = auth.get_user_model()

    def form_valid(self, form: forms.ModelForm, user=None) -> http.HttpResponseRedirect:
        super().form_valid(form)
        if user is None:
            user = form.save()
        user.is_active = False
        user.save()
        send_email(user)
        return shortcuts.redirect(self.success_url)


class ResendConfirmation(generic.FormView):
    http_method_names = ["get", "post"]
    template_name = "django_users/resend_form.html"
    extra_context = {"instructions": "Resend confirmation token"}
    form_class = users_forms.UserResendConfirmation
    success_url = urls.reverse_lazy("confirmation_sent")

    def form_valid(self, form, **kwargs) -> http.HttpResponse:
        super().form_valid(form)
        try:
            user = auth.get_user_model().objects.get(username=form["username"].value())
            if user.is_active is False:
                send_email(user)
                return shortcuts.render(self.request, self.success_url, {form: form})
            else:
                return shortcuts.render(self.request, self.template_name, {form: form})
        except auth.get_user_model().DoesNotExist:
            form.errors = [
                {"username": "Hey you haven't registered yet.  Register first!"}
            ]
            return shortcuts.render(self.request, self.template_name, {form: form})


class ConfirmSent(generic.View):
    template_name = "django_users/registration_confirmation_sent.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)


class Profile(LoginRequiredMixin, generic.View):
    template_name = "django_users/profile.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)
