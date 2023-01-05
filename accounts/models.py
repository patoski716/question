from django.db import models

# Create your models here.



STATUS = (
    ("First","First"),
    ("Second","Second")
)

class Question(models.Model):
    photo= models.ImageField(default='')
    course_title = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    semester = models.CharField(max_length=255,choices=STATUS, default="First")
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.course_title