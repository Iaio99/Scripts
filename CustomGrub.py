#!/bin/python3
import subprocess
import sys

f = open("/etc/grub.d/40_custom","a")
print("""
if [ ${grub_platform} == "efi" ]; then
    menuentry "Shell UEFI" {
        insmod fat
        insmod chain
        search --no-floppy --set=root --file /shellx64.efi
        chainloader /shellx64.efi
    }
fi

menuentry "System Reboot" {
    echo "Rebooting the system..."
    reboot
}

menuentry "System halt" {
	echo "Halting the system..."
	halt
}""",file=f)
f.close()
subprocess.run(["grub-mkconfig", "-o", "/boot/grub/grub.cfg"], stdout=sys.stdout)

