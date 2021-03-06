'''
By Megan Rose
Wireframe, 
SoftShade,
Wireframe on Shaded and
Toggle Normals
in Four viewports
'''

'''
	Turns on Wireframe in all viewports
'''

import maya.cmds as cmds
#makes P an array. ModelPanel tells getpanel we want the panels that are in sight right now.
p = cmds.getPanel(type='modelPanel')
# This is looping through all of the panels we got from our getPanel
for view in p:
# change a model's appearance or physical materal. We take the Panels from View. Edit the displayAppearances to wireframe.
		cmds.modelEditor(view, edit=True, displayAppearance='wireframe' )


'''
	Turns on Smoothshade in all viewports
'''

import maya.cmds as cmds
#makes P an array. ModelPanel tells getpanel we want the panels that are in sight right now.
p = cmds.getPanel(type='modelPanel')
# This is looping through all of the panels we got from our getPanel
for view in p:
# change a model's appearance or physical materal. We take the Panels from View. Edit the displayAppearances to smoothshaded.
		cmds.modelEditor(view, edit=True, displayAppearance='smoothShaded' )

'''
	Toggle wireframe On Shaded
'''

import maya.cmds as cmds
 
#makes P an array. ModelPanel tells getpanel we want the panels that are in sight right now.
p = cmds.getPanel(type='modelPanel')
 
#This is looping through all of the panels we got from our getPanel
for view in p:
	
        # check to see if the view currently has the wireframe shaded
        currentState = cmds.modelEditor(view, q = True, wireframeOnShaded = True)

        # change a panel's wireframe shading to the opposite of what it is currently set to
        cmds.modelEditor(view, edit = True, wireframeOnShaded = not currentState)
	
'''
	Toggle Normals       
'''

import maya.cmds as cmds

selection = cmds.ls(sl= True)

cmds.polyOptions(f=True,r=True, dn=True)
#PolyOptions Changes the global display polygonal attributes(fancydef)
#F flag is Force, R flag is Replace, DN flag is Display Normals
