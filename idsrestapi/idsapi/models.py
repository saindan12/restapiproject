from django.db import models

class Network(models.Model):
    timestamp = models.DateTimeField()
    source_ip = models.CharField(max_length=15)
    destination_ip = models.CharField(max_length=15)
    protocol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.source_ip
    
    