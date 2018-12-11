from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo')
class Practice(models.Model):
    pId = models.IntegerField(primary_key=True)
    pName = models.CharField(max_length=20)
    pAge = models.IntegerField()
    pGender = models.BooleanField(default=False)
    pAddress = models.CharField(max_length=50)
    pPhone = models.CharField(max_length=11,null=True)
    pSalary = models.DecimalField(max_digits=8,decimal_places=2)
    pSection = models.CharField(max_length=20)



'''
INSERT INTO books_practive
VALUES  (10001,'张朝阳',36,1,'北京朝阳区','18018640012',10000,'网络部'),
(10003,'李婷',20,0,'北京房山区','18008640012',9000,'网络部'),
(10005,'钱有才',25,1,'北京海淀区','18008640012',11000,'移动事业部'),
(10006,'赵丽',23,0,'北京朝阳区','18008640012',20000,'公关部'),
(10007,'张亮',30,1,'北京西城区','18008640012',5000,'保卫部'),
(10002,'张阳',28,1,'北京朝阳区','null',12000,'网络部'),
(10004,'李娜',30,0,'北京通州区','null',7000,'人事部');
'''