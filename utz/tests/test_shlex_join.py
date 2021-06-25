
from utz import shlex_join

def test_shlex_join():
    assert shlex_join(list('abc')) == '"a" "b" "c"'
