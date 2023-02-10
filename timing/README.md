# Measure Virtual Device Startup Time

The script in this directory was used to measure the time it takes to boot a network device and perform the minimal initial configuration.

If you want to repeat the measurements:

* [Install netlab](https://netsim-tools.readthedocs.io/en/latest/install.html)
* [Build Vagrant boxes](https://netsim-tools.readthedocs.io/en/latest/labs/libvirt.html) for the networking devices you want to test
* Execute `./timing.sh <list-of-devices>`
