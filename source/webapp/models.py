from django.db import models
from webapp.validators import MinLengthValidator


class Status(models.Model):
    name = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tracker(BaseModel):
    title = models.CharField(max_length=3000, null=False, blank=False, validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=3000, null=True, blank=True, validators=(MinLengthValidator(5),))
    status = models.ForeignKey('webapp.Status', null=True, related_name="trackers", blank=True,
                               on_delete=models.PROTECT)
    type = models.ManyToManyField('webapp.Type', null=True, related_name="trackers", blank=True)
    date = models.DateField(null=True, blank=True)
    project = models.ForeignKey('webapp.Project', null=True, related_name="project_trackers", default=1,
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'trackers'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Project(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True)
    date = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
