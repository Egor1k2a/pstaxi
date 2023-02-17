from django import forms
from motorpool.models import Brand


class SendEmailForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=30, required=False)
    email = forms.EmailField(label='Ваш email', required=False)
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea)
    checkbox1 = forms.BooleanField(label='Чекбокс 1', required=False)
    checkbox2 = forms.BooleanField(label='Чекбокс 2', required=False)
    amount = forms.IntegerField(label='Сумма', required=False)
    variant = forms.ChoiceField(label='Один вариант', choices=(
        (1, 'Вариант 1'),
        (2, 'Вариант 2'),
        (3, 'Вариант 3'),
        (4, 'Вариант 4'),
    ))
    variants = forms.MultipleChoiceField(label='Несколько вариантов', choices=(
        (1, 'Множественный выбор 1'),
        (2, 'Множественный выбор 2'),
        (3, 'Множественный выбор 3'),
        (4, 'Множественный выбор 4'),
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите имя'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['checkbox1'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['checkbox2'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['variant'].widget.attrs.update({'class': 'form-select'})
        self.fields['variants'].widget.attrs.update({'class': 'form-select', 'multiple': True})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        variants = cleaned_data.get('variants')

        check_successful = True

        msg = 'Это поле должно быть обязательно заполнено'
        if not name:
            self.add_error('name', msg)
            check_successful = False

        if not email:
            self.add_error('email', msg)
            check_successful = False

        if not check_successful or not variants:
            self.add_error('variants', 'Поля name и email не заполнены')
            raise forms.ValidationError('Форма содержит ошибки')

        return cleaned_data

    def clean_variants(self):
        variants = self.cleaned_data['variants']
        if len(variants) < 2:
            raise forms.ValidationError('Нужно выбрать минимум 2 варианта')
        return variants


class BrandCreationForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('title', 'logo')

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if Brand.objects.filter(title=title).exists():
            raise forms.ValidationError(f'Бренд с названием {title} уже существует')

        return cleaned_data


class BrandUpdateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('title', 'logo')
