# acl_admin
Access Control List Dictionary
## install
```
pip install -r requirements.txt
```

### using cui tools
#### csv=>acl
```
$python3 csv_acl.py example.csv
access-list permit tcp 10.0.0.0 0.0.0.255 0 192.168.0.0 0.0.0.255 80
access-list permit tcp 10.0.0.0 0.0.0.255 0 192.168.0.0 0.0.0.255 443
access-list permit tcp 10.0.0.0 0.0.0.255 0 192.168.0.0 0.0.0.255 22
```
#### acl=>csv
```
$python3 acl_csv.py example_acl.txt
0,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,80
0,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,443
0,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,22
```

```
$python3 acl_csv.py example_acl.txt 1
1,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,80
1,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,443
1,tcp,10.0.0.0,0.0.0.255,0,192.168.0.0,0.0.0.255,22
```



## csv format
[[vlan numder or hostname],[0:permit or 1:deny],protocol,src-ip,wild card,src-port,dst-ip,wild card,dst-port]
## csv example
1,0,10.0.0.0,24,0,192.168.0.0,24,80   
1,0,10.0.0.0,24,0,192.168.0.0,24,443  
1,0,10.0.0.0,24,0,192.168.0.0,24,22    
