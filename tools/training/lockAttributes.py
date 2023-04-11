import maya.cmds as cmds 


def lockAttributesFromSelection()->None:
    """lock the translate, rotation, scale attributes of the selected objects 
    attributeList       (str)   :   list of the attributes to lock 

    """

    #create a list from the selection 
    selectionList=cmds.ls(sl=True)

    attributeList = [
        "translateX", "rotateX", "scaleX",
        "translateY", "rotateY", "scaleY",
        "translateZ", "rotateZ", "scaleZ"
    ]

    # 2 combined loops, for each selected objects, loop a command that locks the attributes for each listed attributes 
    for i in selectionList: 

        for a in attributeList:

            #set the attribute to locked mode
            cmds.setAttr("%s.%s" % (i, a), lock=True)

#execute function
lockAttributesFromSelection()

