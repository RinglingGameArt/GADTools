#Mike Marra
#Intial Maya Setup for UDK Script
#Sets up the preferences commonly used in Maya for working with UDK

import maya.cmds as cmds
# Enables polygon borders and sets the edge width to 4 #
cmds.polyOptions(np=True, db=True, sb=4)
# Sets Undo amount to infinite #
cmds.undoInfo(infinity=True)
# Makes the viewcube visible #
cmds.viewManip(visible=True)
cmds.optionVar(iv=('viewCubeShowCube', 1))
# Sets the Z axis to be up #
cmds.upAxis(ax='z', rv=True)
# Sets the near and far clip for the persp view camera #
cmds.setAttr('perspShape.nearClipPlane', 1)
cmds.setAttr('perspShape.farClipPlane', 100000)
# Sets the near and far clip for the top view camera #
cmds.setAttr('topShape.nearClipPlane', 1)
cmds.setAttr('topShape.farClipPlane', 100000)
# Sets the near and far clip for the front view camera #
cmds.setAttr('frontShape.nearClipPlane', 1)
cmds.setAttr('frontShape.farClipPlane', 100000)
# Sets the near and far clip for the side view camera #
cmds.setAttr('sideShape.nearClipPlane', 1)
cmds.setAttr('sideShape.farClipPlane', 100000)
# To change the grid spacing and subdivisions #
cmds.grid(spacing=16, d=1)
# To change the grid length and width #
cmds.grid(size=512)
