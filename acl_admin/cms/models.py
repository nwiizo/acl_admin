from django.db import models

# Create your models here.
class ACL(models.Model):
    """Access_Control_List"""
    acl_id = models.IntegerField('acl_id', blank=True)
    vlan = models.IntegerFoeld('vlan',blank=True)
    acl = models.CharField('アクセスリストコントロール', max_length=225)
    active = models.IntegerFoeld('有効無効', blank=True)

    def __int__(self):
            return self.acl_id
        
    def __int__(self):
            return self.vlan
    
    def __int__(self):
            return self.active
