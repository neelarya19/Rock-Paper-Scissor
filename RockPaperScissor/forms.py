from django import forms
from django.db.models import fields

from core.models import Player,Rounds

MOVE_CHOICE=(
    ('R','Rock'),
    ('P','Paper'),
    ('S','Scissor')
)

class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.pop("autofocus",None)

    class Meta:
        model=Player
        fields=['Name']

class MoveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MoveForm, self).__init__(*args, **kwargs)
        self.fields['Move'].widget.attrs.pop("autofocus",None)

    class Meta:
        model=Rounds
        fields=['Move']
