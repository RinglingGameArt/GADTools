"""
Didn't figure out how to attach the drag context in time.
I just copied the example from autodesk.com, not sure what's wrong
DON'T FORGET, MAKE DRAGGER FOR BEVEL OFFSET (.1 STEP SIZE)
AND POLY AVERAGE (1 STEP SIZE)
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

cmds.dragAttrContext('myDragAttrContext')

if cmds.filterExpand(sm=31):
    cmds.polyAverageVertex(i=0, ch=False)
    cmds.dragAttrContext('myDragAttrContext', e=True, ct='polyAverageVertex.iterations')
    cmds.setToolTo('myDragAttrContext')

else:
    OpenMaya.MGlobal.displayWarning("At least one vertex must be selected.")


####################

def SampleContextPress():
    pressPosition = cmds.dra

####################

"""
contextToolsMM "MayaWindow|formLayout1|viewPanes|modelPanel4|modelPanel4|modelPanel4|modelPanel4CommandPop";
AverageVertex;
polyPerformAction polyAverageVertex v 0;
polyAverageVertex -ch 1 pSphere1.vtx[8:9] pSphere1.vtx[16:18] pSphere1.vtx[24:26] pSphere1.vtx[32:34] pSphere1.vtx[40:41];
// Result: polyAverageVertex2 //
// Result: polyAverageVertex -ch 1 pSphere1.vtx[8:9] pSphere1.vtx[16:18] pSphere1.vtx[24:26] pSphere1.vtx[32:34] pSphere1.vtx[40:41] //
refreshAE;
select -addFirst polyAverageVertex2 ;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {source buildDisplayMenu;} polyNormalSizeMenuUpdate;
dR_updateCounter; dR_updateSymButton;
dR_updateCommandPanel;
changeToolIcon;
dR_contextChanged;
currentCtx;
// Result: dragAttrContext //
setAttr "polyAverageVertex2.iterations" 69.7;
"""
