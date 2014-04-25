#imports
import maya.cmds as cmds
import logging

#variables
Selection = cmds.ls(sl=True)
#window_name = "controlsWindow"

cmds.delete(Selection, constructionHistory=True)
cmds.cutKey(Selection, clear=True)
cmds.makeIdentity(Selection, apply=True, t=1, r=1, s=1, n=0)
