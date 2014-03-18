#!/usr/bin/env python
"""
Simple debug module
"""


def debug(phenny, input):
    print ("[ADMIN]:%s - [input.sender]:%s - [input.nick]:%s - "
           "[input.action]:%s - [input RAW]:%s") % (
        input.admin, input.sender, input.nick, input.event, input)
    return

debug.rule = r'.*'
debug.priority = 'low'
debug.example = 'anything'
