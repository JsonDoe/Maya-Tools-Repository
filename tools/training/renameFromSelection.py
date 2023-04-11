import maya.cmds as cmds

def renameSelection(desiredName:str)-> None:
    """rename the selected objects with the same name and an incrementation

    desiredName     :   (str)   =   write the name you wish to give the selected elements

    
    """

    selectionList = cmds.ls(sl=True)

    #used to index the objects prperly
    index = 0

    #loop the function to rename each objects of the list 
    for i in selectionList:

        #maya function to rename 
        cmds.rename(i, "%s_%03d" % (desiredName, index))

        #update the index
        index= index+1

#Enter the name you wish to give the elements between (" ")
renameSelection("desiredName")
