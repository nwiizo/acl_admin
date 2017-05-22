# acl_admin
Access Control List Dictionary
## install
```
pip install -r requirements.txt
```

## csv format
[[vlan numder or hostname],[0:permit or 1:deny],protocol,src-ip,wild card,src-port,dst-ip,wild card,dst-port]
## csv example
1,0,10.0.0.0,24,0,192.168.0.0,24,80   
1,0,10.0.0.0,24,0,192.168.0.0,24,443  
1,0,10.0.0.0,24,0,192.168.0.0,24,22    
