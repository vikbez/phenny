WHATISTHIS
==========
This is a fork of [phenny irc bot](https://github.com/sbp/phenny).  
The goal of this version is to be simple, extensible, with minimum modules possible.  
This version also supports (kinds of) hot load/unload/reload.  
Thanks to [sfan5](https://github.com/sfan5) this version also implements hostmasks for owner/admin identification.  


USE IT
======
1. Run ./phenny - this creates a default config file
2. Edit ~/.phenny/default.py
3. Move config file to phenny folder if you want
4. Run ./phenny - this now runs phenny with your settings


IMPROVE IT
==========
How to make modules: [myano's tutorial](https://github.com/myano/jenni/wiki/How-to-create-a-phenny-module)


TODO
====
- improve load/unload/reload/loadlist modules
- improve configuration files check
- clean code
- simplify code
- unify rules of modules
- save current load-unload state of modules to config file (make config file dynamic)
- add module.throttle (in seconds, implements usage limit per user per command)


LINKS
=====
Original author: [Sean B. Palmer](http://inamidst.com/sbp)
