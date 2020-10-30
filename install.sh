#!/bin/sh
SCRIPT=$(readlink -f $0)
SCRIPTPATH=$(dirname $SCRIPT)
if [ $# -eq 0 ]; then 
    echo "Usage: install.sh [install | uninstall]"
else
    if [ -w /usr/bin ]; then
        if [ "$1" = "install" ]; then
            cp ${SCRIPTPATH}/nishisay.py /usr/bin/nishisay
            if [ $? -eq 0 ]; then
                echo "Installed successfully."
            fi
        elif [ "$1" = "uninstall" ]; then
            rm /usr/bin/nishisay
            if [ $? -eq 0 ]; then
                echo "Uninstalled successfully."
            fi
        fi
    else
        sudo sh $SCRIPT $1
    fi
fi