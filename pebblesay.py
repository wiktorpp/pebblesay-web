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



text = document["input"].value
think = False


#########################
#parsing text (wrapping)#
#########################

#wrapping text
text = wrap(text, width)

#calculating width
width = max(len(i) for i in text)

####################
#printing (finally)#
####################

#printing top line
document["output"].attach(" _".replace(" ", "\u2800"))
for i in range(0, width):
    document["output"].attach('_')
document["output"].attach("_")

#printing one line of text
if len(text) == 1:
    document["output"].attach("   {}".format(asciiart[0]).replace(" ", "\u2800"))
    document["output"].attach(html.BR())
    document["output"].attach("< {} >  {}".format(text[0], asciiart[1]).replace(" ", "\u2800"))
    document["output"].attach(html.BR())

#printing multiple lines of text
elif len(text) > 1:
    document["output"].attach("")
    document["output"].attach(html.BR())
    for i in range(0, len(text)):
        if i == 0:
            document["output"].attach("/ {} \\  ".format(text[0].ljust(width)).replace(" ", "\u2800"))
        elif len(text) - i == 1:
            document["output"].attach("\\ {} /  ".format(text[i].ljust(width)).replace(" ", "\u2800"))
        else:
            document["output"].attach("│ {} │  ".format(text[i].ljust(width)).replace(" ", "\u2800"))

        #printing asciiart
        if len(text) - i == 2:
            document["output"].attach(asciiart[0].replace(" ", "\u2800"))
        elif len(text) - i == 1:
            document["output"].attach(asciiart[1].replace(" ", "\u2800"))

        document["output"].attach("")
        document["output"].attach(html.BR())

spacing = " " * width

#printing bottom line
document["output"].attach(" ¯".replace(" ", "\u2800"))
for i in range(0, width):
    document["output"].attach('¯'.replace(" ", "\u2800"))
document["output"].attach("¯ ".replace(" ", "\u2800"))
if not think:
    document["output"].attach("\\ {}".format(asciiart[2]).replace(" ", "\u2800"))
    document["output"].attach(html.BR())
    document["output"].attach((spacing + "     \\{}".format(asciiart[3])).replace(" ", "\u2800"))
    document["output"].attach(html.BR())
else:
    document["output"].attach("o {}".format(asciiart[2]).replace(" ", "\u2800"))
    document["output"].attach((spacing + "     o{}".format(asciiart[3])).replace(" ", "\u2800"))
    document["output"].attach(html.BR())

#printing rest of asciiart
for i in range(4, len(asciiart)):
    document["output"].attach((spacing + asciiart[i] + "").replace(" ", "\u2800"))
    document["output"].attach(html.BR())
