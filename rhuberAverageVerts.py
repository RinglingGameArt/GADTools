"""
WIP. changed to Average Verts slider because cleanup was already being worked on by rbaker.
"""
import maya.cmds as cmds
if cmds.filterExpand(sm=31): #int 31 is the filter number for verts
    print "verts!"
else:
    print "poop"

#cmds.polyAverageVertex (i=10, ch=True)
