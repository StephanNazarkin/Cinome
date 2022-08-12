from django.db import models

class Test(models.Model):
   title = models.CharField(max_length=100)

   def _str_(self):
     return self.title
