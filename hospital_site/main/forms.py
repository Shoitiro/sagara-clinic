from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=100,
        required=True,
        error_messages={'required': 'お名前は必須です'}
    )

    email = forms.EmailField(
        label='メールアドレス',
        required=True,
        error_messages={'required': 'メールアドレスは必須です'}
    )

    date = forms.DateField(
    label='予約希望日',
    widget=forms.DateInput(attrs={'type': 'date'}),
    required=True,
    error_messages={'required': '予約希望日を選択してください'}
    )

    start_time = forms.TimeField(
    label='開始時間',
    widget=forms.TimeInput(attrs={'type': 'time'}),
    required=True,
    error_messages={'required': '開始時間を入力してください'}
    )

    end_time = forms.TimeField(
    label='終了時間',
    widget=forms.TimeInput(attrs={'type': 'time'}),
    required=True,
    error_messages={'required': '終了時間を入力してください'}
    )

    message = forms.CharField(
        label='ご要望・症状など',
        widget=forms.Textarea,
        required=False  # ← これは任意のままでOK
    )

class QuestionnaireForm(forms.Form):
    age = forms.IntegerField(label='年齢', required=True)
    symptoms = forms.CharField(label='症状', widget=forms.Textarea, required=True)
    allergy = forms.CharField(label='アレルギー', required=False)
    medication = forms.CharField(label='服用中の薬', required=False)
    first_visit = forms.BooleanField(label='初診ですか？', required=False)
