# ssh-restrict: whitelist remote commands via ssh config 

ssh-restrict is a trivial script to safely execute remote commands via
SSH.  It is especially aimed at automated remote commands (in which SSH keys
are not secured via password), where a compromise of the remote system could
also compromise the local system.

To prevent this, you can invoke ssh-restrict through the SSH
authorized\_keys configuration, which will limit the remote system so that it can only execute a
set of statically defined commands. 

## Setup

In .ssh/authorized\_keys:

    command="/usr/local/bin/ssh-restrict /etc/ssh-restrict/backup",no-agent-forwarding,no-port-
    forwarding,no-pty,no-X11-forwarding ssh-rsa AAA13626…

command="..." sets the command, the other options disable potentially
dangerous stuff like port forwarding.

As you see, the forcecommand accepts exactly one argument, which is the configuration file
defining the allowed commands. 

The configuration file should look like this:

    home = tar -C / -cf - home
    say (\w+) (\d+)= echo {1}. {0}

## Usage

Now, on the remote system, run this:

    ssh user@yourhost home

On your system, this will translate to:

    tar -C / -cf - home
    
ssh-restrict supports arguments using regular expressions. If you run

    ssh user@yourhost say foo 25
    
it translates to

    echo 25. foo

