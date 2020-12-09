#!/bin/bash
domain_prefix=$(basename $(pwd))
pvlan_switch=PVLAN
isolated='c2 c3'
for node in $isolated
do
  domain=${domain_prefix}_${node}
  device=$(virsh domiflist $domain|grep ${pvlan_switch}|awk '{ print $1 }')
  if [ -n "$device" ]; then
    echo "VM $domain is attached to ${pvlan_switch} with $device"
    sudo bridge link set dev $device isolated on
    echo "... $device isolated"
  else
    echo "VM $domain is NOT attached to ${pvlan_switch}"
  fi
done
