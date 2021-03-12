from django.db import models

class Hereglegch(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=30)

class Baraa(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    too=models.IntegerField()
    image=models.CharField(max_length=300)

class Tohirgoo(models.Model):
    word=models.CharField(max_length=300)

class Tses(models.Model):
    word=models.CharField(max_length=300)
    nuugdsan=models.IntegerField()
    daraalal=models.IntegerField()
