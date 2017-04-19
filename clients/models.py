from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Speed_packet(models.Model):
    ds = models.IntegerField(null=True)
    us = models.IntegerField(null=True)
    
class Client_service(models.Model):
    service = models.IntegerField(null=True)
    '''
    def __str__(self):
        return  self.service
    class Meta:
        ordering = ['service']
'''

class Clients_det(models.Model):
    cl_add_ul = models.CharField(max_length = 100)
    cl_add_nrd = models.CharField(max_length = 20)
    cl_add_nrm = models.CharField(max_length = 20)
    cl_ip = models.CharField(max_length = 100, null=True)
    cl_mac = models.CharField(max_length = 100, null=True)
    srv = models.ForeignKey(Client_service)
    speed = models.ForeignKey(Speed_packet)
    last_log_seen = models.CharField(max_length = 100, blank=True, null=True)
