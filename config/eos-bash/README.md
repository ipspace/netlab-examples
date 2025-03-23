# Running a Custom Bash Script on Arista EOS

This directory demonstrates how to run a **bash** script as a custom configuration template on an Arista EOS container.

The gist of the solution is the `run-script` custom configuration template directory. It contains:

* `eos.j2` -- the template for the **bash** script that will be executed on Arista switches.
* `deploy.eos-clab.yml` -- deployment task list for Arista cEOS containers. It uses Docker to create the target script file directly within the container and execute it.
* `deploy.eos.yml` -- deployment task list for Arista VMs. It creates a local file from the script template, uses **scp** to copy it to the Arista switch, and **bash** EOS command to execute the script.

The bash script creates the `/tmp/hello.txt` file. Use the `netlab exec '*' bash cat /tmp/hello.txt` command to verify that the file has been created.
