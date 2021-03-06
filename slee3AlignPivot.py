# Soojin Lee 
# GA 240_01 
# This script helps to make align pivot with multiple objects
# also can change all of the pivot location bottom XYZ / good for the modular kits 
# selected multiple objects and run the script. 


import maya.cmds as cmds
    
#function settings   
def myFunction1(*args): #gives a definition and hold the values of all nonkeyword variable arguments. / *args 
    #function1=X button
    selection = cmds.ls(sl=True)
    for selected in selection:
        bounding_box = cmds.xform(selected, q=True, boundingBox=True, ws=True)
        xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
    
        cmds.move(xmin, ymin, zmin, [selected +".scalePivot",selected + ".rotatePivot"], x=True, y=True, z=True, absolute=True)
        #change location of pivot
        # change the xyz min and max for ajust pivot location
        piv = cmds.xform (selected , piv=True, q=True, ws=True) 
        cmds.xform(selection , ws=True, piv=(piv[0], piv[1], piv[2]) )#Align pivot to the x button pivot setting

    
def myFunction2(*args):
    selection = cmds.ls(sl=True)
    for selected in selection:
        bounding_box = cmds.xform(selected, q=True, boundingBox=True, ws=True)
        xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
        
        cmds.move(xmax, ymin, zmin, [selected +".scalePivot",selected + ".rotatePivot"], x=True, y=True, z=True, absolute=True)
        #change location of pivot
        piv = cmds.xform (selected , piv=True, q=True, ws=True) 
        cmds.xform(selection , ws=True, piv=(piv[0], piv[1], piv[2]) )#Align pivot to the y button pivot setting

def myFunction3(*args):
    selection = cmds.ls(sl=True)
    for selected in selection:
        bounding_box = cmds.xform(selected, q=True, boundingBox=True, ws=True)
        xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
        
        cmds.move(xmax, ymax, zmin, [selected +".scalePivot",selected + ".rotatePivot"], x=True, y=True, z=True, absolute=True)
        #change location of pivot
        piv = cmds.xform (selected , piv=True, q=True, ws=True) 
        cmds.xform(selection , ws=True, piv=(piv[0], piv[1], piv[2]) )#Align pivot to the z button pivot setting

def myFunction4(*args): #new!
    selection = cmds.ls(sl=True)
    for selected in selection:
        bounding_box = cmds.xform(selected, q=True, boundingBox=True, ws=True)
        xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
        
        cmds.xform(selected, cp=True)
        piv = cmds.xform (selected , piv=True, q=True, ws=True) 
        cmds.xform(selection , ws=True, piv=(piv[0], piv[1], piv[2]) )#Align pivot to the z button pivot setting
    
def myFunction5(*args): #new!
    selection = cmds.ls(sl=True)
    for selected in selection:
        bounding_box = cmds.xform(selected, q=True, boundingBox=True, ws=True)
        xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
        
        cmds.move(bounding_box[2], [selected + ".scalePivot", selected + ".rotatePivot"], z=True, absolute=True)
        piv = cmds.xform (selected , piv=True, q=True, ws=True) 
        cmds.xform(selection , ws=True, piv=(piv[0], piv[1], piv[2]) )#Align pivot to the z button pivot setting

#widget setting
window_name = "slee3AlignPivot"

#check and reload the window
if cmds.window(window_name, q=True, exists=True):
    cmds.deleteUI(window_name)
    #delete old one and create new one 
    
my_window = cmds.window(window_name, title="slee3AlignPivot") #title is winodw name (on the top of the window)
cmds.window( window_name, edit=True, wh=(250,200))#resizing the size of window

#column layout
my_layout = cmds.columnLayout(parent=my_window, adj=True)

cmds.text(label="") 
cmds.text(label="Select object and") 
cmds.text(label="Choose Pivot location")
cmds.text(label="If you make a selection of objects,")
cmds.text(label="Automatically align the all pivots")
cmds.text(label="")
cmds.button(label="Center", command=myFunction4)
cmds.button(label="Bottom Center", command=myFunction5)
cmds.button(label="X", command=myFunction1) #create button on my window! 
cmds.button(label="Y", command=myFunction2)
cmds.button(label="Z", command=myFunction3)
cmds.text(label="") 
#also can uses it as the space between the other texts / useful / make it nice layout!
cmds.text(label="") 

cmds.showWindow(my_window)
