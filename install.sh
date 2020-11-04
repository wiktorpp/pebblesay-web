#!/bin/sh
SCRIPT=$(readlink -f $0)
SCRIPTPATH=$(dirname $SCRIPT)
if [ $# -eq 0 ]; then 
    echo "Usage: install.sh <install | purge | link>"
else
    if [ -w /usr/bin ] || [ "$1" = "temp" ]; then
        if [ "$1" = "install" ]; then
            if cp ${SCRIPTPATH}/nishisay.py /usr/bin/nishisay; then
                echo "Installed successfully."
            fi
        elif [ "$1" = "purge" ]; then
            if rm /usr/bin/nishisay; then
                echo "Uninstalled successfully."
            fi
        elif [ "$1" = "link" ]; then
            cp nishisay.py nishisay
            echo "\nexport PATH=\$PATH\":$SCRIPTPATH\"" >> ~/.bashrc
            echo "Please reopen your terminal window."
        else
            echo "Error: Wrong argument."
        fi
    else
        sudo sh $SCRIPT $1
    fi
fi