from django.db import models

# Create your models here.
class ACL(models.Model):
    """Access_Control_List"""
    vlan = models.IntegerField('vlan番号', blank=True, default=0)
    protocol = models.CharField('プロトコル', max_length=15)
    src_ip = models.CharField('送信元IP', max_length=64)
    src_wc = models.CharField('送信元ワイルドカード', max_length=64)
    src_port = models.CharField('送信元ポート番号', max_length=64)    
    dst_ip = models.CharField('宛先IP', max_length=64)
    dst_wc = models.CharField('宛先ワイルドカード', max_length=64)
    dst_port = models.CharField('宛先ポート番号', max_length=64)

    def __str__(self):
            return self.vlan
