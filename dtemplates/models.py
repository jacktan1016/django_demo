from django.db import models

class BookInfoManager(models.Manager):
    def add_book(self,title,date):
        book = BookInfo()
        book.btitle = title
        book.bpub_date = date
        book.save()
        return book

# Create your models here.
class BookInfo(models.Model):

    books = BookInfoManager()

    btitle = models.CharField(verbose_name="名称",max_length=20)
    bpub_date = models.DateField(verbose_name = "出版日期")
    bread = models.IntegerField(verbose_name="阅读量",default=0)
    is_delete = models.BooleanField(verbose_name="逻辑删除",default=False)
    bcomment = models.IntegerField(verbose_name="评论量",default=0)
    image = models.ImageField(upload_to = "abs",null=True,verbose_name='上传图像') # 上传到abs文件夹

    class Meta:
        db_table = "tb_books"
        verbose_name = "图书"  # 在admin站点显示
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.btitle  # print时返回btitle名称


    # 自定义方法列
    def date_time(self):
        return self.bpub_date.strftime('%Y-%m-%d')

    date_time.short_description = '发布日期'
    date_time.admin_order_field = 'bpub_date'  # 排序

class HeroInfo(models.Model):
    # 枚举
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(verbose_name="英雄名",max_length=20)
    hgender = models.SmallIntegerField(choices = GENDER_CHOICES,default=0,verbose_name="性别")
    hcomment = models.CharField(verbose_name="描述信息",max_length=20,null=True)
    # 关联外键
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name="图书")
    is_delete = models.BooleanField(default=False,verbose_name="逻辑删除")

    class Meta:
        db_table = "tb_heros"
        verbose_name = "英雄"
        verbose_name_plural = verbose_name # 显示的复数名称

    def __str__(self):
        return self.hname

    # 关联书本的阅读量
    def bread(self):

        return self.hbook.bread
    bread.short_description = "书的阅读量"





