from py2neo import Graph, Node, Relationship, authenticate

authenticate("hobby-kfleidofeielgbkejgnknfpl.dbs.graphenedb.com:24789", "shifter", "b.ngigs6TLdGbW.nMOTq9xe36TkiDJH")

graph = Graph(
    'http://hobby-kfleidofeielgbkejgnknfpl.dbs.graphenedb.com:24789',
    bolt = False
)

print('Creating node ... ')

test_node = Node('Entity ', eid='21398alkdalskj02', tri='askmdfoqoms')
graph.create(test_node)

print('Node was created successfully ...')

print(test_node['eid'])
