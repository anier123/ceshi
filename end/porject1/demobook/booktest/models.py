from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1998-11-16")
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default="male")
    conten = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="heros")

    def __str__(self):
        return self.name


class UserManager(models.Model):
    """
    自定义一个模型管理员 该模型不在有objects 对象
    """

    def deleteByTelePhone(self, tel):
        user = self.get(telephone=tel)
        user.delete()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")

    def __str__(self):
        return self.telephone

    class Meta:
        # 表名
        db_table = "用户类"
        ordering = ["telephone"]
        verbose_name = "用户管理类"
        verbose_name_plural = "用户模型类"


class Account(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="用户名密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(default="1326729135@qq.com")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签名")
    articles = models.ManyToManyField(Article)

# 一对多   一方Book  实例b  多方Hero  实例h    关系字段定义在多方
# 一找多    b.hero_set.all()    如果定义过related_name='heros' 则使用  b.heros.all()
# 多找一   h.book

# 一对一   一方Account  实例a   一方Concact 实例c   关系字段定义在任意一方
# a 找 c  a.concact
# c 找 a  c.account

# 多对多  多方Article  实例a    多方Tag 实例t   关系字段可以定义在任意一方
# 添加关系   t.articles.add(a)    移除关系  t.articles.remove(a)
# a 找 所有的 t   a.tag_set.all()   如果定义过related_name='tags' 则使用 a.tags.all()
# t 找 所有的 a   t.articles.all(
