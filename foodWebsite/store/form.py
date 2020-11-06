from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfileInfo


class RegisterForm(UserCreationForm):
    age = forms.IntegerField()
    GENDER = ((1, 'Male'), (2, 'Female'),)
    gender = forms.ChoiceField(choices=GENDER)
    CP = ((0, '0'), (1, '1'), (2, '2'), (3, '3'))
    cp = forms.ChoiceField(choices=CP)

    trestbps = forms.IntegerField()

    chol = forms.IntegerField()
    FBS = ((1, '>120 mg/dl'), (0, '<=120 mg/dl'))
    fbs = forms.ChoiceField(choices=FBS)
    RES = ((1, '1'), (2, '2'), (3, '3'))
    restecg = forms.ChoiceField(choices=RES)

    thalach = forms.IntegerField()

    EXANG = ((0, 'No'), (2, 'Yes'))
    exang = forms.ChoiceField(choices=EXANG)

    oldpeak = forms.FloatField()

    slope = forms.IntegerField()
    CA = ((1, '1'), (2, '2'), (3, '3'))
    ca = forms.ChoiceField(choices=CA)
    THAL = ((3, 'Normal'), (2, 'Fixed defect'), (3, 'Reversable defect'))
    thal = forms.ChoiceField(choices=THAL)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "age", "gender", "cp", "trestbps", "chol", "fbs",
                  "restecg", "thalach", "exang", "exang",
                  "slope", "ca", "thal"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(RegisterForm, self).save(commit=True)
        user_profile = UserProfileInfo(user=user,
                                       gender=self.cleaned_data['gender'],
                                       age=self.cleaned_data['age'],
                                       cp=self.cleaned_data['cp'],
                                       trestbps=self.cleaned_data['trestbps'],
                                       chol=self.cleaned_data['chol'],
                                       fbs=self.cleaned_data['fbs'],
                                       restecg=self.cleaned_data['restecg'],
                                       thalach=self.cleaned_data['thalach'],
                                       exang=self.cleaned_data['exang'],
                                       oldpeak=self.cleaned_data['oldpeak'],
                                       slope=self.cleaned_data['slope'],
                                       ca=self.cleaned_data['ca'],
                                       thal=self.cleaned_data['thal'])
        user_profile.save()
        return user, user_profile
