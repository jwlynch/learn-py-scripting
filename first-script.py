#!/usr/bin/python3

__module_name__ = "Cancel's HelloBot"
__module_version__ = "1.0.0"
__module_description__ = "HelloBot by Cancel"

print( "\0034",__module_name__, __module_version__,"has been loaded\003" )

import xchat
import os
import re

def on_join(word, word_eol, userdata):
      triggernick, triggerchannel, triggerhost = word
      #we could also do triggernick = word[0]
      #we could also do triggernick = word[1] you get the picture
      destination = xchat.get_context()
      destination.command("say Hello " + triggernick + " and welcome to " + triggerchannel)

xchat.hook_print('Join', on_join)


