#
# Turn a dictionary (or most everything else) into a single-element list
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError

def make_list(l):
  return l if type(l) is list else [l]

class FilterModule(object):
  def filters(self):
    return {
      'make_list': make_list
    }
