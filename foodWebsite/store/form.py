from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import pickle
from .models import UserProfileInfo
from django.core.files.storage import default_storage


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
    CA = ((0, '1'), (1, '2'), (2, '3'))
    ca = forms.ChoiceField(choices=CA)
    THAL = ((0, 'Normal'), (1, 'Fixed defect'), (2, 'Reversable defect'))
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

    def predict_data(self, data):
        f = default_storage.open("store/datamodel/finalized_model.sav", "rb")
        loaded_model = pickle.load(f)
        result = loaded_model.predict([data])
        return result

    # def prepareDataCP(self, data):
    #     data_prepare = []
    #     switcher = {
    #         '0': data_prepare.extend([1, 0, 0, 0]),
    #         '1': data_prepare.extend([0, 1, 0, 0]),
    #         '2': data_prepare.extend([0, 0, 1, 0]),
    #         '3': data_prepare.extend([0, 0, 0, 1])
    #     }
    #     return switcher.get(data, [0, 0, 0, 0])
    #
    # def prepareDataTHALandSlope(self, data):
    #     data_prepare = []
    #     switcher = {
    #         '1': data_prepare.extend([1, 0, 0]),
    #         '2': data_prepare.extend([0, 1, 0]),
    #         '3': data_prepare.extend([0, 0, 1])
    #     }
    #     return switcher.get(data, [0, 0, 0])

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(RegisterForm, self).save(commit=True)
        # predict data

        data = [
            self.cleaned_data['age'],
            self.cleaned_data['gender'],
            self.cleaned_data['trestbps'],
            self.cleaned_data['chol'],
            self.cleaned_data['fbs'],
            self.cleaned_data['restecg'],
            self.cleaned_data['thalach'],
            self.cleaned_data['exang'],
            self.cleaned_data['oldpeak'],
            self.cleaned_data['ca']
        ]
        print(data)

        # add cp
        # data = data + [1, 0, 0, 0]
        cp = self.cleaned_data['cp']
        if cp == '0':
            data.extend([1, 0, 0, 0])

        if cp == '1':
            data.extend([0, 1, 0, 0])

        if cp == '2':
            data.extend([0, 0, 1, 0])
        if cp == '3':
            data.extend([0, 0, 0, 1])

        # add thal
        thal = self.cleaned_data['thal']

        if thal == '0':
            data.extend([1, 0, 0, 0])

        if thal == '1':
            data.extend([0, 1, 0, 0])

        if thal == '2':
            data.extend([0, 0, 1, 0])
        if thal == '3':
            data.extend([0, 0, 0, 1])

        # add slope

        slope = self.cleaned_data['slope']
        if slope == 0:
            data.extend([1, 0, 0])
        if slope == 1:
            data.extend([0, 1, 0])
        if slope == 2:
            data.extend([0, 0, 1])

        print(12312)
        print(data)
        print(123)
        # data = [1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        data = [int(x) for x in data]

        target = self.predict_data(data)

        # user_profile = UserProfileInfo(target=target)
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
                                       thal=self.cleaned_data['thal'],
                                       target=target)

        user_profile.save()
        return user, user_profile
