from django import forms
from .models import Student, InterviewScore, StudentDocument

# Form for Student Personal Details
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'application_number', 'dob', 'phone_number', 
            'parent_phone', 'address', 'qualification', 'college', 
            'cgpa', 'email', 'category', 'seat_type'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),  # Date input for DOB
            'category': forms.Select(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')]),
            'seat_type': forms.Select(choices=[('NRI', 'NRI'), ('Non-IBS', 'Non-IBS')]),
        }

# Form for Interview Score Details
class InterviewScoreForm(forms.ModelForm):
    class Meta:
        model = InterviewScore
        fields = [
            'application_number', 'interview_mark', 'lbs_rank', 
            'cgpa_degree', 'document_submission', 'general_knowledge', 
            'course_knowledge', 'status'
        ]
        widgets = {
            'document_submission': forms.Select(choices=[('submitted', 'Submitted'), ('not-submitted', 'Not Submitted')]),
            'status': forms.Select(choices=[('approved', 'Approved'), ('rejected', 'Rejected')]),
        }
class StudentDocumentForm(forms.ModelForm):
    class Meta:
        model = StudentDocument
        fields = ['sslc', 'entrance_admit_card', 'payment', 'allotment_menu', 'hse', 'lbs_admit_card', 'degree', 'school_leaving', 'tc']