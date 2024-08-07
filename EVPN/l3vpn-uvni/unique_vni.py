'''
The plugin generates unique transit VNI per node
'''

from box import Box

def post_transform(topo: Box) -> None:
  for name,node in topo.nodes.items():
    if 'vrfs' not in node:
      continue
    for vname,vdata in node.vrfs.items():
      if vdata.get('evpn.evi') and vdata.get('evpn.transit_vni'):
        vdata.evpn.transit_vni = 200000 + 100 * vdata.evpn.evi + node.id
