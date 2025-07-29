from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Pune', 'Pune'),
		('Mumbai', 'Mumbai'),
		('Patna', 'Patna'),
	)

	DISCRICT_CHOICES = (
		('Akurdi', 'Akurdi'), 
		('Kalyan', 'Kalyan'),
		('Pimpri', 'Pimpri'),
	)

	PAYMENT_METHOD_CHOICES = (
		('GPay', 'Gpay'),
		('Paytm','Paytm')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
