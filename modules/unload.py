#!/usr/bin/env python
"""
unload.py - Phenny Module unloader Module
"""

import sys, os.path, time, imp
import irc


def f_unload(phenny, input):
    """Reloads a module, for use by admins only."""
    if not input.admin:
        return

    name = input.group(2)

    if not name:
        return phenny.reply('unload what ?')

    if name == phenny.config.owner:
        return phenny.reply('What?')

    if not sys.modules.has_key(name):
        return phenny.reply('%s: no such module!' % name)

    del(sys.modules[name])
    phenny.variables = None
    phenny.commands = None
    phenny.setup()
    # TODO: replace phenny.setup with search and delete commands
    # phenny.bind_commands()

    phenny.reply('<unloaded %s>' % name)
f_unload.name = 'unload'
f_unload.rule = (['unload'], r'(\S+)?')
f_unload.priority = 'high'
f_unload.thread = False

if __name__ == '__main__':
    print __doc__.strip()
