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
textWrapped = []
for i in text:
    textWrapped.extend(wrap(i, 35))
text=textWrapped

#calculating width
textWidth = max(len(i) for i in text)
textHeight = len(text)

##########
#printing#
##########
output = []

#generating top line
output.append(f" {'_' * (textWidth + 2)}   ")

#one line of text
if textHeight == 1:
    output.append(f"< {text[0]} >  ")

#multiple lines of text
else:
    for i, line in enumerate(text):
        if i == 0:
            output.append(f"/ {line.ljust(textWidth)} \\  ")
        elif textHeight - i == 1:
            output.append(f"\\ {line.ljust(textWidth)} /  ")
        else:
            output.append(f"│ {line.ljust(textWidth)} │  ")

spacing = " " * textWidth

#creating bottom line and the tail
tailChar = "\\"
output.append(f" {'¯' * (textWidth + 2)} {tailChar} ")
output.append(f"{spacing}     {tailChar}")

output = [f"{bubbleLine}{asciiartLine}" for bubbleLine, asciiartLine in 
    zip(
        output, 
        ["" for _ in range(textHeight + 3 - 4)] + asciiart[:4]
    )
]

#appending the rest of asciiart
for line in asciiart[4:]:
    output.append(f"{spacing}{line}")

print("\n".join(output))

#document["output"].attach(html.CODE(html.H6(output.replace(" ", " "))))
for line in output:
    window.term.writeln(line)