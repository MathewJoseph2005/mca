from django.db import models
from django.contrib.auth.models import User
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    application_number = models.CharField(max_length=20, unique=True)
    dob = models.DateField()  # Date of Birth
    phone_number = models.CharField(max_length=15)  # Student's phone number
    parent_phone = models.CharField(max_length=15)  # Parent's phone number
    address = models.TextField()
    qualification = models.CharField(max_length=50)  # Current qualification
    college = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    email = models.EmailField()
    category = models.CharField(max_length=10, choices=[('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')])
    seat_type = models.CharField(max_length=10, choices=[('NRI', 'NRI'), ('Non-IBS', 'Non-IBS')])

    def __str__(self):
        return self.name

class InterviewScore(models.Model):
    application_number = models.CharField(max_length=20, null=True, blank=True)
    interview_mark = models.DecimalField(max_digits=5, decimal_places=2)
    lbs_rank = models.IntegerField()
    cgpa_degree = models.DecimalField(max_digits=4, decimal_places=2)
    document_submission = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('not-submitted', 'Not Submitted')])
    general_knowledge = models.IntegerField()
    course_knowledge = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"Interview Score for {self.application_number}"


    def __str__(self):
        return f"Interview Score for {self.student.name}"
class StudentDocument(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="documents")
    sslc = models.FileField(upload_to="documents/")
    entrance_admit_card = models.FileField(upload_to="documents/")
    payment = models.FileField(upload_to="documents/")
    allotment_menu = models.FileField(upload_to="documents/")
    hse = models.FileField(upload_to="documents/")
    lbs_admit_card = models.FileField(upload_to="documents/")
    degree = models.FileField(upload_to="documents/")
    school_leaving = models.FileField(upload_to="documents/")
    tc = models.FileField(upload_to="documents/")

    def __str__(self):
        return f"Documents for {self.student.name}"
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('faculty', 'Faculty'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='faculty')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"