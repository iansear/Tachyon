from django.conf import settings
from django.db import models

class Job(models.Model):
    company = models.ForeignKey('Company')
    client = models.ForeignKey('Client')
    courier = models.ForeignKey('Courier')
    round_trip = models.BooleanField()
    time_frame = models.DurationField()
    pick_company = models.CharField(max_length=100)
    pick_name = models.CharField(max_length=100)
    pick_address = models.CharField(max_length=100)
    pick_phone = models.CharField(max_length=20)
    pick_email = models.EmailField(max_length=254)
    drop_company = models.CharField(max_length=100)
    drop_name = models.CharField(max_length=100)
    drop_address = models.CharField(max_length=100)
    drop_phone = models.CharField(max_length=20)
    drop_email = models.EmailField(max_length=254)
    instructions = models.TextField(blank=True)
    package_type = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=12, decimal_places=2)
    zones = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    submit_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    claim_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    pick_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    pick_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    drop_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    pod = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    job_status = models.CharField(max_length=20)
    payment_status = models.BooleanField()
    billing_status = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    company = models.ForeignKey('Company')
    user = models.OneToOneField('auth.User')
    alias = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.alias

class Courier(models.Model):
    companies = models.ManyToManyField('Company')
    user = models.OneToOneField('auth.User')
    alias = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, null=True)
    is_working = models.NullBooleanField()

    def __str__(self):
        return self.alias

class Price(models.Model):
    company = models.ForeignKey('Company')
    base_rate = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    double_rate = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    triple_rate = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    asap = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    zone = models.IntegerField(blank=True)
    oversize = models.BooleanField()
    double_oversize = models.BooleanField()
    vehicle = models.BooleanField()
    vehicleoversize = models.BooleanField()
    am_afterhours = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    pm_afterhours = models.TimeField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.company

