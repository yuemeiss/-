from django.db import models

# Create your models here.
class ClsTable(models.Model):
    name = models.CharField(max_length=100)

class Qiushipro(models.Model):
    title = models.CharField(max_length=188)
    content = models.TextField()
    img_url = models.CharField(max_length=250)
    localImgPath = models.CharField(max_length=250)
    funny_num = models.CharField(max_length=20)
    comment_num = models.CharField(max_length=20)
    comment_list = models.TextField()
    clsid = models.ForeignKey('ClsTable')
    # 操作者
    operator = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '糗事百科'