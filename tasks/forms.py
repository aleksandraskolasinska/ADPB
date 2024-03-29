from django import forms
from .models import Project, ProjectStatus, ProjectPriority

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_description', 'projectPriority', 'projectStatus']
        