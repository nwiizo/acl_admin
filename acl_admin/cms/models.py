from django.db import models

# Create your models here.
class ACL(models.Model):
    """Access_Control_List"""
    acl_id = models.IntegerField('acl_id', blank=True, defa)
    acl = models.CharField('アクセスリストコントロール', max_length=225)
    active = models.CharField('有効無効', )

    def __int__(self):
            return self.acl_id
