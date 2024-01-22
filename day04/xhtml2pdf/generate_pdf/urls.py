from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from generate_pdf import views
from generate_pdf.views import generate_pdf_report

app_name = 'generate_pdf'

urlpatterns = [
    path('generate_pdf_report', generate_pdf_report.as_view(), name='generate_pdf_report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()