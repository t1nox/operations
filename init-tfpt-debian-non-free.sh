#!/bin/bash



# tftp directory
TFTP="/srv/tftp"

# temporary working directory
# FOR Debian 10 Buster 
TMP_TFTPx64deb10="/srv/tmp/debian-10-amd64-current"
TMP_TFTPx86deb10="/srv/tmp/debian-10-i386-current"

#For Debian 9 Stretch x64
#TMP_TFTPx64deb9="/srv/tmp/debian-9-amd64-current"  #не в этот раз

# debian netboot url
URLdeb10amd64="http://ftp.fr.debian.org/debian/dists/buster/main/installer-amd64/current/images/netboot/debian-installer/amd64"
URLdeb10x86="http://ftp.fr.debian.org/debian/dists/buster/main/installer-i386/current/images/netboot/debian-installer/i386"

URLfirmwareDeb10="http://cdimage.debian.org/cdimage/unofficial/non-free/firmware/buster/current"

URLfirmwareDeb9="http://cdimage.debian.org/cdimage/unofficial/non-free/firmware/jessie/current"

mkdir -p $TMP_TFTPx64deb10
mkdir -p $TMP_TFTPx86deb10
#mkdir -p $TMP_TFTPx64deb9 # не нуждается в обновлении


cd    $TMP_TFTP

wget "http://cdimage.debian.org/cdimage/unofficial/non-free/firmware/wheezy/current/firmware.tar.gz"
