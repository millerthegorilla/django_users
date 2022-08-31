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

    def form_valid(
        self, form: users_forms.CustomUserCreation
    ) -> http.HttpResponseRedirect:
        super().form_valid(form)
        user = form.save()
        send_email(user)
        return shortcuts.redirect(self.success_url)


class ResendConfirmation(generic.FormView):
    http_method_names = ["get", "post"]
    template_name = "django_users/resend_form.html"
    extra_context = {"instructions": "Resend confirmation token"}
    form_class = users_forms.UserResendConfirmation
    success_url = urls.reverse_lazy("confirmation_sent")


class ConfirmSent(generic.View):
    template_name = "django_users/registration_confirmation_sent.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)


class Profile(LoginRequiredMixin, generic.View):
    template_name = "django_users/profile.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)
