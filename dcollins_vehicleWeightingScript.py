"""
    Automatic joint weighting tool
    By: Dylan Collins
    
    Requires a hierarchy of joints with the following names:
        Main_Root
            Link_01
            B_L_Tire
            B_R_Tire
            F_L_Tire
            F_R_Tire
            B_L_Axle
            B_R_Axle
            F_L_Axle
            F_R_Axle
            Gun_Base
                Gun_Rotate
    
    Group all meshes under Entire_Vehicle
    Put meshes into groups within the Entire_Vehicle group matching the joint they should be bound to.
    For example, all meshes that should be attched to F_R_Tire should be in a group called F_R_Tire inside the Entire_Vehicle group.
    All meshes in Entire_Vehicle that aren't assigned a joint group are given a smooth bind.
    The script takes longer depending on the amount of separate objects making up the vehicle.
    Save a backup of the vehicle before running it through this script.
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import logging

checkNames = ["Link_01", "B_L_Tire", "B_R_Tire", "F_L_Tire", "F_R_Tire", "B_L_Axle", "B_R_Axle", "F_L_Axle", "F_R_Axle", "Gun_Base", "Main_Root"]

#puts joints in required order
for check in checkNames:
    checkJoint = cmds.ls(check, typ="joint")
    cmds.reorder(checkJoint, b=True)
    
mainRoot = cmds.ls("Main_Root", typ="joint")
jointsList = (cmds.listRelatives(mainRoot, c=True, path=True)) + mainRoot

"""
Temporarily rename joints to get group names
"""
for sel, name in zip(jointsList, checkNames):
    
    cmds.rename(sel, (name + "_temp"))

"""
Make selection sets for groups
"""
for check in checkNames:
    if check != "Link_01" and check != "Gun_Base":    #ignore Link_01 and Gun_Base when looking for groups
        if cmds.objExists(check):
            print "Found " + check
            meshSelection = cmds.ls(check, dag=True, typ="mesh")
            selectionSetName = (check + "Set")    #Add 'Set' to the end of each selection name (B_L_AxelSet)
            meshVertexCount = cmds.polyEvaluate(meshSelection, vertex=True)    #Get vertex count of each mesh
            for mesh in meshSelection:
                selVertex = mesh + ".vtx[0:"+str(meshVertexCount)+"]"    #Get all vertex names for selection
                cmds.sets(selVertex, n=selectionSetName)    #Create set from verticies
        else:
            print "Couldn't find " + check
            OpenMaya.MGlobal.displayError("Couldn't find group: " + check)
    else:
        print "Ignoring " + check

"""
Combine meshes and bind skin
"""
cmds.select("Entire_Vehicle")
combinedVehicle = cmds.polyUnite(ch=False)
totalVertexCount= cmds.polyEvaluate(combinedVehicle, vertex=True)    #get vertex count of combined vehicle
selTotalVertex = combinedVehicle[0] + ".vtx[0:"+str(totalVertexCount)+"]"
cmds.xform(combinedVehicle, rotatePivot=(0, 0, 0))
cmds.skinCluster("Main_Root_temp", combinedVehicle)    #make skin cluster for vehicle

cmds.skinPercent("skinCluster1", selTotalVertex, transformValue=("Main_Root_temp", 0.0))
#create smooth skin for axles
cmds.skinCluster("skinCluster1", e=True, inf="Main_Root_temp")
cmds.skinCluster("skinCluster1", e=True, inf="B_L_Axle_temp", dr=3.0)
cmds.skinCluster("skinCluster1", e=True, inf="B_R_Axle_temp", dr=3.0)
cmds.skinCluster("skinCluster1", e=True, inf="F_L_Axle_temp", dr=3.0)
cmds.skinCluster("skinCluster1", e=True, inf="F_R_Axle_temp", dr=3.0)
cmds.skinPercent("skinCluster1", "Main_RootSet", transformValue=("Main_Root_temp", 1.0))

"""
Weight mesh based on selection sets
"""
weightSets = cmds.ls("*Set*", sets=True)    #Select any sets in scene
for weightSel in weightSets:
    weightSelNoDigit = "".join(i for i in weightSel if not i.isdigit())
    weightSelNoSuffix = weightSelNoDigit.replace("Set", "")
    #Compares set names without suffix or numbers to check list
    if weightSelNoSuffix in checkNames:
        print ("Selecting " + weightSel)
        jointName = weightSelNoSuffix + "_temp"    #Get name of corresponding joint by removing "Set" from the end of the string
        print jointName
        cmds.skinPercent("skinCluster1", weightSel, transformValue=(jointName, 1.0))    #Set selection weight to 1 for corresponding vertex
    else:
        print "skipping"
        
"""
Get list of temp joint names
"""
mainRootTemp = cmds.ls("Main_Root_temp", typ="joint")
jointsListTemp = (cmds.listRelatives(mainRootTemp, c=True, path=True)) + mainRootTemp

"""
Change joints back to original names 
"""
for sel, name in zip(jointsListTemp, checkNames):
    
    cmds.rename(sel, name)
    
"""
Remove sets
"""
for weightSel in weightSets:
    weightSelNoDigit = "".join(i for i in weightSel if not i.isdigit())
    weightSelNoSuffix = weightSelNoDigit.replace("Set", "")
    #Compares set names without suffix or numbers to check list
    if weightSelNoSuffix in checkNames:
        print ("Selecting " + weightSel)
        cmds.delete(weightSel)
    else:
        print "skipping"
