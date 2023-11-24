from .models import Event
from .models import Attendance  # استيراد نموذج الحضور
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import base64
from django.core.mail import EmailMessage
from .models import Event, Accepted, Applicant
from django.shortcuts import render
from io import BytesIO
from django.shortcuts import render, redirect
import qrcode
from .forms import ApplicantForm
from django.contrib.auth.decorators import user_passes_test
from django.dispatch import receiver
from django.db.models.signals import post_save
from .forms import ApplicantForm


@receiver(post_save, sender=Accepted)
def create_qr_code_and_send_email(sender, instance, **kwargs):
    if instance.is_accepted:
        # إنشاء رمز QR
        qr_code = generate_qr_code(instance)

        # إرسال البريد الإلكتروني
        send_acceptance_email(instance, qr_code)


def regist(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.event = Event.objects.first()
            applicant.save()
            return redirect('success')
    else:
        form = ApplicantForm()

    return render(request, 'regist_event/regist.html', {'form': form})


def success(request):

    return render(request, 'regist_event/success.html')


def generate_qr_code(Accepted):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(
        f"البريد الإلكتروني: {Accepted.event} {Accepted.email}, رقم الهاتف: {Accepted.phone}")
    qr.make(fit=True)

    # إنشاء صورة رمز QR وتحويلها إلى BytesIO
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")

    return img_bytes.getvalue()


def send_acceptance_email(Accepted, qr_code):
    subject = 'تم قبول دعوتك'
    message = 'نحن بانتظارك!'
    From = 'hunterxadxad@example.com'
    To = [Accepted.email]

    # Encode the QR code as base64
    qr_code_base64 = base64.b64encode(qr_code).decode()

    email = EmailMessage(subject, message, From,  To)
    email.attach(f"qrcode_{Accepted.email}.png", qr_code, "image/png")
    email.send()

    email.send()


@api_view(['POST'])
def process_qr_code(request):
    if request.method == 'POST':
        Applicant = request.data.get('Applicant', '')

        if Applicant:
            email = ApplicantForm(Applicant)
            phone_number = ApplicantForm(Applicant)
            event = ApplicantForm(Applicant)

            form = ApplicantForm({
                'email': email,
                'phone_number': phone_number,
                'event': event,
            })

            if form.is_valid():
                form.save()

                # إنشاء سجل جديد في نموذج Attendance وحفظه في قاعدة البيانات
                Attendance.objects.create(
                    name=Applicant,  # افتراضياً، يمكنك استخدام اسم المتقدم
                    email=email,
                    phone_number=phone_number,
                    event=event
                )

                return Response({'message': 'QR code data received and processed'})

    return Response({'message': 'Invalid data'}, status=400)


@user_passes_test(lambda user: user.is_staff or user.is_superuser)
def scan(request):
    return render(request, 'regist_event/scan.html')


def all_events(request):
    events = Event.objects.all()
    form = ApplicantForm()  # تعيين قيمة افتراضية لـ form خارج الشرط

    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    return render(request, 'event/event.html', {'form': form, 'events': events})
