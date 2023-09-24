#!/bin/sh

backup_dir="Backup"

# Ottieni la lista dei nomi dei container
container_list=$(lxc list --format csv --columns=n)

# Itera su ogni nome del container
for container_name in $container_list
do
    # Crea un file di backup compresso per ciascun container
    lxc export $container_name $backup_dir/$container_name.tar.gz

    echo "Backup del container $container_name completato."
done

