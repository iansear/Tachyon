from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import CharField
from django.forms import ModelChoiceField
from django.forms import PasswordInput
from delivery.models import Courier
from delivery.models import Company
from delivery.models import Job

class RegisterCourierForm(ModelForm):

    alias = CharField(label = ("Employee Alias"))
    phone = CharField(label = ("Personal Phone"))
    
    class Meta:
        model = Courier
        fields = ['alias', 'phone']

class RegisterCompanyForm(ModelForm):

    name = CharField(label = ("Company Name"))
    phone = CharField(label = ("Company Phone"))
    email = CharField(label = ("Company Email address"))

    class Meta:
        model = Company
        fields = ['name', 'phone', 'email']

class RegisterUserForm(UserCreationForm):

    error_messages = { 'password_mismatch': ("The two passwords do not match."),}
    
    password1 = CharField(label = ("Password"),
                widget = PasswordInput)
    
    password2 = CharField(label = ("Password Confirmations"),
                widget = PasswordInput,
                help_text = ("Enter the same password as above."))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class AssignCourierForm(ModelForm):

    def __init__(self, user_id):
        print 'init'
        self.user_id = user_id
        courier = Courier.objects.filter(user = user_id)
        company = Company.objects.filter(courier = courier)
        super(AssignCourierForm, self).__init__(user_id)
        self.fields['alias'].queryset = Courier.objects.filter(companies = company)
        print 'exit init'

    print 'class'
    roster = ModelChoiceField(queryset = None, empty_label="(------)")
    print 'roster'

    class Meta:
        model = Job
        fields = ['courier']
