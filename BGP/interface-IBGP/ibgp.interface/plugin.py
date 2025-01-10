'''
Custom plugin for BGP anycast scenario

Removes IBGP sessions from the members of the 'anycast' group
'''

from box import Box
from netsim import api, data

_config_name: str = ''

def post_transform(topo: Box) -> None:
  for name,node in topo.nodes.items():
    if 'bgp.neighbors' not in node:
      continue

    node.bgp.neighbors = [ ngb for ngb in node.bgp.neighbors if ngb.type != 'ibgp' ]

    for intf in node.interfaces:
      for ngb in intf.neighbors:
        ngb_data = topo.nodes[ngb.node]
        if 'bgp' not in ngb_data:
          continue
        if ngb_data.get('bgp.as',None) != node.get('bgp.as',0):
          continue

        ibgp_ngb = { 'as': ngb_data.get('bgp.as'), 'name': ngb.node, 'type': 'localas_ibgp', 'activate': {} }
        for af in ['ipv4','ipv6']:
          if af in intf and af in ngb:
            ibgp_ngb['activate'][af] = True
            ibgp_ngb[af] = ngb[af].split('/')[0]

        node.bgp.neighbors.append(ibgp_ngb)
