"""
    Automatically unwrap lightmap from existing UV set
    By: Dylan Collins
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

"""
Global Variables
"""
selection = cmds.ls(sl=True)
global layoutMapping
layoutMapping = 1
global preScale
preScale = 2
global shellLayout
shellLayout = 2
global layoutScale
layoutScale = 1
global layoutRotate
layoutRotate = 1

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
        global preScale
        percentageSpace = cmds.floatSliderGrp(self.shellSpacingSlider, q=True, v=True)    #get percentage space from slider
        
        self.currentMap = cmds.optionMenuGrp(self.uvSetChoice, q=True, v=True)
        cmds.polyCopyUV(self.selFace, cm=True, uvi=self.currentMap, uvs=self.inputLightmap)
        #cmds.polyMultiLayoutUV(psc=2, scale=1, rotateForBestFit=2, layout=2, ps=percentageSpace, uvs=self.inputLightmap) Default settings
        cmds.polyMultiLayoutUV(psc=preScale, scale=layoutScale, lm=layoutMapping, rotateForBestFit=layoutRotate, layout=shellLayout, ps=percentageSpace, uvs=self.inputLightmap)
        cmds.TextureViewWindow()    #opens uv texture editor
        cmds.select(self.sel)        #selects original objects to get out of face selection
        cmds.deleteUI(self.optionWindow)
        print preScale
        print shellLayout

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
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        
        standardLayout = cmds.columnLayout(parent=self.optionWindow, adj=True)
        self.uvSetChoice = cmds.optionMenuGrp(label="Source UV Set")
        for uvSet in self.uvList:    #lists selections' uv sets
            cmds.menuItem(label=uvSet)
        self.lightmapBox = cmds.textFieldGrp(label="New UV Set Name", text=self.lightmap)
        self.presetSelect = cmds.optionMenuGrp(self.presetSelect, label="Spacing Presets", cc=self.presetValue)
        for preset in self.spacingPresets:
            cmds.menuItem(label=preset)
        cmds.floatSliderGrp(self.shellSpacingSlider, label="Percentage Space:", v=3.200, step=0.001, max=5.000, field=True)
        print cmds.floatSliderGrp(self.shellSpacingSlider, q=True, v=True)
        cmds.button(label="Generate Lightmap", width=200, c=self.copyAndLayoutCheck)
        
        advancedLayout = cmds.columnLayout(parent=self.optionWindow, adj=True)
        
        layoutObjectsCollection = cmds.radioCollection()                        #radial button, creates new layout
        layoutObjectsCollection_layout = cmds.columnLayout()
        cmds.text(label = "Layout objects:", p=layoutObjectsCollection_layout)
        rbl = cmds.radioButton(label="Per object(overlapping)", p=layoutObjectsCollection_layout, onc=lambda *args: self.perObjectLayout(0))
        rbl = cmds.radioButton(label="Single or multiple objects(non-overlapping)", p=layoutObjectsCollection_layout, onc=lambda *args: self.perObjectLayout(1), sl=True )
                
        prescaleCollection = cmds.radioCollection()                        #radial button, creates new layout
        prescaleCollection_layout = cmds.columnLayout()
        cmds.text(label = "Prescale:", p=prescaleCollection_layout)
        rbl = cmds.radioButton(label="None", p=prescaleCollection_layout, onc=lambda *args: self.prescaleLayout(0))
        rbl = cmds.radioButton(label="Object", p=prescaleCollection_layout, onc=lambda *args: self.prescaleLayout(1))
        rbl = cmds.radioButton(label="World", p=prescaleCollection_layout, onc=lambda *args: self.prescaleLayout(2), sl=True)

        collection = cmds.radioCollection()                        #radial button, creates new layout
        collection_layout = cmds.columnLayout()
        cmds.text(label = "Shell Layout:", p=collection_layout)
        rbl = cmds.radioButton(label="Into region", p=collection_layout, onc=lambda *args: self.shellLayout(0), sl=True)
        rbl = cmds.radioButton(label="Along U", p=collection_layout, onc=lambda *args: self.shellLayout(1))
        rbl = cmds.radioButton(label="None", p=collection_layout, onc=lambda *args: self.shellLayout(2))
           
        collection = cmds.radioCollection()                        #radial button, creates new layout
        collection_layout = cmds.columnLayout()
        cmds.text(label = "Scale:", p=collection_layout)
        rbl = cmds.radioButton(label="None", p=collection_layout, onc=lambda *args: self.scaleLayout(0))
        rbl = cmds.radioButton(label="Uniform", p=collection_layout, onc=lambda *args: self.scaleLayout(1), sl=True)
        rbl = cmds.radioButton(label="Stretch", p=collection_layout, onc=lambda *args: self.scaleLayout(2))
        
        rotateCollection = cmds.radioCollection()                        #radial button, creates new layout
        rotateCollection_layout = cmds.columnLayout()
        cmds.text(label = "Rotate:", p=rotateCollection_layout)
        rbl = cmds.radioButton(label="None", p=rotateCollection_layout, onc=lambda *args: self.rotationLayout(0))
        rbl = cmds.radioButton(label="90 degrees", p=rotateCollection_layout, onc=lambda *args: self.rotationLayout(1), sl=True)
        rbl = cmds.radioButton(label="Free", p=rotateCollection_layout, onc=lambda *args: self.rotationLayout(2))
        
        cmds.tabLayout( tabs, edit=True, tabLabel=((standardLayout, 'General'), (advancedLayout, 'Advanced')) ) 
        
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
        
    def perObjectLayout(_ignoreme, layoutValue):
        global layoutMapping
        layoutMapping=layoutValue
        
    def prescaleLayout(_ignoreme, layoutValue):
        global preScale
        preScale=layoutValue

    def shellLayout(_ignoreme, layoutValue):
        global shellLayout
        shellLayout=layoutValue
        
    def scaleLayout(_ignoreme, layoutValue):
        global layoutScale
        layoutScale=layoutValue
        
    def rotationLayout(_ignoreme, layoutValue):
        global layoutRotate
        layoutRotate=layoutValue
  
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
