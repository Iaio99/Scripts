#!/bin/python3
import subprocess

fs_uuid=subprocess.getoutput("grub-probe --target=fs_uuid /boot/EFI/Microsoft/Boot/bootmgfw.efi")
hints_string=subprocess.getoutput("grub-probe --target=hints_string /boot/EFI/Microsoft/Boot/bootmgfw.efi")
f=open("/etc/grub.d/40_custom","a")
print("""
if [ ${grub_platform} == "efi" ]; then
	menuentry "Firmware setup" {
            fwsetup
	}
        fi
if [ ${grub_platform} == "efi" ]; then
    menuentry "Shell UEFI" {
        insmod fat
        insmod chain
        search --no-floppy --set=root --file /shellx64.efi
        chainloader /shellx64.efi
    }
fi
menuentry "Riavvio del sistema" {
    echo "Riavviando il sistema..."
    reboot
}
menuentry "Arresto del sistema" {
	echo "Arrestando il sistema..."
	halt
}""",file=f)
f.close()

