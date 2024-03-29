#!/bin/sh


echo "Resetting iptables Rules..."
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -t raw -F
iptables -t raw -X
iptables -t security -F
iptables -t security -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
echo "Done"


#Start of firewall setup
iptables -N TCP
iptables -N UDP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
iptables -P INPUT DROP
iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT
iptables -A INPUT -p udp -m conntrack --ctstate NEW -j UDP
iptables -A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP
iptables -A INPUT -p udp -j REJECT --reject-with icmp-port-unreachable
iptables -A INPUT -p tcp -j REJECT --reject-with tcp-reset
iptables -A INPUT -j REJECT --reject-with icmp-proto-unreachable
#Services that you want
iptables -A TCP -p tcp --dport 22 -j ACCEPT

##Spoofing attack protection
#sysctl net.ipv4.conf.all.rp_filter=1
#
##Block ping request
#sysctl net.ipv4.icmp_echo_ignore_all=1
#
##Protection against SYN scans
#iptables -I TCP -p tcp -m recent --update --rsource --seconds 60 --name TCP-PORTSCAN -j REJECT --reject-with tcp-reset
#iptables -D INPUT -p tcp -j REJECT --reject-with tcp-reset
#iptables -A INPUT -p tcp -m recent --set --rsource --name TCP-PORTSCAN -j REJECT --reject-with tcp-reset
#
##UDP Scans
#iptables -I UDP -p udp -m recent --update --rsource --seconds 60 --name UDP-PORTSCAN -j REJECT --reject-with icmp-port-unreachable
#iptables -D INPUT -p udp -j REJECT --reject-with icmp-port-unreachable
#iptables -A INPUT -p udp -m recent --set --rsource --name UDP-PORTSCAN -j REJECT --reject-with icmp-port-unreachable
#
##Restore Final Rule
#iptables -D INPUT -j REJECT --reject-with icmp-proto-unreachable
#iptables -A INPUT -j REJECT --reject-with icmp-proto-unreachable
#
##Protection against bruteforce attacks
#iptables -N IN_SSH
#iptables -N LOG_AND_DROP
#iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -j IN_SSH
#iptables -A IN_SSH -m recent --name sshbf --rttl --rcheck --hitcount 3 --seconds 10 -j LOG_AND_DROP
#iptables -A IN_SSH -m recent --name sshbf --rttl --rcheck --hitcount 4 --seconds 1800 -j LOG_AND_DROP 
#iptables -A IN_SSH -m recent --name sshbf --set -j ACCEPT
#iptables -A LOG_AND_DROP -j LOG --log-prefix "iptables deny: " --log-level 7
#iptables -A LOG_AND_DROP -j DROP
#
##IPv6
##cp /etc/iptables/iptables.rules /etc/iptables/ip6tables.rules
##ip6tables -A INPUT -p ipv6-icmp --icmpv6-type 128 -m conntrack --ctstate NEW -j ACCEPT
##ip6tables -A INPUT -s fe80::/10 -p ipv6-icmp -j ACCEPT
##ip6tables -A INPUT -p udp --sport 547 --dport 546 -j ACCEPT
##ip6tables -t mangle -A PREROUTING -m rpfilter -j ACCEPT
##ip6tables -t mangle -A PREROUTING -j DROP
#
##Save
#iptables-save -f /etc/iptables/iptables.rules
##ip6tables-save -f /etc/iptables/#ip6tables.rules