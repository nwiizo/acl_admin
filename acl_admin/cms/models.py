from django.db import models

# Create your models here.
class ACL(models.Model):
    """Access_Control_List"""
    acl_id = models.IntegerField('acl_id', blank=True)
    vlan = models.IntegerFoeld('vlan',blank=True)
    acl = models.CharField('ACL', max_length=225)
    active = models.IntegerFoeld('active', blank=True,default=0)

    def __int__(self):
            return self.acl_id
        
    def __int__(self):
            return self.vlan
    
    def __int__(self):
            return self.active
