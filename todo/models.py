from django.db import models

# Create your models here.

class ToDo(models.Model):
    nom = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.nom 
    
