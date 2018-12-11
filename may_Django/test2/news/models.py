from django.db import models

# Create your models here.
class NewsManager(models.Manager):
    def add_column(self,ntitle1=None,ncontent1=None):
        news = self.model()
        news.ntitle = ntitle1
        news.ncontent = ncontent1
        # news.ntype.add(obj)   添加关系行不通
        news.save()
        return news


class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)
#多对多关系
class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)
    ncontent = models.TextField()
    npub_date = models.DateTimeField(auto_now_add=True)
    ntype = models.ManyToManyField('TypeInfo')
    aa = NewsManager()

# b = TypeInfo.objects.filter(newsinfo__ntitle__contains='路人')   可以找到
# b = NewsInfo.objects.filter(ntype__tname__contains='社')  写ntype
# b.ntype  b.ntype_set  找不到  这里返回的是一个多表关联类 相当于 objects 封装了和很多方法 如add() get()
# aa=b.ntype.get() 这样会找到
# b = NewsInfo.objects.get(id=1)
# c = TypeInfo.objects.get(id=2)
# b.ntype.add(c)  使用多表关联字段   在关联表中添加一个新的关联
# b.ntype.remove(c)  删除





# 网上 多关联
# class Goods(models.Model):
#     gname = models.CharField(max_length=20)
#     gprice = models.DecimalField(max_digits=5,decimal_places=2)
#     gcategory = models.ForeignKey('Category',null=True,on_delete=models.SET_NULL)
# class Category(models.Model):
#     cname = models.CharField(max_length=20)
#
# class Store(models.Model):
#     sname = models.CharField(max_length=30)
#     sdetail = models.TextField(blank=True,null=True)
#     scategory = models.ManyToManyField('Category')
#自定义管理员
class Mymanager(models.Manager):
    #定义自己的方法  获得所有省 和直辖市
    def get_all_sheng(self):
        return super().filter(aparent__isnull=True)



#自关联
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)
    aparent = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL,default='110')  #on_delete 主表删除 从表为空
    area = Mymanager()
