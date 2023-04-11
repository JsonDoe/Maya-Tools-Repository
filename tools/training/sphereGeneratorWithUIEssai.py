#sphere generator.py 

from maya import cmds
import random 


#define rhe generation variable.
count       =100

baseName    ="TEMP"

rangeRadius =[0.5,2.0]
rangePosX   =[-100, 100]
rangePosY   =[-100, 100]
rangePosZ   =[-100, 100]
rangeRotX   =[-180, 180]
rangeRotY   =[-180, 180]
rangeRotZ   =[-180, 180]
scaleFactor =[0.5, 5]

def clean(baseName:str)->None: 
    """Clean the setup root if exist in the current scene.
    
    Args:
        baseName    (str) : The base name of the setup.
        
    Return:
        None
    """

    #search the setup root in the scene.
    root = cmds.ls("%s_root" % baseName)
    # Check if the object exist.
    if(len(root) > 0 ):
        cmds.delete(root[0])

clean(baseName)


def createRoot(baseName:str)-> str:
    """Create the setup root.
    
    Args:
        baseName    (str) : The base name of the setup.
        
    Return:
        str: The new root.
    """
    #create the setup root.
    return cmds.createNode("transform", n="%s_root" % baseName)

root = createRoot(baseName)

#create the sphere.
def createSphere(
    count:int,
    scaleFactor:list[float],
    baseName:str,
    root:str,
    rangeRadius:list[float],
    rangePosX:list[float],
    rangePosY:list[float],
    rangePosZ:list[float],
    rangeRotX:list[float],
    rangeRotY:list[float],
    rangeRotZ:list[float]
    ) -> None:

    """Generate the spheres..
    
    Args:

        count       (int)           : The count of spheres.
        baseName    (str)           : The base name of the setup.
        root        (str)           : The root setup.
        rangeRadius (list[float])   : The minimum and maximum radius.
        rangePosX   (list[float])   : The minimum and maximum position on axis X.
        rangePosY   (list[float])   : The minimum and maximum position on axis Y.
        rangePosZ   (list[float])   : The minimum and maximum position on axis Z.
        rangeRotX   (list[float])   : The minimum and maximum rotation on axis X.
        rangeRotY   (list[float])   : The minimum and maximum rotation on axis Y.
        rangeRotZ   (list[float])   : The minimum and maximum rotation on axis Z.
        
    Return:
        str: The new root.
    """

    for i in range(count):
        #define the sphere Name 
        sName = "%s_%04d" % (baseName, i)

        sphere = cmds.polySphere(n=sName, sx=10, sy=10, r=random.uniform(rangeRadius[0], rangeRadius[1]))

        #Parent the sphere to the setup root.
        cmds.parent(sName, root)

        #set the position
        cmds.setAttr("%s.translateX" % sName, random.uniform(rangePosX[0], rangePosX[1]))
        cmds.setAttr("%s.translateY" % sName, random.uniform(rangePosY[0], rangePosY[1]))
        cmds.setAttr("%s.translateZ" % sName, random.uniform(rangePosZ[0], rangePosZ[1]))

        #set the rotation 
        cmds.setAttr("%s.rotateX" % sName, random.uniform(rangeRotX[0], rangeRotX[1]))
        cmds.setAttr("%s.rotateY" % sName, random.uniform(rangeRotY[0], rangeRotY[1]))
        cmds.setAttr("%s.rotateZ" % sName, random.uniform(rangeRotZ[0], rangeRotZ[1]))

        cmds.setAttr("%s.scaleX" % sName, random.uniform(scaleFactor[0], scaleFactor[1]))
        cmds.setAttr("%s.scaleY" % sName, random.uniform(scaleFactor[0], scaleFactor[1]))
        cmds.setAttr("%s.scaleZ" % sName, random.uniform(scaleFactor[0], scaleFactor[1]))


def generateSpheres():

    clean(baseName)
    root = createRoot(baseName)
    createSphere(
    count,
    scaleFactor,
    baseName,
    root,
    rangeRadius,
    rangePosX,
    rangePosY,
    rangePosZ,
    rangeRotX,
    rangeRotY,
    rangeRotZ
    )



