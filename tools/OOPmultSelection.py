import maya.cmds as cmds

class MultTool:
    def __init__(self):
        """ INIT
        Args:
            self.sel         list[str] :  list from selection
            self.attrList    list[str] :  list all the attributes the script can affect

        Returns:
            None
        """
        self.sel= cmds.ls(sl=True)

        self.attrList = ["tx","ty","tz",
                         "rx","ry","rz",
                         "sx","sy","sz",                        
                        ]



    def clickRefresh(self, *args):
        """ refresh the selection list
        Args:
            self.sel         list[str] :  list from selection
        Returns:
            None
        """
        self.sel= cmds.ls(sl=True)

    def clickMultAdd(self, *args):
        """ refresh the selection list
        Args:
            multTx          float    :  Translate X muliplier (Get value from UI) 
            multTy          float    :  Translate Y muliplier (Get value from UI)
            multTz          float    :  Translate Z muliplier (Get value from UI)

            multRx          float    :  Rotation X muliplier (Get value from UI)
            multRy          float    :  Rotation Y muliplier (Get value from UI)
            multRz          float    :  Rotation Z muliplier (Get value from UI)

            multSx          float    :  Scale X muliplier (Get value from UI)
            multSy          float    :  Scale Y muliplier (Get value from UI)
            multSz          float    :  Scale Z muliplier (Get value from UI)

            addTx           float    :  Translate X value to add (Get value from UI)
            addTy           float    :  Translate Y value to add (Get value from UI)
            addTz           float    :  Translate Z value to add (Get value from UI)

            addRx           float    :  Rotation X value to add (Get value from UI)
            addRy           float    :  Rotation Y value to add (Get value from UI)
            addRz           float    :  Rotation Z value to add (Get value from UI)

            addSx           float    :  Scale X value to add (Get value from UI)
            addSy           float    :  Scale Y value to add (Get value from UI)
            addSz           float    :  Scale Z value to add (Get value from UI)

        Returns:
            None
        """

        multTx   =   cmds.floatFieldGrp("translateX", q=True, value1=True )
        addTx    =   cmds.floatFieldGrp("translateX", q=True, value2=True )
        multTy   =   cmds.floatFieldGrp("translateY", q=True, value1=True )
        addTy    =   cmds.floatFieldGrp("translateY", q=True, value2=True )   
        multTz   =   cmds.floatFieldGrp("translateZ", q=True, value1=True )
        addTz    =   cmds.floatFieldGrp("translateZ", q=True, value2=True )      

        multRx   =   cmds.floatFieldGrp("rotateX", q=True, value1=True )
        addRx    =   cmds.floatFieldGrp("rotateX", q=True, value2=True )
        multRy   =   cmds.floatFieldGrp("rotateY", q=True, value1=True )
        addRy    =   cmds.floatFieldGrp("rotateY", q=True, value2=True )   
        multRz   =   cmds.floatFieldGrp("rotateZ", q=True, value1=True )
        addRz    =   cmds.floatFieldGrp("rotateZ", q=True, value2=True )   

        multSx   =   cmds.floatFieldGrp("scaleX", q=True, value1=True )
        addSx    =   cmds.floatFieldGrp("scaleX", q=True, value2=True )
        multSy   =   cmds.floatFieldGrp("scaleY", q=True, value1=True )
        addSy    =   cmds.floatFieldGrp("scaleY", q=True, value2=True )   
        multSz   =   cmds.floatFieldGrp("scaleZ", q=True, value1=True )
        addSz    =   cmds.floatFieldGrp("scaleZ", q=True, value2=True )   

        multList= [     multTx,multTy,multTz,
                        multRx,multRy,multRz,
                        multSx,multSy,multSz
                    ]

        addList=  [     addTx,addTy,addTz,
                        addRx,addRy,addRz,
                        addSx,addSy,addSz
                    ]



        for item in self.sel:

            index=0

            for attrib in self.attrList:


                cmds.setAttr("%s.%s" % ( item, attrib ), ( (cmds.getAttr("%s.%s"% ( item, attrib ) ) * multList[index]) + addList[index]))
                index +=1
            



    def multAddUI(self):
        """ Display the multAdd tool UI.
        Args:
            windowName      (str) : The name of the window.
        Returns:
            None
        """

        windowName = "Multiply / Add value Tool"

        #Delete the window if already exist.
        try: 
            cmds.deleteUI(windowName)
        except:
            pass

        #Delete the window if already exist.
        mainWindow = cmds.window(windowName)
        #Create the main layout. 
        mainLayout = cmds.columnLayout("mainLayout")


        #create 2 fields for each attributes

        cmds.floatFieldGrp("translateX", label="multiply / add translate X", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("translateY", label="multiply / add translate Y", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("translateZ", label="multiply / add translate Z", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)

        cmds.floatFieldGrp("rotateX", label="multiply / add rotate X", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("rotateY", label="multiply / add rotate Y", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("rotateZ", label="multiply / add rotate Z", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)

        cmds.floatFieldGrp("scaleX", label="multiply / add scale X", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("scaleY", label="multiply / add scale Y", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)
        cmds.floatFieldGrp("scaleZ", label="multiply / add scale Z", numberOfFields=2 , value1=1, value2=0, parent=mainLayout)


        #add 2 buttons, one to execute function and one to refresh selection 
        cmds.button("refresh", label="Refresh Selection", command=self.clickRefresh)
        cmds.button("multAdd", label="Mult / Add Values", command=self.clickMultAdd)



        cmds.showWindow(mainWindow)

try1 = MultTool()
try1.multAddUI() 