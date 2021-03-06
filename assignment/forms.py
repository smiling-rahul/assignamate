from django import forms

from .models import Assignment,Questions,Booklet,Workbook,Workbook_page,Interests

from django.contrib.auth.models import User

class AssignmentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a question...'
        }
    ))
    discription = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write description...'
        }
    ),required=False)
    CATEGORY_CHOICES = (
        ('jee_main', 'JEE-Main'),
        ('jee-advance', 'JEE-ADVANCE'),
        ('gate-cs', 'GATE-computer Science and IT'),
        ('gate-me', 'GATE-Mechanical Engineering'),
        ('gate-ee', 'GATE-Electrical Engineering'),
        ('gate-ece', 'GATE-electronics Engineering'),
        ('gate-ce', 'GATE-Civil Engineering'),
        ('gate-mt', 'GATE-Metallurgical and Materials Engineering'),
        ('ssc', 'SSC'),
        ('other','OTHERS')
    )
    category = forms.ChoiceField(widget=forms.Select,choices=CATEGORY_CHOICES)


    class Meta:
        model=Assignment
        fields = ('title', 'discription', 'category','image')


class QuestionForm(forms.ModelForm):
    question=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control' ,
            'placeholder': 'Write a question...'
        }
    ))

    option_a = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Write your answer...'
       }
    ))


    option_b = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))

    option_c = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))

    option_d = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))
    CHOICES = (('a', 'Option a'), ('b', 'Option b'),('c', 'Option c'), ('d', 'Option d'),)
    answer = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)


    positive_marks=forms.CharField(widget=forms.TextInput(
        attrs = {
        'class': 'form-control',
        'placeholder': 'Marks...'
        }
    )
    )
    negative_marks = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Marks...'
        }
    )
    )

    hint = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your hint...'
        }
    ),required=False)

    tags = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your tags...'
        }
    ),required=False)

    image=forms.ImageField(required=False)

    class Meta:
        model = Questions
        fields = ('question','image','option_a','option_b',
                  'option_c','option_d','answer','positive_marks',
                  'negative_marks','hint','tags',)





class DocumentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the title of the book...'
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the subject...'
        }
    ))
    author = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the author...'
        }
    ))
    discription = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the book...'
        }
    ))
    link = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link (google-drive,Dropbox etc)...'
        }
    ))
    class Meta:
        model = Booklet
        fields = ('name', 'subject','author','discription', 'link','image' )


class Workbook_page_Form(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your title...'
        }
    ))
    class Meta:
        model=Workbook_page
        fields=('title','text','image')

class Workbook_Form(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your title...'
        }
    ))

    quotes = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your quotes...'
        }
    ),required=False)

    discription = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your text...'
        }
    ),required=False)

    class Meta:
        model=Workbook
        fields=('name','quotes','discription','background_image')

class Interest_form(forms.ModelForm):
    class Meta:
        model =Interests
        fields=('intrest',)






