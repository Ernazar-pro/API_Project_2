from django.db import models

class StudyCenter(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Учебного центра'
        verbose_name_plural = 'Учебные центры'

class Teacher(models.Model):
    fullname = models.CharField(max_length=256)
    about = models.TextField()
    experience = models.PositiveIntegerField()
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учители'

class Student(models.Model):
    fullname = models.CharField(max_length=256)
    about = models.TextField()
    phone_number = models.CharField(max_length=256)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Учебного центра'
        verbose_name_plural = 'Учебные центры'