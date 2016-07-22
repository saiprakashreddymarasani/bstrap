from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_employees= Employee.objects.all()
    context={"all_employees": all_employees}
    return render(request , "index.html", context)


def detail(request,employee_id):
    all_employees = Employee.objects.all()
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("NO Employee")
    return render(request , "detail.html", {"employee": employee})
