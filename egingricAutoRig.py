"""
    Builds a Vehicle Rig Based on your vehicle objects.
    Version 1.0
    By: Eric D. Gingrich
    
    Requirements:
        All objects that make up the entire vehicle in a group called "Entire_Vehicle" 
        
        (NOTE: For the weighting script you will also need to combine or group all objects that make up the chasis
        and name them "Main_Root" You might as well do this now).
        
        All objects that make up the individual wheels combined or grouped with the following names: 
            B_L_Tire
            B_R_Tire
            F_L_Tire
            F_R_Tire
        
        All objects that make up the individual brake drums or wishbones combined or grouped with the following names:
        (This part of the script puts a bone on the inside of the wishbone so that it can pivot from this spot. 
        If you have axles it won't pivot from this point, but the bone needs to go in roughly the same spot on the
        inside of the brake drum anyway).
            B_L_Axle
            B_R_Axle
            F_L_Axle
            F_R_Axle  
        
        The rest of the suspension can be named whatever you want, but just make sure it is under the 
        "Entire Vehicle" group.
"""
# Import Maya Commands
import maya.cmds as cmds

# Get vehicle chasis Main_Root rotation
# Check If Entire_Vehicle is pointing down positive X
# If pointing down positive x continue, 
# if not FIX and say "Vehicle not oriented down positive X... correcting."

# TO DO: This should probably be a looping function. I will firgure that out later.
# Get locations of vehicle objects so we can use them for the joint locations.
#Make sure pivot is centered
cmds.xform("Entire_Vehicle", centerPivots=True)
MainRootLoc = cmds.xform("Entire_Vehicle", query=True, worldSpace=True, rotatePivot=True)
print MainRootLoc


