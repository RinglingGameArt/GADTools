"""
rhuber
select verts
middle mouse drag
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

pAV = "polyAverageVertex" + "1" + ".iterations"

if cmds.filterExpand(sm=31): #31 = verts
    cmds.polyAverageVertex(i=0, ch=True)
    cmds.dragAttrContext('myDragAttrContext', e=True, ct=pAV)
    cmds.setToolTo('myDragAttrContext')

else:
    OpenMaya.MGlobal.displayWarning("At least one vertex must be selected.")

"""
cmds.selectMode(c=True)
cmds.selectMode(object=True)
cmds.delete(ch=True)
"""



vert = cmds.ls(sl=True)
sel = cmds.sets()
#fix this part


cmds.selectMode(co=True)
cmds.selectMode(o=True)
sel = cmds.sets()
suf = cmds.listHistory()[1].replace("polyAverageVertex", "")
cmds.selectMode(co=True)
cmds.select(sel)

print suf
cmds.listConnections(type='inputs')
cmds.listHistory(ha=True, pdo=True, future=True)
