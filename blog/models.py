from django.db import models

# Create your models here.

class Blog(models. Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    entry = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title
        
    
    def summary(self):
        return self.entry[:9]
    
    def pub_improved(self):
        return self.pub_date.strftime('%B %d, %Y')
        