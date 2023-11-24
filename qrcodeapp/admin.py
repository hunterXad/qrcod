
from django.contrib import admin
from .models import Event, Applicant, Accepted, Attendance

admin.site.register(Event)
admin.site.register(Accepted)
admin.site.register(Attendance)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'email', 'age', 'phone_number', 'status')
    list_filter = ('event')  # يجب ترك هذا السطر كما هو إذا كنت تستخدم "event"
    search_fields = ('name', 'email')
    list_per_page = 20

    # تقييد الوصول إلى صفحة المتقدمين للمستخدمين العاديين
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Applicant)
