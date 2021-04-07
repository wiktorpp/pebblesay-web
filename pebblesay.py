#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################
#importing liblaries#
#####################

from os import *
from threading import Timer
from textwrap import wrap
from browser import *

############################
#declaring static variables#
############################

asciiart = [
                      "     /|_   ___/|",
                      "    / __\\_/    |",
                      "   | /     \\   >",
                      "  / | Ó  °_ | /",
                "        | \\ ░ W ░/  |",
                "         \\_ |   _| /",
                "           < \\// -\\\  ___",
                "         /  /  _ --|\\/   \\",
                "         | /  / --/ |    /",
                "         \\   / \\     >  /",
                "   __     \\/__/_  / \\_  \\",
                "  O   \\  / /O O \\     \\  \\",
                "   O   \\/  °(_)°|      \\  |",
                "    \\   \\   \\   |      |  |",
                "     \\   \\   |   \\     | /",
                "      \\      |    |   /",
                "       \\_____\\___/___/",
]
mods = {
    "imgNoColor" : [
                          "     /|_   ___/|",
                          "    / __\\_/    |",
                          "   | /     \\   >",
                          "  / | Ó  °_ | /",
                    "        | \\ ░ W ░/  |",
                    "         \\_ |   _| /",
                    "           < \\// -\\\  ___",
                    "         /  /  _ --|\\/   \\",
                    "         | /  / --/ |    /",
                    "         \\   / \\     >  /",
                    "   __     \\/__/_  / \\_  \\",
                    "  O   \\  / /O O \\     \\  \\",
                    "   O   \\/  °(_)°|      \\  |",
                    "    \\   \\   \\   |      |  |",
                    "     \\   \\   |   \\     | /",
                    "      \\      |    |   /",
                    "nocolor\\_____\\___/___/(todo)"
    ],
    "uwu" : [
             "*",
             "*",
             "*",
             "  / | U   U | /"
    ],
    "ono" : [
                   "*",
                   "*",
                   "*",
                   "  / | O   O | /",
             "        | \\ ░ n ░/  |"
    ],
    "x3" : [
                   "*",
                   "*",
                   "*",
                   "  / | >   < | /",
             "        | \\ ░ W ░/  |"
    ]
}
width = 35



text = document["input"].value.split("\n")
think = False


#########################
#parsing text (wrapping)#
#########################

#wrapping text
textTmp = text
text = []
for i in textTmp:
    text.extend(wrap(i, width))
print(text)

#calculating width
width = max(len(i) for i in text)

####################
#printing (finally)#
####################
output = ""

#printing top line
output += " _"
for i in range(0, width):
    output += '_'
output += "_"

#printing one line of text
if len(text) == 1:
    output += "   {}<br>".format(asciiart[0])
    output += "< {} >  {}<br>".format(text[0], asciiart[1])

#printing multiple lines of text
elif len(text) > 1:
    output += "<br>"
    for i in range(0, len(text)):
        if i == 0:
            output += "/ {} \\  ".format(text[0].ljust(width))
        elif len(text) - i == 1:
            output += "\\ {} /  ".format(text[i].ljust(width))
        else:
            output += "│ {} │  ".format(text[i].ljust(width))

        #printing asciiart
        if len(text) - i == 2:
            output += asciiart[0]
        elif len(text) - i == 1:
            output += asciiart[1]

        output += "<br>"

spacing = " " * width

#printing bottom line
output += " ¯"
for i in range(0, width):
    output += '¯'
output += "¯ "
if not think:
    output += "\\ {}<br>".format(asciiart[2])
    output += spacing + "     \\{}<br>".format(asciiart[3])
else:
    output += "o {}<br>".format(asciiart[2])
    output += spacing + "     o{}<br>".format(asciiart[3])

#printing rest of asciiart
for i in range(4, len(asciiart)):
    output += spacing + asciiart[i] + "<br>"

document["output"].attach(html.CODE(output.replace(" ", "\u2800")))