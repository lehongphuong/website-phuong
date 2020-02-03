from django.db import models
import datetime

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/

STATUS_ACTION = [
    (0, 'Đang Chạy'),
    (1, 'Đã Dừng')
] 
 
class Customer(models.Model): 
    id = models.AutoField
    name_phuong = models.CharField('Tên Phương', max_length=50)
    url_post = models.CharField('Đường dẫn Post', max_length=50)
    number_post = models.IntegerField('Số lần Post', default=0)
    action = models.IntegerField('Hành Động', default=0) 