# For Link_01 we need to Determine the bounding box so we know where to put our pivot at the front of the vehicle
bounding_box = cmds.xform("Entire_Vehicle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
#Make sure pivot is centered
cmds.xform("Entire_Vehicle", centerPivots=True)
# move the pivot point in the Xmax direction to the front of the vehicle
cmds.move(xmax, ["Entire_Vehicle" + ".scalePivot","Entire_Vehicle" + ".rotatePivot"], x=True, absolute=True)
Link_01Loc = cmds.xform("Entire_Vehicle", query=True, worldSpace=True, rotatePivot=True)
print Link_01Loc



#Get tire locs.
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|B_L_Tire", centerPivots=True)
B_L_TireLoc = cmds.xform("Entire_Vehicle|B_L_Tire", query=True, worldSpace=True, rotatePivot=True)
print B_L_TireLoc


# For Gun_Rotate we need to Determine the bounding box so we know where to put our pivot at the top of the vehicle
bounding_box = cmds.xform("Entire_Vehicle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
#Make sure pivot is centered
cmds.xform("Entire_Vehicle", centerPivots=True)
# move the pivot point in the zmax direction to the top of the vehicle
cmds.move(zmax, ["Entire_Vehicle" + ".scalePivot","Entire_Vehicle" + ".rotatePivot"], z=True, absolute=True)
# now move the pivot point in x to the location of the back tires.
cmds.move(B_L_TireLoc[0], ["Entire_Vehicle" + ".scalePivot","Entire_Vehicle" + ".rotatePivot"], x=True, absolute=True)
Gun_RotateLoc = cmds.xform("Entire_Vehicle", query=True, worldSpace=True, rotatePivot=True)
print Gun_RotateLoc

# For Gun_Base put it halfway between Main_Root and Gun_Rotate with some math
Gun_BaseLoc = [Gun_RotateLoc[0] - (Gun_RotateLoc[0] / 2), 0, Gun_RotateLoc[2] - (MainRootLoc[2] / 2)]
print Gun_RotateLoc
print MainRootLoc
print Gun_BaseLoc

# Now that we have our loc info, move Entire_Vehicle pivot back to 0,0,0, just in case Unreal cares about such things
cmds.xform("Entire_Vehicle", centerPivots=True)
bounding_box = cmds.xform("Entire_Vehicle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
# move the pivot point in the zmin direction to the bottom of the vehicle
cmds.move(zmin, ["Entire_Vehicle" + ".scalePivot","Entire_Vehicle" + ".rotatePivot"], z=True, absolute=True)

#Make sure pivot is centered
cmds.xform("Entire_Vehicle|B_R_Tire", centerPivots=True)
B_R_TireLoc = cmds.xform("Entire_Vehicle|B_R_Tire", query=True, worldSpace=True, rotatePivot=True)
print B_R_TireLoc
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|F_L_Tire", centerPivots=True)
F_L_TireLoc = cmds.xform("Entire_Vehicle|F_L_Tire", query=True, worldSpace=True, rotatePivot=True)
print F_L_TireLoc
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|F_R_Tire", centerPivots=True)
F_R_TireLoc = cmds.xform("Entire_Vehicle|F_R_Tire", query=True, worldSpace=True, rotatePivot=True)
print F_R_TireLoc

#For the axles we want the joint to be on the inside, towards the center of the vehicle.
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|B_L_Axle", centerPivots=True)
# Determine the bounding box so we know where to put our pivot
bounding_box = cmds.xform("Entire_Vehicle|B_L_Axle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
# move the pivot point in the Ymin direction to the inside Y point
cmds.move(ymin, ["Entire_Vehicle|B_L_Axle" + ".scalePivot","Entire_Vehicle|B_L_Axle" + ".rotatePivot"], y=True, absolute=True)
B_L_AxleLoc = cmds.xform("Entire_Vehicle|B_L_Axle", query=True, worldSpace=True, rotatePivot=True)
print B_L_AxleLoc
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|B_R_Axle", centerPivots=True)
# Determine the bounding box so we know where to put our pivot
bounding_box = cmds.xform("Entire_Vehicle|B_R_Axle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
# move the pivot point in the Ymax direction to the inside Y point
cmds.move(ymax, ["Entire_Vehicle|B_R_Axle" + ".scalePivot","Entire_Vehicle|B_R_Axle" + ".rotatePivot"], y=True, absolute=True)
B_R_AxleLoc = cmds.xform("Entire_Vehicle|B_R_Axle", query=True, worldSpace=True, rotatePivot=True)
print B_R_AxleLoc
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|F_L_Axle", centerPivots=True)
# Determine the bounding box so we know where to put our pivot
bounding_box = cmds.xform("Entire_Vehicle|F_L_Axle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
# move the pivot point in the Ymin direction to the inside Y point
cmds.move(ymin, ["Entire_Vehicle|F_L_Axle" + ".scalePivot","Entire_Vehicle|F_L_Axle" + ".rotatePivot"], y=True, absolute=True)
F_L_AxleLoc = cmds.xform("Entire_Vehicle|F_L_Axle", query=True, worldSpace=True, rotatePivot=True)
print F_L_AxleLoc
#Make sure pivot is centered
cmds.xform("Entire_Vehicle|F_R_Axle", centerPivots=True)
# Determine the bounding box so we know where to put our pivot
bounding_box = cmds.xform("Entire_Vehicle|F_R_Axle", q=True, boundingBox=True, ws=True)
xmin, ymin, zmin, xmax, ymax, zmax = bounding_box
# move the pivot point in the Ymax direction to the inside Y point
cmds.move(ymax, ["Entire_Vehicle|F_R_Axle" + ".scalePivot","Entire_Vehicle|F_R_Axle" + ".rotatePivot"], y=True, absolute=True)
F_R_AxleLoc = cmds.xform("Entire_Vehicle|F_R_Axle", query=True, worldSpace=True, rotatePivot=True)
print F_R_AxleLoc

#Now we can create our joints.
# Delesect everything
cmds.select(deselect=True)

# Create Main_Root joint #############################
new_Joint = cmds.joint(position=(MainRootLoc))
# rename the new joint
cmds.rename(new_Joint, "Main_Root")
# Check to see if it got named correctly and if it didn't display a warning. 
# For example if there is already a joint named Main_Root it will name this one Man_Root1 which won't work in UDK.

# Create Link_01 joint
new_Joint = cmds.joint(position=(Link_01Loc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "Link_01")

#Create Tire Joints ###################################
#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create B_L_Tire joint
new_Joint = cmds.joint(position=(B_L_TireLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "B_L_Tire")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create B_R_Tire joint
new_Joint = cmds.joint(position=(B_R_TireLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "B_R_Tire")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create F_L_Tire joint
new_Joint = cmds.joint(position=(F_L_TireLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "F_L_Tire")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create F_R_Tire joint
new_Joint = cmds.joint(position=(F_R_TireLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "F_R_Tire")

#Create Axle Joints ##################################
#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create B_L_Axle joint
new_Joint = cmds.joint(position=(B_L_AxleLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "B_L_Axle")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create B_R_Axle joint
new_Joint = cmds.joint(position=(B_R_AxleLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "B_R_Axle")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create F_L_Axle joint
new_Joint = cmds.joint(position=(F_L_AxleLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "F_L_Axle")

#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create F_R_Axle joint
new_Joint = cmds.joint(position=(F_R_AxleLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "F_R_Axle")

#Create Gun Joints ######################################
#Go back up to Main_Root so next joint is child of it.
cmds.pickWalk(direction="up")
# Create Gun_Base joint
new_Joint = cmds.joint(position=(Gun_BaseLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "Gun_Base")

# Create Gun_Rotate joint as child of Gun_Rotate joint
new_Joint = cmds.joint(position=(Gun_RotateLoc))
cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="yup")
cmds.rename(new_Joint, "Gun_Rotate")
