import maya.cmds as cmds

class ToolBox:

    def __init__(self):

        #list of the desired groups
        self.hierarchyList   = ["asset_rig", "meshes_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP", "rig_GRP", "bones_GRP" ]

        #List of the objects to parent
        self.childList       = ["meshes_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP", "rig_GRP", "bones_GRP"]

        #list of the objects to parent the previously defined objects to 
        self.parentList      = ["asset_rig", "meshes_GRP","meshes_GRP","meshes_GRP","meshes_GRP", "asset_rig", "asset_rig"]

        #create list from maya selection
        self.selectionList = cmds.ls(sl=True)

        #list of the attributes to lock 
        self.attributeList = [
            "translateX", "rotateX", "scaleX",
            "translateY", "rotateY", "scaleY",
            "translateZ", "rotateZ", "scaleZ"
            ]




    def createHierarchy(self, desiredHierarchy:list[str])->None:
        """create the groups composing the hierarchy 

        hierarchyList   =   list(str) : list of the group names 

        """

        index=0
        for i in desiredHierarchy:

            cmds.group(em=True, n= i )

            index= index + 1

    def parentHierarchy(self, childList:list[str], parentList:list[str])->None:
        """Parent the hierarchy 

        childList       =   list(str) : list of the group to parent
        parentList      =   list(str) : list of the group to parent to 


        """

        index=0
        for i in childList:
            cmds.parent(i, parentList[index])
            index = index + 1




    def build(self, desiredHierarchy:list[str], childList:list[str], parentList:list[str], nspc:str=None)->None:
        """build the hierarchy defined in the lists 

        hierarchyList          list(str)    : list of the group names 

        childList               list(str)   : list of the group to parent
        parentList              list(str)   : list of the group to parent to 
        nspc                    (str)       : desired name of the namespace (OPTIONNAL)


        """

        self.createHierarchy(desiredHierarchy)
        self.parentHierarchy(childList, parentList)

        if nspc != None: 
            cmds.namespace(add=nspc)
            for i in desiredHierarchy:
                cmds.rename(i, "%s:%s" % (nspc, i))
        

    def buildDefinedHierarchy(self)->None:
        """build the hierarchy defined in the init lists 
        
        """

        self.build(self.hierarchyList, self.childList, self.parentList)



    def renameSelection(self, desiredName:str)-> None:
        """rename the selected objects with the same name and an incrementation

        desiredName     :   (str)   =   write the name you wish to give the selected elements


        """

        #used to index the objects prperly
        index = 0

        #loop the function to rename each objects of the list 
        for i in self.selectionList:

            #maya function to rename 
            cmds.rename(i, "%s_%03d" % (desiredName, index))

            #update the index
            index= index+1

    def matchTransformFromSelection(self)->None: 
        """Match the position, rotation, scale of the first selected object to the second object, if more than one object is selected, only works with the first 2 objects

        selectionList       (str)       :       "list of the selected objects /!\ activate the track selection in maya option order to get the expected result 


        """


        #maya command to match the atrributes of the first object to the second object 
        cmds.matchTransform(self.selectionList[0], self.selectionList[1])


    #I created a alternative for the function to work with more than one object at the time 
    def matchTransformAllSelectionToFirst(self)->None: 
        """Match the position, rotation, scale of all the selected objects to the first object selected 

        selectionList       (str)       :       "list of the selected objects /!\ activate the track selection in maya option order to get the expected result 


        """



        index = 0
        #loop function wich match the transformation of all the objects to the first one 
        for i in self.selectionList: 

            if index > 0: 
                #maya command to match the atrributes of an object to another, here each object will be match to the first one 
                cmds.matchTransform(i, self.selectionList[0])
                index = index + 1 

            else : 
                index = index + 1

    


    def lockAttributesFromSelection(self)->None:
        """lock the translate, rotation, scale attributes of the selected objects 
        attributeList       list[str]   :   list of the attributes to lock 

        """


        # 2 combined loops, for each selected objects, loop a command that locks the attributes for each listed attributes 
        for i in self.selectionList: 

            for a in self.attributeList:

                #set the attribute to locked mode
                cmds.setAttr("%s.%s" % (i, a), lock=True)




#remove the # of 2 sucessive tb lines to use the functions 

#code line to call the lockAttributesFromSelection function (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.lockAttributesFromSelection()

#code line to call the matchTransformFromSelection function (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.matchTransformFromSelection()

#code line to call the matchTransformAllSelectionToFirst function (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.matchTransformAllSelectionToFirst()

#code line to call the renameSelection function 
#Enter the name you wish to give the elements between (" ") , (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.renameSelection("desiredName")

#code line to call the buildDefinedHierarchy function (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.buildDefinedHierarchy()

#code line to call the build function using the lists defined in the init and adding a namespace, change "desiredNameSpace" to any name you want to give to the namespace (remove # on the 2 following lines to use)
#tb = ToolBox()
#tb.build(tb.hierarchyList, tb.childList, tb.parentList, "desiredNameSpace")

