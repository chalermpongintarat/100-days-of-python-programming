from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from generate_pdf.utils import render_to_pdf

class generate_pdf_report(View):
    def get(self, request, pk, *args, **kwargs):
        template = get_template('generate_pdf_report.html')
        contents = "Generate PDF from HTML using XHTML2PDF in Django Project"
        pdf = render_to_pdf("generate_pdf_report.html", {'contents':contents})

        return HttpResponse(pdf, content_type= "application/pdf")