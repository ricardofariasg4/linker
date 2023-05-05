#!/bin/bash

PENDRIVES_MEDIA=$(lsblk | awk '{print $7}' | grep /media | cut -d / -f 3)
PENDRIVES_MNT=$(lsblk | awk '{print $7}' | grep /mnt | cut -d / -f 3)

# Grava o nome dos pendrives em um arquivo
echo "$PENDRIVES_MEDIA" > pendrives_media.txt
echo "$PENDRIVES_MNT" > pendrives_mnt.txt

