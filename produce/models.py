from django.db import models


# Create your models here.
class TypeModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='类型名字')
    image = models.ImageField(upload_to='media/first_chart/', verbose_name='类型封面图')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name


class TypeContent(models.Model):
    name = models.CharField(max_length=100, verbose_name='文章标题')
    image = models.ImageField(upload_to='media/content_chart/', verbose_name='文章配图')
    path = models.CharField(max_length=1000, verbose_name='文章对应的链接')
    type = models.ForeignKey(TypeModel, related_name='contents', verbose_name='关联的类型')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
