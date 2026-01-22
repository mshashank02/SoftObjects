import meshio 
m = meshio.read("/home/mshashank02/SoftObjectsV2/objects/large_1/tet_coarse/tetwild_out_.msh")
print([(c.type, len(c.data)) for c in m.cells])