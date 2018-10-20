from django import forms
from django.forms import modelformset_factory
from .models import Profile, Company


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['summary', 'totalExperience', 'cCTC', 'eCTC']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


CompanyFormset = modelformset_factory(
    Company,
    fields=['companyName', 'duration', 'designation', 'contribution'],
    extra=1
)f