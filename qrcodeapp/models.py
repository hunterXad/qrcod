from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
# from django.utils import timezone
from datetime import datetime


class Event(models.Model):
    event_code = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=50, unique=False, null=False,
                                  blank=False, default='Startup', verbose_name='Name Of Event')
    image = models.ImageField(
        upload_to='%Y/%m/%d', null=False, blank=False, verbose_name='Image')
    namber_user = models.IntegerField(
        null=False, blank=False, default=50, verbose_name='Number Of User')
    ditils = models.TextField(
        null=False, blank=False, default='Welcome to my event, here I will write all details of the event', verbose_name='Details Of Event')
    date = models.DateTimeField(
        default=datetime.now, null=False, blank=False, verbose_name='Time Of Event')

    def __str__(self):
        return f'{self.event_code} - {self.name_event}'

    class Meta:
        ordering = ['-event_code']


class Applicant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(default=20)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')]

    )
    city = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    study_section = models.CharField(
        max_length=100)
    knew_event = models.CharField(
        max_length=30,
        choices=[("From Friend", "From Friend"), ("From Social Media",
                                                  "From Social Media"), ("Other", "Other")],

    )
    artving_at_time = models.CharField(
        max_length=30, choices=[('I Can', 'I Can'), ('I Try', 'I Try')])

    visit_hub200 = models.CharField(
        max_length=30,
        choices=[("Yes", "Yes"), ("No", "No")],

    )
    about_me = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Accepted(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.email


@receiver(post_save, sender=Applicant)
def create_accepted(sender, instance, **kwargs):

    if instance.is_accepted:

        Accepted.objects.create(
            name=instance.name,
            event=instance.event,
            email=instance.email,
            phone=instance.phone_number,
            is_accepted=True
        )


class Attendance(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    event = models.CharField(max_length=100)

    def __str__(self):
        return self.event
