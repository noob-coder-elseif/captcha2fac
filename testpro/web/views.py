from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q
# Create your views here.
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def pdf_gen(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    lines = [
        "First line",
        "Second LIne",
        "Third Line"
    ]

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='report.pdf')

def checkpdf(request):
    return render(request, 'pdfclick.html')


def product_by_category(request, slug):
    brands = request.GET.get('brand')
    dict = {}

    filtered_products = User.objects.filter(Q(category__slug__contains=slug) | Q(category__parent__slug__contains=slug) | Q(category__parent__parent__slug__contains=slug),parent=None)
    dict["products"] = filtered_products
    
    b_id = filtered_products.values_list('brand', flat=True).distinct()

    dict["brands"] = User.objects.filter(id__in=b_id)
    if brands:
        new_filtered_products = filtered_products.filter(brand__name__in=brands.split(','))
        paginated_filtered_products = Paginator(new_filtered_products, 2)
        page_number = request.GET.get('page')
    else:
        paginated_filtered_products = Paginator(filtered_products, 2)
        page_number = request.GET.get('page')
    product_page_obj = paginated_filtered_products.get_page(page_number)
    dict["product_page_obj"] = product_page_obj
    return render(request, 'category.html', dict)