"""
rhuber
select verts
middle mouse drag
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
suf = cmds.listHistory()[1].replace("polyAverageVertex", "")
pAV = "polyAverageVertex" + str(suf) + ".iterations" #these two can be consolidated, already getting name, just add.iterations

if cmds.filterExpand(sm=31): #31 = verts
    cmds.polyAverageVertex(i=0, ch=True)
    suf = cmds.listHistory()[1].replace("polyAverageVertex", "")
    print suf
    cmds.dragAttrContext('myDragAttrContext', e=True, ct=pAV) #something wrong here, fix
    cmds.setToolTo('myDragAttrContext')

else:
    OpenMaya.MGlobal.displayWarning("At least one vertex must be selected.")

