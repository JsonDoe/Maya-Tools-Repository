from maya import cmds
from maya.api     import OpenMaya
from frankenstein import RigUtils
from frankenstein import RigObject
import math

#ToolBox class

class autoRigBasicProp: 

    def __init__(self):


        #define namespace 
        self.nspc = "namespace"

        self.index=0

        self.selectionIndex = 0

        self.colorDict ={ 
           "decimalRGB" : {
               "red"   : [255,0,0],
               "green" : [0,255,0],
               "blue"  : [0,0,255]  
           }
        }

        self.selected = cmds.ls(sl=True)

         
        #regarder comment loader un fichier JSON 
        self.meshModuleDict = { 
            
            "hierarchy" : ["asset_rig", "meshes_GRP", "rig_GRP", "bones_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP", "technical_LO_GRP", "technical_MI_GRP", "technical_HI_GRP"],

            "parentLists": {

                "childrens" : ["meshes_GRP", "rig_GRP", "bones_GRP", "HI_GRP", "MI_GRP", "LO_GRP", "Technical_GRP","technical_LO_GRP", "technical_MI_GRP", "technical_HI_GRP"], 

                "parents" : ["asset_rig", "asset_rig", "asset_rig", "meshes_GRP", "meshes_GRP", "meshes_GRP", "meshes_GRP","Technical_GRP","Technical_GRP","Technical_GRP"]

            }
        } 

        self.rigModuleDict = { 


                "hierarchy" : ["module" , "setup", "guid_GRP", "IK_GRP", "FK_GRP" , "controllers_GRP", "bones_GRP", "algo_GRP", "hidden_GRP"], 

                "parentLists" : {
                    
                    "setup" : {
                        "parent" : {
                            "parentName" : "module",
                            "cnsName" : "parent",
                            "offset" : True

                        },
                    },

                    "childrens" : ["setup", "guid_GRP", "IK_GRP", "FK_GRP" , "controllers_GRP", "bones_GRP", "algo_GRP", "hidden_GRP"],
                    "parents" : ["module", "module", "controllers_GRP", "controllers_GRP" , "module", "module", "module", "module"]
                
                }
            }

        self.props = {                 
        
                "hierarchy": ["parentAttach","module" , "controllers_GRP", "algo_GRP", "hidden_GRP"],

                "parentLists" : {

                    "childrens" : ["module", "controllers_GRP", "algo_GRP", "hidden_GRP","parentAttach", "global_CON", "local_CON" ],
                    "parents" : ["rig_GRP","module","module","module", "controllers_GRP", "parentAttach", "global_CON"]


                },

                "controllers": ["global_CON","local_CON"] ,

                "constraints" : {

                    "parent" :  {

                        "receivers" : [self.selected[self.selectionIndex]] ,

                        "targets" : ["local_CON"],

                        "names" : ["pC_GloProp_ALG"],

                        "offset" : [False]
                    },


                        "scale" : {
                            
                            
                            "receivers": [self.selected[self.selectionIndex]],

                            "targets" : ["local_CON"],

                            "names" : ["sC_GloProp_ALG"],

                            "offset" : [False]                            
    
                        }

                    }



                
        }
        
        self.noNspc = ":"


    def colorDisplay(self, bufferName:str, colorList, nspc:str=None)->None:

        """ Color a buffer.

        Args:
            bufferName      (str)           : The buffer name.
            colorList       list(float)     : the red color value.
            nspc            (str)           : the namespace name. (optinnal)
 

        Returns:
            None
        """

        if nspc==None:
            cmds.setAttr( f"{bufferName}" + ".useOutlinerColor" , True )
            cmds.setAttr( f"{bufferName}" + ".outlinerColor" , colorList[0],colorList[1],colorList[2])

        else:
            cmds.setAttr( f"{nspc}:{bufferName}" + ".useOutlinerColor" , True )
            cmds.setAttr( f"{nspc}:{bufferName}" + ".outlinerColor" , colorList[0],colorList[1],colorList[2])
        
    def renameSelected(self,nspc) -> None:
    
        """rename the selected object
        
        Args:
            nspc    (str)   : define the namespace Name.

        Returns:
            None
        
        """

        cmds.rename( self.selected[self.selectionIndex] , f":{nspc}:{self.selected[self.selectionIndex]}" )

    def matchTransform(self ,objectName:str, targetName:str, nspc:str=None)->None:
        """ Match the transformations of an object with a target.

        Args:
            objectName      (str)  : The joint name.
            targetName      (str)  : radius size value.
            nspc            (str)   : commune nameSpace (optionnal) 


        Returns:
            None
        """

        if nspc==None:
            cmds.matchTransform(f"{objectName}",f"{targetName}")

        else:
            cmds.matchTransform(f"{nspc}:{objectName}",f"{nspc}:{targetName}")


    def createNamespace(self, nspc) -> None:
        """create a namespace with the chosen name and set it as the curret namespace
        
        Args:
            nspc    (str)   : define the namespace Name.

        Returns:
            None
        
        """
        cmds.namespace( add=f"{nspc}")
        cmds.namespace( set=f"{nspc}")

    def setNamespaceToDefault(self) -> None:
        """set the namespace back to default 
        
        Args:
            None

        Returns:
            None
        
        """
        cmds.namespace( set=":")


    def frankStoreRestPose(self, name:str) -> None :

        """Store the restPose of an object via Frankenstein 
        
        Args:
            name    (str)   : The aimed object name.

        Returns:
            None
        
        """

        cmds.select(name)
        RigUtils().setNeutralPose2()
        cmds.select(clear=True)

        cmds.select(name)
        RigUtils().setNeutralPose2()
        cmds.select(clear=True)


    def createEmptyGroup(self, chosenName:str=None) -> None:
        """Create an Empty group with the option of giving it a name
        
        Args:
            chosenName    (str)   : The empty group object name. (optionnal)

        Returns:
            None        
        """
        if (chosenName==None):
            cmds.group(em=True)
            
        else: cmds.group( em=True, n=chosenName)
        
        

    def createPropsControllers(self , 
            gloShapeNum, gloColorList, gloTransNum, gloScaleNum, gloWidthNum,
            locShapeNum, locColorList, locTransNum, locScaleNum, locWidthNum
            ) -> None:

 

        """Create and name controllers for global and Local controllers
        
        Args:
            None

        Returns:
            None        
        """

        ru                  = RigUtils()
        ctrl                = ru.createRigController(gloShapeNum)
        ctrl.color          = OpenMaya.MColor([gloColorList[0], gloColorList[1], gloColorList[2], gloColorList[3]])
        ctrl.transparency   = gloTransNum
        ctrl.globalScale    = gloScaleNum
        ctrl.wireWidth      = gloWidthNum       
        ctrl.name           = "global_CON"


        ru                  = RigUtils()
        ctrl                = ru.createRigController(locShapeNum)
        ctrl.color          = OpenMaya.MColor([locColorList[0], locColorList[1], locColorList[2], locColorList[3]])
        ctrl.transparency   = locTransNum
        ctrl.globalScale    = locScaleNum
        ctrl.wireWidth      = locWidthNum  
        ctrl.name           = "local_CON"
        


    def loopCreateGroup(self, targetList) -> None: #voir comment ajouter un :type dict(containing a list) of str type  

        """Store the restPose of an object via Frankenstein 
        
        Args:
            name    (str)   : The aimed object name.

        Returns:
            None
        
        """
        for i in targetList: 
            self.createEmptyGroup(i)


    def createRigModule(self):
        """Store the restPose of an object via Frankenstein 
        
        Args:
            name    (str)   : The aimed object name.

        Returns:
            None
        
        """
        for i in self.rigModuleDict["hierarchy"]: 
            self.createEmptyGroup(i)


    def parentObjects(self,child:str,parent:str, nspc:str=None) -> None:
        """parent an object to another 
        
        Args:
            child     (str)       : The object to parent name.
            parent    (str)       : The parent name.
            nspc      (str)       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        if (nspc==None):
            cmds.parent(f"{child}",f"{parent}") 
            
        else:
            cmds.parent( f"{nspc}:{child}", f"{nspc}:{parent}") 


    def parentObjectsLoop(self, childList, parentList, nspc:str=None)-> None:

        """parent an object to another 
        
        Args:
            childList       list((str))         : The object to parent name.
            parentList      list((str))         : The parent name.
            nspc            (str)               : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        self.index = 0

        if nspc==None:
            for i in childList:
                

                self.parentObjects(childList[self.index], parentList[self.index])
                self.index = self.index + 1
        else:
            for i in childList:
                
                               
                self.parentObjects(childList[self.index], parentList[self.index], nspc)
                self.index = self.index + 1
        
        self.index = 0



    def parentHierarchy(self,nspc:str=None) -> None: #now no needed 
        #parent hierarchy properly than clear selection
        """parent an object to another 
        
        Args:
            child     (str)       : The object to parent name.
            parent    (str)       : The parent name.
            nspc      (str)       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """
        self.index = 0

        if nspc==None:
            for i in self.rigModuleDict["parentLists"]["childrens"]:
                

                self.parentObjects(self.rigModuleDict["parentLists"]["childrens"][self.index], self.rigModuleDict["parentLists"]["parents"][self.index])
                self.index = self.index + 1
        else:
            for i in self.rigModuleDict["parentLists"]["childrens"]:
                
                               
                self.parentObjects(self.rigModuleDict["parentLists"]["childrens"][self.index], self.rigModuleDict["parentLists"]["parents"][self.index], nspc)
                self.index = self.index + 1
        
        self.index = 0



    def parentPropsControllers(self, nspc:str=None) -> None:
            """parent props controllers 
            
            Args:
                nspc      (str)       : The nameSpace name. (optionnal)
    
            Returns:
                None
            
            """

            cmds.parent( f"{nspc}:local_CON" , f"{nspc}:global_CON" )
            cmds.parent( f"{nspc}:global_CON" , f"{nspc}:controllers_GRP" )

            cmds.matchTransform(f"{nspc}:global_CON",f"{nspc}:{self.selected[self.selectionIndex]}")


    def parentConstraint(self, receiver:str, target:str, consName:str , offset:bool , nspc:str=None ):

        """Apply a parent constraint  
        
        Args:
            receiver    (str)       : The name of the object receiving the parent constraint 

            target      (str)       : The name of the target leading the parent constraint 

            consName    (str)       : Name given to the constraint

            offset      (Bool)      : define if the maintain offset option is activated or not 

            nspc        (str)       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        if nspc ==None:

            cmds.parentConstraint( f"{target}", f"{receiver}", n=consName , mo=offset )               

        else:

            cmds.parentConstraint( f"{nspc}:{target}", f"{nspc}:{receiver}", n=consName , mo=offset )

    def parentConstraintLoop(self, receiverList, targetList, nameList, offsetList, nspc:str=None)-> None:

        """Apply a parent constraint  
        
        Args:
            receiverList    (list(str))       : The name of the object receiving the parent constraint 

            target          (list(str))       : The name of the target leading the parent constraint 

            consName        (list(str))       : Name given to the constraint

            offset          (list(Bool))      : define if the maintain offset option is activated or not 

            nameList        (list(str))       : define the name of the constraint

            nspc            (list(str))       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        self.index = 0

        if nspc==None:
            for i in receiverList:
                

                self.parentConstraint(receiverList[self.index], targetList[self.index], nameList[self.index], offsetList[self.index])
                self.index = self.index + 1
        else:
            for i in receiverList:
                
                print(self.index, receiverList[self.index], targetList[self.index], nameList[self.index], offsetList[self.index], nspc)        
                self.parentConstraint(receiverList[self.index], targetList[self.index], nameList[self.index], offsetList[self.index], nspc)
                self.index = self.index + 1
        
        self.index = 0


    def scaleConstraint(self, receiver:str, target:str, consName:str , offset:bool , nspc:str=None ):

        """Apply a scale constraint  
        
        Args:
            receiver    (str)       : The name of the object receiving the parent constraint 

            target      (str)       : The name of the target leading the parent constraint 

            consName    (str)       : Name given to the constraint

            offset      (Bool)      : define if the maintain offset option is activated or not 

            nspc        (str)       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        if nspc ==None:

            cmds.scaleConstraint( f"{target}", f"{receiver}", n=consName , mo=offset )               

        else:

            cmds.scaleConstraint( f"{nspc}:{target}", f"{nspc}:{receiver}", n=consName , mo=offset )

    def scaleConstraintLoop(self, receiverList:list[str], targetList, nameList, offsetList, nspc:str=None)-> None:

        """Apply a scale constraint  
        
        Args:
            receiverList    (list(str))       : The name of the object receiving the parent constraint 

            target          (list(str))       : The name of the target leading the parent constraint 

            consName        (list(str))       : Name given to the constraint

            offset          (list(Bool))      : define if the maintain offset option is activated or not 

            nameList        (list(str))       : define the name of the constraint

            nspc            (list(str))       : The nameSpace name. (optionnal)

        Returns:
            None
        
        """

        self.index = 0

        if nspc==None:
            for i in receiverList:
                

                self.scaleConstraint(receiverList[self.index], targetList[self.index], nameList[self.index], offsetList[self.index])
                self.index = self.index + 1
        else:
            for i in receiverList:
                
                               
                self.scaleConstraint(receiverList[self.index], targetList[self.index], nameList[self.index], offsetList[self.index], nspc)
                self.index = self.index + 1
        
        self.index = 0

    def clickRefresh(self, *args):
        """ refresh the selection list
        Args:
            self.sel         list[str] :  list from selection
        Returns:
            None
        """
        self.selected= cmds.ls(sl=True)        

    def autoRigProps(self,nspc,
            gloShapeNum, gloColorList, gloTransNum, gloScaleNum, gloWidthNum,
            locShapeNum, locColorList, locTransNum, locScaleNum, locWidthNum ) -> None:

        """Create a basic auto Rig on an Obj 
        
        Args:

            gloShapeNum     Float               : define the global controller's shape from the controller list 

            gloColorList    (list(float))       : define the global controller's colors with a list of numbers (RGBA) 

            gloTransNum     Float               : define the global controller's transparency

            gloScaleNum     Float               : define the global controller's scale

            gloWidthNum     Float               : define the global controller's shape width

            locShapeNum     Float               : define the local controller's shape from the controller list 

            locColorList    (list(float))       : define the local controller's colors with a list of numbers (RGBA) 

            locTransNum     Float               : define the local controller's transparency

            locScaleNum     Float               : define the local controller's scale

            locWidthNum     Float               : define the local controller's shape width

            nspc            (list(str))       : Define the namespace name. (optionnal)

        Returns:
            None
        
        """        

        selectionList = cmds.ls(sl=True)
        #add a center pivot

        self.createNamespace(nspc)    
        self.renameSelected(nspc)   
        self.loopCreateGroup(self.meshModuleDict["hierarchy"])
        self.parentObjectsLoop(self.meshModuleDict["parentLists"]["childrens"], self.meshModuleDict["parentLists"]["parents"] , nspc)
        self.createPropsControllers(            
            gloShapeNum, gloColorList, gloTransNum, gloScaleNum, gloWidthNum,
            locShapeNum, locColorList, locTransNum, locScaleNum, locWidthNum
            )
        self.loopCreateGroup(self.props["hierarchy"])
        self.parentObjectsLoop(self.props["parentLists"]["childrens"], self.props["parentLists"]["parents"] , nspc)

        
        for i in self.props["controllers"]:
            self.matchTransform(i, self.selected[self.selectionIndex], nspc) 
        
        self.parentConstraintLoop(selectionList, self.props["constraints"]["parent"]["targets"], self.props["constraints"]["parent"]["names"], self.props["constraints"]["parent"]["offset"], nspc)
        self.scaleConstraintLoop(selectionList, self.props["constraints"]["parent"]["targets"], self.props["constraints"]["scale"]["names"], self.props["constraints"]["parent"]["offset"], nspc)
        self.colorDisplay(self.props["hierarchy"][0], self.colorDict["decimalRGB"]["green"], nspc)
        self.parentObjects(self.selected[self.index], self.meshModuleDict["hierarchy"][5], nspc ) 
        self.parentObjects(self.props["constraints"]["parent"]["names"][self.index], self.props["hierarchy"][3], nspc )
        self.parentObjects(self.props["constraints"]["scale"]["names"][self.index], self.props["hierarchy"][3],nspc )
        self.setNamespaceToDefault()


    def UIPropClick(self, *args):
        """Create a basic auto Rig on an Obj 
        
        Args:

            gloShapeNum     Float               : define the global controller's shape from the controller list 

            gloColorList    (list(float))       : define the global controller's colors with a list of numbers (RGBA) 

            gloTransNum     Float               : define the global controller's transparency

            gloScaleNum     Float               : define the global controller's scale

            gloWidthNum     Float               : define the global controller's shape width

            locShapeNum     Float               : define the local controller's shape from the controller list 

            locColorList    (list(float))       : define the local controller's colors with a list of numbers (RGBA) 

            locTransNum     Float               : define the local controller's transparency

            locScaleNum     Float               : define the local controller's scale

            locWidthNum     Float               : define the local controller's shape width

            nspc            (list(str))       : Define the namespace name. (optionnal)

            (Get all data from UI)

        Returns:
            None
        
        """   

        gloColorList= [0,0,0,0]
        locColorList= [0,0,0,0]

        self.nspc       =   cmds.textFieldGrp("chosenNspc", q=True, text=True)
        gloShapeNum     =   cmds.intFieldGrp("propsControllersShapes", q=True, value1=True )

        gloColorList[0] =   cmds.floatFieldGrp("globalControllerColor", q=True, value1=True )
        gloColorList[1] =   cmds.floatFieldGrp("globalControllerColor", q=True, value2=True )
        gloColorList[2] =   cmds.floatFieldGrp("globalControllerColor", q=True, value3=True )
        gloColorList[3] =   cmds.floatFieldGrp("globalControllerColor", q=True, value4=True )



        gloTransNum     =   cmds.floatFieldGrp("propsControllersTransparency", q=True, value1=True )
        gloScaleNum     =   cmds.floatFieldGrp("propsControllersScale", q=True, value1=True )
        gloWidthNum     =   cmds.floatFieldGrp("propsControllersWireWidth", q=True, value1=True )



        locShapeNum     =    cmds.intFieldGrp("propsControllersShapes", q=True, value2=True )
        locColorList[0] =    cmds.floatFieldGrp("localControllerColor", q=True, value1=True )
        locColorList[1] =    cmds.floatFieldGrp("localControllerColor", q=True, value2=True )
        locColorList[2] =    cmds.floatFieldGrp("localControllerColor", q=True, value3=True )
        locColorList[3] =    cmds.floatFieldGrp("localControllerColor", q=True, value4=True )
        locTransNum     =    cmds.floatFieldGrp("propsControllersTransparency", q=True, value2=True )
        locScaleNum     =    cmds.floatFieldGrp("propsControllersScale", q=True, value2=True )
        locWidthNum     =    cmds.floatFieldGrp("propsControllersWireWidth", q=True, value2=True )



        self.autoRigProps(self.nspc,
            gloShapeNum, gloColorList, gloTransNum, gloScaleNum, gloWidthNum,
            locShapeNum, locColorList, locTransNum, locScaleNum, locWidthNum )

    def autoRigPropsUI(self):
        """ Display the user UI.
        Args:
            windowName      (str) : The name of the window.
        Returns:
            None
        """

        windowName = "Auto Rig Props UI"

        #Delete the window if already exist.
        try: 
            cmds.deleteUI(windowName)
        except:
            pass

        #Delete the window if already exist.
        mainWindow = cmds.window(windowName)
        #Create the main layout. 
        mainLayout = cmds.columnLayout("mainLayout")


        #Add the count widget. Le field définis le nombre de value qu'on peut insérer?~~

        cmds.intFieldGrp("propsControllersShapes", label="Props Controllers Shapes Numbers global/local", numberOfFields=2 , value1=8 , value2= 7, parent=mainLayout)

        cmds.floatFieldGrp("propsControllersTransparency", label="Props Controllers Transparency", numberOfFields=2 , value1=0, value2=0, parent=mainLayout)

        cmds.floatFieldGrp("propsControllersScale", label="Props Controllers Scale", numberOfFields=2 , value1=4.5, value2=2, parent=mainLayout)

        cmds.floatFieldGrp("propsControllersWireWidth", label="Props Controllers Wire Width", numberOfFields=2 , value1=2, value2=2, parent=mainLayout)

        cmds.floatFieldGrp("globalControllerColor", label="global Controller Color RGBA", numberOfFields=4 , value1=1, value2=0.984, value3=0, value4=1, parent=mainLayout)

        cmds.floatFieldGrp("localControllerColor", label="local Controller Color RGBA", numberOfFields=4 , value1=1, value2=0.396, value3=0, value4=1, parent=mainLayout)

        cmds.textFieldGrp("chosenNspc", label="Namespace:", text="nspc", parent=mainLayout)

        #add the exe button      | ne pas mettre de parentèses pour que la fonction ne s'execute qu'au click 
        cmds.button("refresh", label="Refresh Selection", command=self.clickRefresh)
        cmds.button("autoRigPropButton", label="Auto Rig Prop", command=self.UIPropClick)



        cmds.showWindow(mainWindow)
            


autoP = autoRigBasicProp()
autoP.autoRigPropsUI() 