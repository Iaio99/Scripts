# Scripts
A series of scripts for automate a series of (boring) tasks.

## Description of scripts
* `firewall-setup.sh`: This script setup a firewall with iptables. I followed the guide at this link: https://wiki.archlinux.org/title/Simple_stateful_firewall. (**NB**: This script actually works ONLY for ipv4 and for a PC not for a server or for a router):

* `hotspot.py`: This script setup and start and hotspot wifi through Network Manager.

* `CustomGrub.py`: This script edit `/etc/grub/40-custom` and adds some voices, then it regenarete the `grub.cfg`.