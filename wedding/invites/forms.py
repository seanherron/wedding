from django import forms

from extra_views import InlineFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML



from .models import Guest, Invite

class RSVPLookupForm(forms.Form):
    zip_code = forms.CharField(max_length=5)
    last_name = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(RSVPLookupForm, self).clean()
        last_name = cleaned_data.get('last_name')
        zip_code = cleaned_data.get('zip_code')
        guest = Guest.objects.filter(last_name=last_name, invite__zip_code=zip_code).first()
        if not guest:
            raise forms.ValidationError("No Invitation Found.")
        else:
            cleaned_data['invite'] = guest.invite
            return self.cleaned_data

class GuestForm(forms.ModelForm):
    attending_wedding = forms.ChoiceField(
        choices = (
            ('','----------'),
            (False, "I won't be able to make the wedding."),
            (True, "Yes, I'll be there!")
        ),
        initial = '',
        label='Will you be able to attend the wedding on Saturday, April 22, 2017?'
    )
    attending_family_dinner = forms.ChoiceField(
        choices = (
            ('','----------'),
            (False, "I won't be able to make the family dinner."),
            (True, "Yes, I'll be there!")
        ),
        initial = '',
        label='Will you be able to attend the family dinner on Thursday, April 20th at 6:30pm?'
    )
    attending_friends_dinner = forms.ChoiceField(
        choices = (
            ('','----------'),
            (False, "I won't be able to make the friends dinner."),
            (True, "Yes, I'll be there!")
        ),
        initial = '',
        label="Do you plan on attending our friend's dinner on Friday, April 21st? Details to come."
    )

    class Meta:
        model = Guest
        fields = [
            'first_name',
            'last_name',
            'email',
            'attending_wedding',
            'meal_choice',
            'attending_family_dinner',
            'attending_friends_dinner'
        ]

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['first_name'].disabled = True
        self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].disabled = True
        if kwargs.get('instance'):
            guest = kwargs['instance']
            if not guest.invited_to_family_dinner:
                del self.fields['attending_family_dinner']
            if not guest.invited_to_friends_dinner:
                del self.fields['attending_friends_dinner']
        else:
            self.fields['first_name'].widget.attrs['readonly'] = False
            self.fields['first_name'].disabled = False
            self.fields['last_name'].widget.attrs['readonly'] = False
            self.fields['last_name'].disabled = False
            del self.fields['attending_family_dinner']
            del self.fields['attending_friends_dinner']
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
                HTML("""
                    <h3>Guest</h3>
                """),
                Div(
                    Div('first_name',css_class='col-md-6',),
                    Div('last_name',css_class='col-md-6',),
                    css_class='row',
                ),
                'email'
            )





class GuestInline(InlineFormSet):
    def __init__(self, *args, **kwargs):
        super(GuestInline, self).__init__(*args, **kwargs)
        if self.object.has_plusone:
            number_of_guests = Guest.objects.filter(invite=self.object).count()
            if number_of_guests > 1:
                self.extra = 0
            else:
                self.extra = 1
        else:
            self.extra = 0

    model = Guest
    can_delete = False
    form_class = GuestForm
