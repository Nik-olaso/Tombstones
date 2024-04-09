from django import forms
from .models import Tombstone, Comment


class AddTombstone(forms.ModelForm):
    class Meta:
        model = Tombstone
        fields = [
            "company_name",
            "logo",
            "birth_year",
            "death_year",
            "alternate_name",
            "people",
            "link",
            "characteristic",
            "description",
            "death_cause",
            "count_employee",
            "revenue",
            "score_company",
        ]
        widgets = {
            "birth_year": forms.NumberInput(attrs={"max": "2024"}),
            "death_year": forms.NumberInput(attrs={"max": "2024"}),
            "count_employee": forms.NumberInput(attrs={"max": "2147483647"}),
            "revenue": forms.NumberInput(attrs={"max": "2147483647"}),
            "score_company": forms.NumberInput(attrs={"max": "2147483647"}),
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
        ]
        widgets = {
            "comment": forms.Textarea(attrs={'maxlength': 500}),
        }
