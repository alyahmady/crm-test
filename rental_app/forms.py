from django import forms

from rental_app.models import Rental


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ["user", "car", "started_at", "expire_at", "is_returned"]
