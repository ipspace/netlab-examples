import sys
from box import Box
from netsim import common

def post_transform(topo: Box) -> None:
  """
  Processes links with 'traffic-engineering-path' attribute, and resolves
  the loopback IPs of the peers included in the path
  """
  print( f"JvB mpls-te post_transform" )

  # Need to modify node.links, not global topo.links
  for node in topo.nodes.values():
   for link in node.links: # topo.links:
    if 'traffic_engineering_path' in link:
       te_path_ips = []
       for node in link.traffic_engineering_path:
         te_path_ips.append( topo.nodes[ node ].loopback.ipv4 )
       link.te_path_ips = te_path_ips

  # Check consistency of models
  # print( f"POST: nodes={topo.nodes}" )
  # print( f"POST: links={topo.links}" )
