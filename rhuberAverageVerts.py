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
    cmds.polyAverageVertex(i=0, ch=True)
    cmds.dragAttrContext('myDragAttrContext', e=True, ct='polyAverageVertex1.iterations')
    cmds.setToolTo('myDragAttrContext')

else:
    OpenMaya.MGlobal.displayWarning("At least one vertex must be selected.")


"""

import maya.cmds as cmds

# Procedure called on press
def SampleContextPress():
    pressPosition = cmds.draggerContext( 'sampleContext', query=True, anchorPoint=True)
    print ("Press: " + str(pressPosition))

# Procedure called on drag
def SampleContextDrag():
    dragPosition = cmds.draggerContext( 'sampleContext', query=True, dragPoint=True)
    button = cmds.draggerContext( 'sampleContext', query=True, button=True)
    modifier = cmds.draggerContext( 'sampleContext', query=True, modifier=True)
    print ("Drag: " + str(dragPosition) + " Button is " + str(button) + " Modifier is " + modifier + "\n")
    message = str(dragPosition[0]) + ", " + str(dragPosition[1])
    cmds.draggerContext( 'sampleContext', edit=True, drawString=message)

# Define draggerContext with press and drag procedures
cmds.draggerContext( 'sampleContext', pressCommand='SampleContextPress()', dragCommand='SampleContextDrag()', cursor='hand' );

# Set the tool to the sample context created
# Results can be observed by dragging mouse around main window
cmds.setToolTo('sampleContext')

"""
