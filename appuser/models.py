from django.db import models


class User(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    email=models.CharField(max_length=20)

    class Meta:
        db_table = 't_user'

class Zcareer(models.Model):

    city=models.CharField(max_length=22)
    title=models.CharField(max_length=22)
    salary=models.CharField(max_length=22)
    company=models.CharField(max_length=33)
    job=models.TextField()
    uptime=models.CharField(max_length=33)
    exper=models.CharField(max_length=33)
    edu=models.CharField(max_length=33)
    loc=models.CharField(max_length=44)
    brief_company=models.TextField()
    host=models.CharField(max_length=22)
    times=models.CharField(max_length=33)
    status=models.CharField(max_length=10)

    class Meta:
        db_table = 't_zhilian'



