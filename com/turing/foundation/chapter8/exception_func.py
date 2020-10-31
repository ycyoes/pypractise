def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')

# ignore_exception()

handle_exception()

from warnings import warn
warn("I've got a bad feeling about this.")