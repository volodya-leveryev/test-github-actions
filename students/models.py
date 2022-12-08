from django.db import models


class Student(models.Model):
    last_name = models.CharField(verbose_name="фамилия", max_length=50)
    first_name = models.CharField(verbose_name="имя", max_length=50)
    second_name = models.CharField(verbose_name="отчество", max_length=50, blank=True, null=True)
    number = models.CharField(verbose_name="номер зачетки", max_length=10)
    birthday = models.DateField(verbose_name="дата рождения", blank=True, null=True)

    def __str__(self) -> str:
        result = f"{self.last_name} {self.first_name[0]}."
        if self.second_name:
            result += f"{self.second_name[0]}."
        return result

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
