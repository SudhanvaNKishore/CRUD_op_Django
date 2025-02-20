from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q, Max
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def index(request):
    query = ""
    students = Student.objects.all()

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            # Get the next available ID
            next_id = Student.objects.aggregate(max_id=Max('id'))['max_id'] + 1 if Student.objects.exists() else 1
            Student.objects.create(id=next_id, name=name, email=email)
            messages.success(request, "New student added successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.filter(id=id).delete()
            messages.success(request, "Student deleted successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.filter(id=id).update(name=name, email=email)
            messages.success(request, "Student updated successfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))

    context = {"students": students, "query": query}
    return render(request, "index.html", context=context)


def generate_pdf_view(request):
    students = Student.objects.all()
    template_path = 'index.html'
    context = {'student': students}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


def download_pdf(request):
    students = Student.objects.all()
    template_path = 'pdf_template.html'
        
    context = {'students': students}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_details.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response