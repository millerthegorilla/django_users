import uuid  # used as custom salt

from django import forms, http, shortcuts, urls
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django_email_verification import send_email
from django.conf import settings

from . import forms as users_forms


class Register(generic.edit.CreateView):
    http_method_names = ["get", "post"]
    template_name = "django_users/register.html"
    form_class = users_forms.CustomUserCreation
    success_url = urls.reverse_lazy("confirmation_sent")
    model = auth.get_user_model()

    def post(self, request) -> http.HttpResponseRedirect:
        if settings.DEBUG:
            settings.EMAIL_PAGE_DOMAIN = request.scheme + "://" + request.get_host()
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            send_email(user)
            return shortcuts.redirect(self.success_url)
        else:
            return shortcuts.render(request, self.template_name, {"form": form})


class ResendConfirmation(generic.FormView):
    http_method_names = ["get", "post"]
    template_name = "django_users/resend_form.html"
    extra_context = {"instructions": "Resend confirmation token"}
    form_class = users_forms.UserResendConfirmation
    success_url = urls.reverse_lazy("confirmation_sent")

    def post(self, request):
        if settings.DEBUG:
            settings.EMAIL_PAGE_DOMAIN = (
                self.request.scheme + "://" + self.request.get_host()
            )
        form = self.form_class(request.POST)
        if form.is_valid():
            user = auth.get_user_model().objects.get(username=form["username"].value())
            send_email(user)
            return shortcuts.redirect(self.success_url)
        else:
            return shortcuts.render(
                request,
                self.template_name,
                {"form": form, "instructions": "Resend confirmation token"},
            )


class ConfirmSent(generic.View):
    template_name = "django_users/registration_confirmation_sent.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)


class Profile(LoginRequiredMixin, generic.View):
    template_name = "django_users/profile.html"

    def get(self, request):
        return shortcuts.render(request, self.template_name)
