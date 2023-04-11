import maya.cmds as cmds

def matchTransformFromSelection()->None: 
    """Match the position, rotation, scale of the first selected object to the second object, if more than one object is selected, only works with the first 2 objects

    selectionList       (str)       :       "list of the selected objects /!\ activate the track selection in maya option order to get the expected result 

    
    """

    #create list from selection 
    selectionList = cmds.ls(sl=True)

    #maya command to match the atrributes of the first object to the second object 
    cmds.matchTransform(selectionList[0], selectionList[1])


#I created a alternative for the function to work with more than one object at the time 
def matchTransformAllSelectionToFirst()->None: 
    """Match the position, rotation, scale of all the selected objects to the first object selected 

    selectionList       (str)       :       "list of the selected objects /!\ activate the track selection in maya option order to get the expected result 

    
    """
    #create list from selection
    selectionList = cmds.ls(sl=True)


    index = 0
    #loop function wich match the transformation of all the objects to the first one 
    for i in selectionList: 

        if index > 0: 
            #maya command to match the atrributes of an object to another, here each object will be match to the first one 
            cmds.matchTransform(i, selectionList[0])
            index = index + 1 

        else : 
            index = index + 1

    
#call the function 
matchTransformFromSelection()

