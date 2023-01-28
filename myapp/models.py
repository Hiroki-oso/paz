from accounts.models import User
from django.db import models

from accounts.models import User
from django.db import models

class Person(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='お名前', max_length=50)
    height = models.FloatField(verbose_name='身長', blank=False, default=0)
    weight = models.FloatField(verbose_name='体重', blank=True, null=True, default=0)
    bmi = models.FloatField(verbose_name='BMI', blank=True, null=True, default=0)
    appr_w = models.FloatField(verbose_name='適正体重', blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='日付')
    updated_at = models.DateTimeField(auto_now=True)
    memo = models.TextField(verbose_name='メモ', blank=True, null=True, max_length=1000)
    
    def save(self, *args, **kwargs):
        self.bmi = round(self.weight / ((self.height/100)**2),1) 
        self.appr_w = round((((self.height/100)**2)*22),1)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'person'
        
    def __str__(self):
        return self.username

