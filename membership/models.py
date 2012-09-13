from django.db import models

# Create your models here.
class Group(models.Model):
    Name = models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.Title    

    def save(self, *args, **kwargs):
        return super(Entry, self).save(*args, **kwargs)