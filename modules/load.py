#!/usr/bin/env python
"""
load.py - Phenny Module loader Module
"""

import sys, os, time, imp
import irc


def f_load(phenny, input):
    """loads a module, for use by admins only."""
    if not input.admin:
        return

    if not input.group(2):
        return phenny.reply('load what ?')

    name = input.group(2)
    if name == phenny.config.owner:
        return phenny.reply('What?')

    path = None
    modpath = os.path.join(os.getcwd(), 'modules')
    for fn in os.listdir(modpath):
        if fn.endswith(name+'.py') and not fn.startswith('_'):
            path = fn

    if not path:
        return phenny.reply('Module %s not found.' % name)

    filepath = os.path.join(modpath, path)

    if filepath.endswith('.pyc') or filepath.endswith('.pyo'):
        filepath = filepath[:-1]
    if not os.path.isfile(filepath):
        return phenny.reply('Found %s, but not the source file' % path)

    try:
        module = imp.load_source(name, filepath)
    except Exception, e:
        print >> sys.stderr, "Error loading %s: %s (in load.py)" % (name, e)

    if hasattr(module, 'setup'):
        module.setup(phenny)
    sys.modules[name] = module

    mtime = os.path.getmtime(module.__file__)
    modified = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(mtime))

    phenny.register(vars(module))
    phenny.bind_commands()

    phenny.reply('%r (version: %s)' % (module, modified))

f_load.name = 'load'
f_load.rule = (['load'], r'(\S+)?')
f_load.priority = 'high'
f_load.thread = False

if __name__ == '__main__':
    print __doc__.strip()
