#!/usr/bin/bash
#
# Clear log buffers on clients and servers
#
echo "y"|netlab connect srv1 clear logging
echo "y"|netlab connect srv2 clear logging
echo "y"|netlab connect cl_a clear logging
echo "y"|netlab connect cl_b clear logging
