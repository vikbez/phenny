#!/usr/bin/env python
"""
loadlist.py - Phenny Module Lister
"""

import sys, os.path, time, imp
import irc


def f_loadlist(phenny, input):
    """List all modules with status, for use by admins only."""
    if not input.admin:
        return

    modlist = None
    modloaded = []
    modnotloaded = []
    modpath = os.path.join(os.getcwd(), 'modules')
    for fn in os.listdir(modpath):
        if fn.endswith('.py') and not fn.startswith('_'):
            if fn[:-3] in sys.modules:
                modloaded.append(fn[:-3])
            else:
                modnotloaded.append(fn[:-3])

    phenny.reply('Loaded modules:')
    phenny.reply(', '.join(map(str, modloaded)))
    phenny.reply('Not loaded modules:')
    phenny.reply(', '.join(map(str, modnotloaded)))

f_loadlist.name = 'loadlist'
f_loadlist.commands = (['loadlist'])
f_loadlist.priority = 'high'
f_loadlist.thread = False

if __name__ == '__main__':
    print __doc__.strip()
