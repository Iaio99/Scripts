#!/bin/python3

import sys

from argparse import ArgumentParser
from shutil import which
from subprocess import getoutput


def check_networkmanager():
    return which(name) is not None


def make_hotspot(ssid, password, ifname, con_name):
    getoutput(f"nmcli con add type wifi ifname {ifname} con-name {con_name} autoconnect yes ssid {ssid}")
    getoutput(f"nmcli con modify {con_name} 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared")
    getoutput(f"nmcli con modify {con_name} wifi-sec.key-mgmt wpa-psk")
    getoutput(f"nmcli con modify {con_name} wifi-sec.psk '{password}'")
    getoutput(f"nmcli con up {con_name}")


parser = ArgumentParser()

parser.add_argument("ssid", help="SSID of wifi connection hotspot", type=str)
parser.add_argument("password", help="Password of wifi connection hotspot", type=str)
parser.add_argument("wifi-interface", help="Wi-Fi interface to use for hotspot", type=str)
parser.add_argument("con-name", help="Connection name", default="Hotspot", type=str)

args = parser.parse_args()


if __name__ == "__main__":
    if not check_networkmanager:
        print("This program requires Network Manager!", file=sys.stderr)
        sys.exit(2)

    make_hotspot(args.ssid, args.password, args.ifname, args.con_name)
    