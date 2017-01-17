from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import redirect

from hashids import Hashids
from extra_views import UpdateWithInlinesView, InlineFormSet

from .forms import GuestInline, RSVPLookupForm
from .models import Invite, Guest
# Create your views here.

class RSVPLookupView(FormView):
    template_name = 'invites/lookup.html'
    form_class = RSVPLookupForm

    def form_valid(self, form):
        return redirect('RSVPView', hashid=form.cleaned_data['invite'].generate_absolute_url())

class RSVPView(UpdateWithInlinesView):
    model = Invite
    fields = []
    inlines = [GuestInline]
    template_name = 'invites/rsvp.html'
    success_url = reverse_lazy('RSVPThanks')

    def get_object(self):
        hashids = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH)
        print(self.kwargs['hashid'])
        hashid = hashids.decode(self.kwargs['hashid'])[0]
        return Invite.objects.get(id=hashid)

class RSVPThanksView(TemplateView):
    template_name = 'invites/thanks.html'
