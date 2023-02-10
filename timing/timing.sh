#!/bin/bash
#
# Time how long it takes to spin up a virtual machine and do initial configuration
#
set -e
if [ -z "$1" ]; then
  echo "Specify device type"
  exit 1
fi
for dut in $@; do
  echo "Device: $dut"
  netlab create -d $dut >/dev/null 2>/dev/null
  echo -n "Starting the lab: "
  /usr/bin/time -f "%E" bash -c 'netlab up --snapshot --no-config >/dev/null 2>/dev/null || echo "netlab up failed"'
  echo -n "Device configuration: "
  /usr/bin/time -f "%E" bash -c 'netlab initial >/dev/null 2>/dev/null || echo "netlab up failed"'
  netlab down --cleanup >/dev/null 2>/dev/null
  echo "... done"
  echo ""
done
