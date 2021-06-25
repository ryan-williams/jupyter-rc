# Helper for optional imports:
from contextlib import suppress
_try = suppress(AttributeError, ImportError, ModuleNotFoundError)
