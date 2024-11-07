from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from .models import Student, UserProfile
from .forms import StudentForm, InterviewScoreForm, StudentDocumentForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .forms import StudentForm
from django.contrib.auth import logout
from django.shortcuts import redirect
# Home page view
def home(request):
    return render(request, 'portal/home.html')

# Single Dashboard view for both admin and faculty
@login_required
def dashboard(request):
    students = Student.objects.all()
    # Check if the user is admin to show additional admin features
    is_admin = request.user.is_superuser
    return render(request, 'portal/dashboard.html', {'students': students, 'is_admin': is_admin})

# Add student page (Only accessible by admin)
@login_required
def add_student(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can add students.")

    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('portal:dashboard')  # Redirect to dashboard after saving
    else:
        student_form = StudentForm()

    return render(request, 'portal/add_student.html', {'student_form': student_form})


# View student details
@login_required
def student_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'portal/student_details.html', {'student': student})

# Document submission page (allow students to submit documents)
@login_required
def submit_documents(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.student = student
            document.save()
            return redirect('portal:dashboard')
    else:
        form = StudentDocumentForm()

    return render(request, 'portal/submit_documents.html', {'form': form, 'student': student})

# Custom login view (for both admin and faculty)
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portal:dashboard')  # After successful login, redirect to dashboard
            else:
                form.add_error(None, 'Invalid username or password.')  # Provide feedback if authentication fails
    else:
        form = AuthenticationForm()

    return render(request, 'portal/login.html', {'form': form})
# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Student

def toggle_approval(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.approved = not student.approved  # Toggle the approval status
    student.save()
    return redirect('portal:student_details', student_id=student.id)
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Student

def generate_report(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    # Generate the report logic here (e.g., create a PDF or return a template)
    return render(request, 'portal/report.html', {'student': student})
def custom_logout(request):
    logout(request)
    return redirect('portal:home') 