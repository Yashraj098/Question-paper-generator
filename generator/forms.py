from django import forms

class QuestionPaperForm(forms.Form):
    total_marks = forms.IntegerField(label='Total Marks')
    easy_percentage = forms.IntegerField(label='Percentage of Easy Questions')
    medium_percentage = forms.IntegerField(label='Percentage of Medium Questions')
    hard_percentage = forms.IntegerField(label='Percentage of Hard Questions')