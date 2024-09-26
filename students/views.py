from django.shortcuts import render
from .models import Student
import subprocess

def home(request):
    student = Student.objects.first()
    return render(request, 'home.html', {'student': student})

def lecture(request):
    student = Student.objects.first()
    return render(request, 'lecture.html', {'student': student})

def tasks(request):
    student = Student.objects.first()
    result = None
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            # Внимание: выполнение пользовательского кода через subprocess небезопасно.
            # Это только для примера.
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True, text=True, check=True
            ).stdout
        except subprocess.CalledProcessError as e:
            result = e.stderr

    return render(request, 'tasks.html', {'student': student, 'result': result})
