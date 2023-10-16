from box import Box

def post_transform(topo: Box) -> None:
  for ndata in topo.nodes.values():
    if not ndata.get('bgp.neighbors',[]):
      continue

    ndata.bgp.neighbors = [ ngb for ngb in ndata.bgp.neighbors if ngb['as'] != 65013 ]
