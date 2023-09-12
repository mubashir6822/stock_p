from django import forms
from .models import Stock,StockStatus,News,Holding

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'name', 'price']
class StockStatusForm(forms.ModelForm):
    class Meta:
        model = StockStatus
        fields = ['status']