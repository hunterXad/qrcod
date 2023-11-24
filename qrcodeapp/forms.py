from django import forms
from .models import Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['event', 'name', 'age', 'email', 'phone_number', 'gender', 'city', 'university',
                  'study_section', 'knew_event', 'visit_hub200', 'artving_at_time', 'about_me']


class ApplicantUpdateForm(forms.ModelForm):
    accept = forms.BooleanField(
        required=False, initial=False, label='قبول الطلب')  # حقل لتعقب حالة القبول

    class Meta:
        model = Applicant
        fields = ['is_accepted']
