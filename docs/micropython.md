
## MicroPython Port of pycoin

### Requirements

- micropython
- these **upip** modules:

    micropython-binascii
    micropython-hashlib
    micropython-io
    micropython-struct
    micropython-unittest
    micropython-os
    micropython-hmac
    micropython-functools
    micropython-collections
    micropython-itertoosl       (might be optional?)

- do not install:

    micropython-decimal
        - it is a dummy module
        - instead, use integer satoshi's for everything

- required only for unit tests:
    micropython-json
    micropython-tempfile


