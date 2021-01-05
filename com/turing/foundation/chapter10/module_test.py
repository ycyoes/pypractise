import hello
hello.hello()

import copy
print([n for n in dir(copy) if not n.startswith('_')])
