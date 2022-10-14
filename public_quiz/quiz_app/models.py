from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    score = models.PositiveIntegerField()

class Questions(models.Model):
    
    question = models.CharField(max_length = 100)
    option_1 = models.CharField(max_length = 100)
    option_2 = models.CharField(max_length = 100)
    option_3 = models.CharField(max_length = 100)
    option_4 = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100,choices =[
                                                            ('option_1',"option_1"),
                                                            ('option_2',"option_2"),
                                                            ('option_3',"option_3"),
                                                            ('option_4',"option_4")
                                                            ])
