from django.db import models



CLASSES = [
    ("KG1", "Kindergaten 1"),
    ("KG2", "Kindergaten 2"),
    ("N1", "Nursery 1"),
    ("N2", "Nursery 2"),
    ("P1", "Primary 1"),
    ("P2", "Primary 2"),
    ("P3", "Primary 3"),
    ("P4", "Primary 4"),
    ("P5", "Primary 5"),
]




class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(
        max_length=2,
        choices=[
            ("M", "Male"),
            ("F", "Female")
        ]
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    class Meta:
        verbose_name_plural = "All students"
        verbose_name = "All students"



class Class(models.Model):
    name = models.CharField(choices=CLASSES, max_length=5)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey("teacher.ClassTeacher", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Classes"
