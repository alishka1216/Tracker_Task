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
    description = models.TextField(max_length=3000, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', null=True, related_name="trackers", blank=True, on_delete=models.PROTECT)
    type = models.ManyToManyField('webapp.Type',  null=True, related_name="trackers", blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'trackers'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



# class comment(BaseModel):
#     tracker = models.ForeignKey('webapp.Tracker', on_delete=models.CASCADE,
#                                 related_name='comments',
#                                 verbose_name='Статус')
#     comment = models.CharField(max_length=200, verbose_name='Комментарий', null=False, blank=False)
#     title = models.CharField(max_length=150, null=False, blank=False)
#
#     class Meta:
#         db_table = 'comments'
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
