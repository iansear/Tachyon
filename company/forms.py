from django.forms import ModelForm
from delivery.models import Company

class RegisterCompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'phone', 'email']
