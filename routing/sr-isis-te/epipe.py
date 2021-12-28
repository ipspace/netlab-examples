import sys
from box import Box
from netsim import common

def post_transform(topo: Box) -> None:
  """
  Processes links with 'epipe' attribute, and resolves to the loopback IP of the peer
  """
  print( "JvB epipe post_transform:" )

  # Need to modify node.links, not global topo.links
  for node in topo.nodes:
   for link in node.links: # topo.links:
    if 'epipe' in link:
       peer = topo.nodes_map[ link.epipe ].loopback.ipv4
       print( f"JvB: Resolved {link.epipe} to {peer}" )
       link.epipe_peer = peer
