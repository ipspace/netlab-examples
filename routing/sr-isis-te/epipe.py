from box import Box

def post_transform(topo: Box) -> None:
  """
  Processes links with 'epipe' attribute, and resolves to the loopback IP of the peer
  """
  print( f"JvB epipe post_transform" )

  # Need to modify node.links, not global topo.links
  for node in topo.nodes.values():
   for link in node.links: # topo.links:
    if 'epipe' in link:
       peer = topo.nodes[ link.epipe ].loopback.ipv4
       print( f"JvB: Resolved {link.epipe} to {peer}" )
       link.epipe_peer = peer

  # Check consistency of models
  # print( f"POST: nodes={topo.nodes}" )
  # print( f"POST: links={topo.links}" )
