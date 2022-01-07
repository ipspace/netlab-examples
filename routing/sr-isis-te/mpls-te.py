from box import Box
from netsim import common

def pre_link_transform(topo: Box) -> None:
  """
  Processes links with 'traffic-engineering-path' attribute, and resolves
  the loopback IPs of the peers included in the path
  """
  print( f"JvB mpls-te pre_link_transform" )

  for link in topo.links:
   for i in link.interfaces:
     if 'traffic_engineering_path' in i:
       print( f"Resolving: {i.traffic_engineering_path}" )
       te_path_ips = []
       for node in i.traffic_engineering_path:
         if node not in topo.nodes:
             common.error( f"Invalid node in TE-path: {node}", module='mpls-te')
             continue
         te_path_ips.append( topo.nodes[ node ].loopback.ipv4 )
       i.te_path_ips = te_path_ips

  # Check consistency of models
  # print( f"POST: nodes={topo.nodes}" )
  # print( f"POST: links={topo.links}" )
