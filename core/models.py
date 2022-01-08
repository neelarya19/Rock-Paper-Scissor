from django.db import models

MOVE_CHOICE=(
    ('R','Rock'),
    ('P','Paper'),
    ('S','Scissor')
)

class Player(models.Model):
    Name=models.CharField(max_length=60)


class Rounds(models.Model):
    Name=models.ForeignKey(Player,on_delete=models.CASCADE)
    Move=models.CharField(max_length=10,choices=MOVE_CHOICE)
    Score=models.IntegerField(default=0)



