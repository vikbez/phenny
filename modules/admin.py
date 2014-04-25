#!/usr/bin/env python
"""
admin.py - Phenny Admin Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""


def join(phenny, input):
    """Join the specified channel. This is an admin-only command."""
    # Can only be done in privmsg by an admin
    if not input.admin or input.sender.startswith('#'):
        return
    channel, key = input.group(2), input.group(3)
    if (not channel) or (not channel.startswith('#')):
        return phenny.reply(join.example)
    if not key:
        phenny.write(['JOIN'], channel)
    else:
        phenny.write(['JOIN', channel, key])
join.rule = (['join'], r'(#\S+) (.+)?')
join.priority = 'low'
join.example = '$!join #example (key)'


def part(phenny, input):
    """Part the specified channel. This is an admin-only command."""
    # Can only be done in privmsg by an admin
    if not input.admin or input.sender.startswith('#'):
        return
    channel = input.group(2)
    if (not channel) or (not channel.startswith('#')):
        return phenny.reply(part.example)
    phenny.write(['PART'], channel)
part.rule = (['part'], r'(#\S+)')
part.priority = 'low'
part.example = '$!part #example'


def quit(phenny, input):
    """Quit from the server. This is an owner-only command."""
    # Can only be done in privmsg by the owner
    if input.sender.startswith('#'):
        return
    if input.owner:
        phenny.write(['QUIT'])
        __import__('os')._exit(0)
quit.commands = ['quit']
quit.priority = 'low'
quit.example = '$!quit'


def say(phenny, input):
    # Can only be done in privmsg by an admin
    if input.sender.startswith('#'):
        return phenny.reply(say.example)
    a, b = input.group(2), input.group(3)
    if (not a) or (not b):
        return phenny.reply(say.example)
    if input.admin:
        phenny.msg(a, b)
say.rule = (['say'], r'(#?\S+) (.+)')
say.priority = 'low'
say.example = '$!say nick/channel message'


def mesay(phenny, input):
    # Can only be done in privmsg by an admin
    if input.sender.startswith('#'):
        return phenny.reply(mesay.example)
    a, b = input.group(2), input.group(3)
    if (not a) or (not b):
        return phenny.reply(mesay.example)
    if input.admin:
        msg = '\x01ACTION %s\x01' % b
        phenny.msg(a, msg)
mesay.rule = (['mesay'], r'(#?\S+) (.+)')
mesay.priority = 'low'
mesay.example = '$!mesay nick/channel message'


def kick(phenny, input):
    if not input.admin:
        return
    a, b = input.group(2), input.group(3)
    if (not a) or (not b):
        return phenny.reply(kick.example)
    phenny.write(['KICK', input.sender, a], b)
    return
kick.rule = (['kick'], r'(.+) (.+$)')
kick.priority = 'high'
kick.example = '$!kick pseudo reason'


if __name__ == '__main__':
    print __doc__.strip()
