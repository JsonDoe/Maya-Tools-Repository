import maya.cmds as cmds

#Select one object than all the object you want to aim at the first

selectionList = cmds.ls( orderedSelection = True ) 

if len( selectionList ) >= 2 :
    
    targetName = selectionList[0]
    
    selectionList.remove( targetName ) 
    
    for objectName in selectionList: 
        
        
        cmds.aimConstraint( targetName, objectName, aimVector=[0,1,0] ) 
        
    
    