#*arg faire des recherches complémentaires, *arg permet de mettre autant d'arguments que l'ont veut et récupérer une liste
def click(*args): 
    """Execute the code when the button is clicked.   
    """


    #get the count.             queary ==> va chercher la valeur de cet attribut 
    count = cmds.intFieldGrp("count", q=True, value1=True )

    baseName = cmds.textFieldGrp("baseName", q=True, text=True)

    scaleFactor[0] = cmds.floatFieldGrp("scaleFactor", q=True, value1=True )
    scaleFactor[1] = cmds.floatFieldGrp("scaleFactor", q=True, value2=True )

    rangePosX[0] = cmds.floatFieldGrp("rangePosX", q=True, value1=True )
    rangePosX[1] = cmds.floatFieldGrp("rangePosX", q=True, value2=True )
    rangePosY[0] = cmds.floatFieldGrp("rangePosY", q=True, value1=True )
    rangePosY[1] = cmds.floatFieldGrp("rangePosY", q=True, value2=True )
    rangePosZ[0] = cmds.floatFieldGrp("rangePosZ", q=True, value1=True )
    rangePosZ[1] = cmds.floatFieldGrp("rangePosZ", q=True, value2=True )

    rangeRotX[0] = cmds.floatFieldGrp("rangeRotX", q=True, value1=True )
    rangeRotX[1] = cmds.floatFieldGrp("rangeRotX", q=True, value2=True )
    rangeRotY[0] = cmds.floatFieldGrp("rangeRotY", q=True, value1=True )
    rangeRotY[1] = cmds.floatFieldGrp("rangeRotY", q=True, value2=True )
    rangeRotZ[0] = cmds.floatFieldGrp("rangeRotZ", q=True, value1=True )
    rangeRotZ[1] = cmds.floatFieldGrp("rangeRotZ", q=True, value2=True )



    clean(baseName)
    root = createRoot(baseName)
    createSphere(
    count,
    scaleFactor,
    baseName,
    root,
    rangeRadius,
    rangePosX,
    rangePosY,
    rangePosZ,
    rangeRotX,
    rangeRotY,
    rangeRotZ
    )

"""
createSphere(
    count,
    baseName,
    root,
    rangeRadius,
    rangePosX,
    rangePosY,
    rangePosZ,
    rangeRotX,
    rangeRotY,
    rangeRotZ
    )
"""
#new window --> créer layout (espace dans lequel on ajoute des widgets(--> terme générique hors maya) (paramètres) --> pyQT, )

#ex widget int
#widget Float 
#widget bouton

#principe de return --> si on veut renvoyer une information 

#interface graphique 

"""
try and except : 

try --> essaye d'effectuer la fonction 

except --> si le try ne fonctionne pas --> effectue l'aaction suivante 

pousser documentation des fonctions on peut les utiliser pour faire plus 


cmds.window --> crée une fenêtre 

cmds.column --> équivalent de Qbox verticale, --> positionne des widgets dans la zone définie 



"""



def showUI(windowName):
    """ Display the user UI.

    Args:
        windowName      (str) : The name of the window.

    Returns:
        None
    """

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
    cmds.intFieldGrp("count", label="Count", numberOfFields=1 , value1=100, parent=mainLayout)

    cmds.floatFieldGrp("scaleFactor", label="Scale Factor", numberOfFields=2 , value1=0.5, value2=5, parent=mainLayout)

    cmds.textFieldGrp("baseName", label="Base Name", text="TEMP", parent=mainLayout)

    cmds.floatFieldGrp("rangePosX", label="Range Pos X", numberOfFields=2 , value1=-100, value2=100, parent=mainLayout)

    cmds.floatFieldGrp("rangePosY", label="Range Pos Y", numberOfFields=2 , value1=-100, value2=100, parent=mainLayout)

    cmds.floatFieldGrp("rangePosZ", label="Range Pos Z", numberOfFields=2 , value1=-100, value2=100, parent=mainLayout)

    cmds.floatFieldGrp("rangeRotX", label="Range Rot X", numberOfFields=2 , value1=-180, value2=180, parent=mainLayout)

    cmds.floatFieldGrp("rangeRotY", label="Range Rot Y", numberOfFields=2 , value1=-180, value2=180, parent=mainLayout)

    cmds.floatFieldGrp("rangeRotZ", label="Range Rot Z", numberOfFields=2 , value1=-180, value2=180, parent=mainLayout)

    #add the exe button      | ne pas mettre de parentèses pour que la fonction ne s'execute qu'au click 
    cmds.button("genereteSpheres", label="Generate Spheres", command=click)



    cmds.showWindow(mainWindow)

"""
count       =100

baseName    ="TEMP"

rangeRadius =[0.5,2.0]
rangePosX   =[-100, 100]
rangePosY   =[-100, 100]
rangePosZ   =[-100, 100]
rangeRotX   =[-180, 180]
rangeRotY   =[-180, 180]
rangeRotZ   =[-180, 180]

"""


showUI("sphereGenerator")


