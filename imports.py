#!/usr/bin/env python
# coding: utf-8

# # imports
# Common Jupyter imports and helpers to wildcard import from other notebooks

# In[ ]:


from sys import executable as python
get_ipython().system('{python} -m pip install -q pandas')


# Helper for optional imports:

# In[7]:


from contextlib import suppress
_try = suppress(ImportError, ModuleNotFoundError)


# ## stdlib
# Common imports (and associated helpers) from the Python standard library:

# ### Date/Time

# In[ ]:


from dateutil.parser import parse
from datetime import datetime as dt, date
with _try: from pytz import UTC
now = dt.now()
today = now.strftime('%Y-%m-%d')


# ### Paths

# In[ ]:


from pathlib import Path
def mkdir(path, *args, **kwargs):
    os.mkdirs(str(path), *args, **kwargs)
    return path

def mkpar(path, *args, **kwargs):
    path.parent.mkdir(exist_ok=True, parents=True)
    return path


# ### Other

# In[ ]:


from dataclasses import dataclass

try:
    # Python 3.8
    from functools import cached_property, singledispatchmethod
except ImportError:
    try:
        # Python ≤3.7; pip install cached-property
        from cached_property import cached_property
    except ImportError as e:
        pass

from functools import partial, lru_cache, namedtuple, reduce, singledispatch

from itertools import combinations, combinations_with_replacement, permutations
import json

import os
from os import cpu_count
from os.path import dirname, basename

from re import match

from sys import stdout, stderr, executable as python

from tempfile import NamedTemporaryFile, TemporaryDirectory, TemporaryFile


# ## Sibling modules
# Some other notebooks and Python files from this repo:

# In[2]:


#import ur


# In[3]:


from . import process
from .process import *

from . import pnds
from .pnds import *

from .cd import cd
from .o import o

from .git_helpers import *

from .args_parser import *

from .context import *


# ## Optional Modules

# In[8]:


# joblib: easy parallelization
with _try:
    from joblib import Parallel, delayed
    parallel = Parallel(n_jobs=cpu_count())

# yaml
with _try: import yaml

# git.Repo: default to searching parent directories for a repository
with _try:
    import git
    Repo = partial(git.Repo, search_parent_directories=True)

# requests
with _try:
    from requests import           get as   GET,          post as  POST,           put as   PUT,         patch as PATCH


# ## PyData / Scientific Python

# In[9]:


import numpy as np
from numpy import concatenate, array, ndarray, matrix, nan


# In[10]:


with _try: import seaborn as sns
with _try: import matplotlib.pyplot as plt
with _try: from scipy.sparse import spmatrix, coo_matrix, csr_matrix, csc_matrix

