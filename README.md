# Pyrmenum

A Python-based filesystem permissions enumerator. The idea here is that with a given principle (user, group, etc.), you can visualize the access that principle has on the file system.

## Who the heck cares?
- 🖨️ Sysadmins auditing their filesystems for permissions creep.
- 👨🏽‍💻 Penetration testers enumerating filesystems following exploitation.
- 🕺🏼 Anyone else who may want to know who can read/write what!

## How the heck does it work?
Unfortunately, you have you to do it the hard way for the time being (we're still under development). But here's an example to appease the masses: ```python3 pyrmenum.py --help```

Make sense?