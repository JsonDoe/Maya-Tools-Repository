import maya.cmds as cmds 

#list of the desired groups
hierarchyList   = ["asset_rig", "meshes_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP", "rig_GRP", "bones_GRP" ]

#List of the objects to parent
childList       = ["meshes_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP", "rig_GRP", "bones_GRP"]

#list of the objects to parent the previously defined objects to 
parentList      = ["asset_rig", "meshes_GRP","meshes_GRP","meshes_GRP","meshes_GRP", "asset_rig", "asset_rig"]

def createHierarchy(desiredHierarchy:list[str])->None:
    """create the groups composing the hierarchy 

    hierarchyList   =   list(str) : list of the group names 
    
    """

    index=0
    for i in desiredHierarchy:
         
        cmds.group(em=True, n= i )
        index= index + 1

def parentHierarchy(childList:list[str], parentList:list[str])->None:
    """Parent the hierarchy 

    childList       =   list(str) : list of the group to parent
    parentList      =   list(str) : list of the group to parent to 

    
    """

    index=0
    for i in childList:
        cmds.parent(i, parentList[index])
        index = index + 1

     
def build(desiredHierarchy:list[str], childList:list[str], parentList:list[str])->None:
    """build the hierarchy
    
    """

    createHierarchy(desiredHierarchy)
    parentHierarchy(childList, parentList)

#execute the command based on the previously defined hierarchy and parent/child Lists 
build(hierarchyList, childList, parentList)


