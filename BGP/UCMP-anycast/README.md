```
netlab create ospf+ibgp.yml
sudo containerlab deploy -t clab.yml
netlab config anycast -l '~a[1-4]' -v
netlab config bw-ucmp -l '~[ls][1-4]' -v
```
