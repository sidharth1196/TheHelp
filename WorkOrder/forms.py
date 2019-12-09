from django import forms
from WorkOrder.models import Quote

class QuoteForm(forms.ModelForm):
    class Meta():
        model = Quote
        fields = ('title', 'work_desc', 'charge', 'start_date', 'comments')