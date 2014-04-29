"""
    Automatically unwrap lightmap from existing UV set
    By: Dylan Collins
    
    Use on any selected polyMesh 
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

"""
Global Variables
"""
selection = cmds.ls(sl=True)

"""
Functions
"""

class copyToLightmap():
    
#Select faces for each selected object and query if a lightmap uv already exists    
    def __init__(self):
        self.lightmap = "Lightmap"
        self.shellSpacingSlider = "shellSpacingSlider"
        self.spacingPresets = ["Custom", "2048 Map", "1024 Map", "512 Map", "256 Map", "128 Map", "64 Map", "32 Map"]
        self.spacingPresetValues = [3.2, .05, .1, .2, .4, .8, 1.6, 3.2]
        self.presetSelect = "presetSelect" 
        for self.sel in selection:
            print "test"
            cmds.select(self.sel)
            faceCount = cmds.polyEvaluate(self.sel, face=True)
            self.selFace = self.sel + ".f[0:"+str(faceCount)+"]"
            self.uvList = cmds.polyUVSet(self.selFace, q=True, auv=True)
            self.uvSetOptions()

    def copyAndLayoutCheck(self, none):
        #Query name entered for new lightmap
        self.inputLightmap = cmds.textFieldGrp(self.lightmapBox, q=True, text=True)
        
        #Checks to see if default uv set is being replaced
        if self.inputLightmap == "map1":
            OpenMaya.MGlobal.displayError("The default uv set cannot be replaced")
            return
            
        if self.inputLightmap in self.uvList:
            
            self.replaceWarningWindow()
            
        else:
            self.copyAndLayout()
                
#Copy uvs to new lightmap and layout with edge padding        
    def copyAndLayout(self):
        
        percentageSpace = cmds.floatSliderGrp(self.shellSpacingSlider, q=True, v=True)    #get percentage space from slider
        
        self.currentMap = cmds.optionMenuGrp(self.uvSetChoice, q=True, v=True)
        cmds.polyCopyUV(self.selFace, cm=True, uvi=self.currentMap, uvs=self.inputLightmap)
        cmds.polyMultiLayoutUV(psc=2, scale=1, rotateForBestFit=2, layout=2, ps=percentageSpace, uvs=self.inputLightmap)
        cmds.TextureViewWindow()    #opens uv texture editor
        cmds.select(self.sel)        #selects original objects to get out of face selection
        cmds.deleteUI(self.optionWindow)

#Delete lightmap if it already exists and then makes a new one        
    def replaceLightMap(self, none):
        self.currentMapCheck = cmds.optionMenuGrp(self.uvSetChoice, q=True, v=True)
        if self.inputLightmap == self.currentMapCheck:
            OpenMaya.MGlobal.displayError("Can't overwrite uv set of the same name.")
            cmds.deleteUI(self.replaceWindow)
        else:
            OpenMaya.MGlobal.displayInfo("Lightmap '" + self.inputLightmap + "' exists, overwriting")
            cmds.polyUVSet(self.selFace, uvs=self.inputLightmap, d=True)        #delete lightmap if already exists
            self.copyAndLayout()
            cmds.deleteUI(self.replaceWindow)
            
#Options menu
    def uvSetOptions(self):
        window_name = "uvSetOptions"
        if cmds.window(window_name, q=True, exists=True):
            cmds.deleteUI(window_name)
        self.optionWindow = cmds.window(window_name, title="Lightmap Options")
        layout = cmds.columnLayout(parent=self.optionWindow, adj=True)
        self.uvSetChoice = cmds.optionMenuGrp(label="Source UV Set")
        for uvSet in self.uvList:    #lists selections' uv sets
            cmds.menuItem(label=uvSet)
        self.lightmapBox = cmds.textFieldGrp(label="New UV Set Name", text=self.lightmap)
        self.presetSelect = cmds.optionMenuGrp(self.presetSelect, label="Spacing Presets", cc=self.presetValue)
        for preset in self.spacingPresets:
            cmds.menuItem(label=preset)
        cmds.floatSliderGrp(self.shellSpacingSlider, label="Spacing Amount:", v=3.200, step=0.001, max=5.000, field=True)
        print cmds.floatSliderGrp(self.shellSpacingSlider, q=True, v=True)
        cmds.button(label="Generate Lightmap", width=200, c=self.copyAndLayoutCheck)
        cmds.showWindow(self.optionWindow)

#Set percentage space slider based on value associated with spacing preset chosen        
    def presetValue(self, none):
        for preset, value in zip(self.spacingPresets, self.spacingPresetValues):
            presetSelectValue = cmds.optionMenuGrp(self.presetSelect, q=True, v=True)
            if preset == presetSelectValue:
                cmds.floatSliderGrp(self.shellSpacingSlider, edit=True, v=value)

#Window asking if the old lightmap should be replaced           
    def replaceWarningWindow(self):
        window_name = "replaceWindow"
        if cmds.window(window_name, q=True, exists=True):
            cmds.deleteUI(window_name)
        self.replaceWindow = cmds.window(window_name, title="Replace UV Set?")
        layout = cmds.rowColumnLayout(numberOfColumns=2, parent=self.replaceWindow)
        cmds.text(label=("Uv set '" + self.inputLightmap + "' already exists. Replace?"))
        cmds.text(label="")
        cmds.button(label="Yes", width=200, c=self.replaceLightMap)
        cmds.button(label="No", width=200, c=self.deleteReplaceWindow)
        cmds.text(label="")
        cmds.text(label="")
        cmds.showWindow(self.replaceWindow)
        
    def deleteReplaceWindow(self, none):
        cmds.deleteUI(self.replaceWindow)
        
#closes windows and ends script        
    def endScript(self, none):
        if cmds.window(self.optionWindow, q=True, exists=True):
            cmds.deleteUI(self.optionWindow)
        if cmds.window(self.replaceWindow, q=True, exists=True):
            cmds.deleteUI(self.replaceWindow)
        return
"""
Execute Script
"""    
#Checks if something is selected
if not selection:
    OpenMaya.MGlobal.displayWarning("Select an object")
else:
    copyToLightmap()
