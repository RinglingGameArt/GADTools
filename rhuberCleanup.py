"""
Ryan Huber
Must have object selected.
Deletes History, Freezes transforms, removes all keyframes.
Option checkbox UI coming soon.
"""
#imports
import maya.cmds as cmds
import logging

#variables
Selection = cmds.ls(sl=True) 
#window_name = "controlsWindow"

    cmds.delete(Selection, constructionHistory=True)
    cmds.cutKey(Selection, clear=True)
    cmds.makeIdentity(Selection, apply=True, t=1, r=1, s=1, n=0)

"""
#replace existing window
if cmds.window(window_name, q=True, exists=True):
    cmds.deleteUI(window_name)
#definitions
def DH(useDH):
    cmds.delete(constructionHistory=True)

#commands
cmds.delete(Selection, constructionHistory=True)
cmds.cutKey(Selection, clear=True)
cmds.makeIdentity(Selection, apply=True, t=1, r=1, s=1, n=0)

#make window
my_window = cmds.window(window_name, title="Cleanup")

#adjustability
my_layout = cmds.columnLayout(parent=my_window, adj=True)

#checkbox
cmds.checkBoxGrp(numberOfCheckBoxes=3, label='Options:    ', labelArray3=['Delte History', 'Freeze Transforms', 'Delete Keyframes'] )

#buttons 
cmds.button(parent = my_layout, l = "Confirm")

#show
cmds.showWindow(my_window)
"""
