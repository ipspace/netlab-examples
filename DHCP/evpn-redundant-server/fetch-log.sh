#!/usr/bin/bash
#
# Clear log buffers on clients and servers
#
netlab connect srv1 show log >$1-srv1.log
netlab connect srv2 show log >$1-srv2.log
netlab connect cl_a show log >$1-cl_a.log
