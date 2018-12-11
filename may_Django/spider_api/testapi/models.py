from django.db import models

# Create your models here.
class ClsTable(models.Model):
    name = models.CharField(max_length=100)

class Qiushipro(models.Model):
    # class Publisher(models.Model):
    #     name = models.CharField(max_length=32, verbose_name='名称', unique=True)
    #
    # address = models.CharField(max_length=128, verbose_name='地址')
    #
    # def __str__(self):
    #     return self.name
    #
    # class Meta:
    #     verbose_name = '出版社'
    #
    # verbose_name_plural = verbose_name
    title = models.CharField(max_length=188)
    content = models.TextField()
    img_url = models.CharField(max_length=250)
    localImg = models.CharField(max_length=250)
    funny_num = models.CharField(max_length=20)
    comment_num = models.CharField(max_length=20)
    comment_list = models.TextField()
    clsid = models.ForeignKey('ClsTable')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '糗事百科'

