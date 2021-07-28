from django.db import models

# Create your models here.
CHOICE=(('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    tilte=models.CharField(max_length=100)
    memo=models.TextField()
    priority=models.CharField(
        max_length=100,
        #選択肢が当てられてそこから選ぶ感じ→ラジオボタン
        choices=CHOICE
        )
    duedate=models.DateField()

    def __str__(self):
        return self.tilte
    