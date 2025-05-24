from django.db import models
from django.utils import timezone
# Create your models here.
class Chaivariety(models.Model):
   CHAI_TYPE_CHOICE = [
      ('ML','MASALA'),
      ('GR','GINGER'),
      ('KL','KIWI'),
      ('PL','PLAIN'),
      ('EL','ELAICHI')
   ]
   
   name = models.CharField(max_length=100)
   image = models.ImageField(upload_to='chais/')
   date_added = models.DateTimeField(default=timezone.now)
   type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
   description = models.TextField(default='')

   def __str__(self): # To see the name of object in admin panel
      return self.name

