"""
rhuber
select verts
middle mouse drag
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

var = "polyAverageVertex1.iterations"

if cmds.filterExpand(sm=31): #31 = verts
    cmds.polyAverageVertex(i=0, ch=True)
    cmds.dragAttrContext('myDragAttrContext', e=True, ct=var)
    cmds.setToolTo('myDragAttrContext')

else:
    OpenMaya.MGlobal.displayWarning("At least one vertex must be selected.")

"""
cmds.selectMode(c=True)
cmds.selectMode(object=True)
cmds.delete(ch=True)
"""
