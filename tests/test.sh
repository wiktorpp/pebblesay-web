#!/bin/bash
echo "-> nishisay test test test"
nishisay test test test test test test test test test test test test test test test test

echo "-> cat loremIpsum.txt | nishisay -n"
cat loremIpsum.txt | nishisay -n

echo "-> figlet test | nishisay"
figlet test | nishisay

echo "-> nishisay -c XD"
nishisay -c XD
echo "-> nishisay -n \"Hi, \\nhow are you?hhhhhhhhhhhhhhhhhhhhhhhhhh\""
nishisay -n "Hi, \nhow are you?hhhhhhhhhhhhhhhhhhhhhhhhhh"

echo "-> nishisay"
nishisay

echo "-> nishisay -t"
nishisay -t

echo "-> nishisay -p"
nishisay -p
