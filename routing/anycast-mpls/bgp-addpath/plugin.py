'''
Custom plugin for BGP anycast scenario

Removes IBGP sessions from the members of the 'anycast' group
'''

import sys
from box import Box
from netsim.augment import topology
from netsim import common
from netsim import api

def init(topo: Box) -> None:
  topo.defaults.bgp.attributes.node.append('add_path')

def post_transform(topo: Box) -> None:
  config_name = api.get_config_name(globals())
  for name,node in topo.nodes.items():
    if 'add_path' in node.get('bgp',{}):
      api.list_attribute(node.bgp,'add_path',f'nodes.{node.name}.bgp')
      api.node_config(node,config_name)
