from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from cms.models import ACL


def acl_list(request):
    """ACLの一覧表示"""
#    return HttpResponse('ACL一覧')
    acls = ACL.objects.all().order_by('vlan')
    return render(request,
                  'cms/acl_list.html',
                  {'acls':acls})

def acl_edit(request,vlan=None):
    """ACLの編集"""
    return HttpResponse('ACLの編集')

def acl_del(request,vlan):
    """ACLの削除"""
    return HttpResponse('ACLの削除')
