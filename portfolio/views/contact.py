import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

import resend

from portfolio.forms import ContactForm
from portfolio.models import SiteSettings

logger = logging.getLogger(__name__)


class ContactView(FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("portfolio:contact")

    def dispatch(self, request, *args, **kwargs):
        if not SiteSettings.get().contact_enable:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data.get("phone", "")
        method = form.cleaned_data.get("phone_method", "phone")
        message = form.cleaned_data["message"]

        lines = [f"From: {name} <{email}>"]
        if phone:
            label = "WhatsApp" if method == "whatsapp" else "Phone"
            lines += [f"{label}: {phone}"]
        lines += ["", message]

        try:
            resend.api_key = settings.RESEND_API_KEY
            resend.Emails.send(
                {
                    "from": settings.CONTACT_FROM_EMAIL,
                    "to": settings.CONTACT_TO_EMAIL,
                    "reply_to": email,
                    "subject": f"Pixelmonks contact: {name}",
                    "text": "\n".join(lines),
                }
            )
            messages.success(self.request, "Message sent — I'll be in touch soon.")
        except Exception as exc:
            logger.error("Resend failure: %s", exc)
            messages.error(
                self.request,
                "Message could not be sent right now. "
                "Please email dmanpearl@pixelmonks.com directly.",
            )

        return super().form_valid(form)
