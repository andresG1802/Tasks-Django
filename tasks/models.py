from django.db import models

#Django ya tiene su propio ORM
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    #Para ver el titulo en /admin el titulo de cada tarea
    def __str__(self):
        return self.title