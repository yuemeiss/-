from django.db import models

# Create your models here.
class ClsTable(models.Model):
    name = models.CharField(max_length=100)

class Qiushipro(models.Model):
    title = models.CharField(max_length=188,null=True)
    content = models.TextField(null=True)
    img_url = models.CharField(max_length=250,null=True)
    localImgPath = models.CharField(max_length=250,null=True)
    funny_num = models.CharField(max_length=20,null=True)
    comment_num = models.CharField(max_length=20,null=True)
    comment_list = models.TextField(null=True)
    clsid = models.ForeignKey('ClsTable')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '糗事百科'
class Juziconpro(models.Model):
    tags =models.CharField(max_length=255,null=True)
    intro = models.CharField(max_length=255,null=True)
    content_list = models.TextField(null=True)
    title = models.CharField(max_length=188, null=True)
    img_url = models.CharField(max_length=250, null=True)
    localImgPath = models.CharField(max_length=250, null=True)
    clsid = models.ForeignKey('ClsTable')

class Juzitagtable(models.Model):

    # 最新
    con_time = models.CharField(max_length=255,null=True)
    # 句子去重id
    uuid = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, null=True)
    intro = models.CharField(max_length=255, null=True)
    content_list = models.TextField(null=True)
    title = models.CharField(max_length=188, null=True)
    img_url = models.CharField(max_length=250, null=True)
    localImgPath = models.CharField(max_length=250, null=True)
    clsid = models.ForeignKey('ClsTable')


