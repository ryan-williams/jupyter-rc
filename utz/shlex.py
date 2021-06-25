from utz import escape

def join(args):
    '"%s"' % '" "'.join([escape.join(arg, '"') for arg in args])
