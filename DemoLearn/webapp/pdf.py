# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def html2pdf(template_src, context_dict={}):
#     template=get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type="application/pdf")
#     return None

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os

def html2pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    # Ensure CSS file exists
    css_path = os.path.join(settings.BASE_DIR, "static/profile.css")
    
    if not os.path.exists(css_path):
        print(f"CSS file not found at: {css_path}")  # Debugging output
        css_content = ""
    else:
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()

    result = BytesIO()

    # Generate PDF with CSS
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, default_css=css_content)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    
    return None

def html2pdf2(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    # Ensure CSS file exists
    css_path = os.path.join(settings.BASE_DIR, "static/all_stu_pdf.css")
    
    if not os.path.exists(css_path):
        print(f"CSS file not found at: {css_path}")  # Debugging output
        css_content = ""
    else:
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()

    result = BytesIO()

    # Generate PDF with CSS
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, default_css=css_content)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    
    return None
