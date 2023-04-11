import maya.cmds as cmds
import random

random.seed( 1234 )

#Define the desired parameters
desiredName= "mySphere"
desiredNumber=300
desiredX=200
desiredY=100
desiredZ=300
desiredRot=360
desiredMinScale=0.3
desiredMaxScale=5

#initiate index varible
index = 0

for i in range ( 0, desiredNumber ):
    
    #createPolySphere
    cmds.polySphere( n="%s_%03d" % ( desiredName , index ) )

    #Select the polySphere
    cmds.select("%s_%03d" % ( desiredName , index ) )


    #generate random values for x,y,z coordinates
    x = random.uniform( 0, desiredX)
    y = random.uniform( 0, desiredY)
    z = random.uniform( 0, desiredZ)

    #move the Sphere randomly via previously defined variables
    cmds.move( x, y ,z)

    #generate random values for x,y,z coordinates
    xRot = random.uniform( 0, desiredRot)
    yRot = random.uniform( 0, desiredRot)
    zRot = random.uniform( 0, desiredRot)   

    #Rotate
    cmds.rotate( xRot, yRot, zRot )   
    
    #generate random scaling value 
    scalingFactor = random.uniform( desiredMinScale, desiredMaxScale ) 


    #Scale
    cmds.scale( scalingFactor, scalingFactor, scalingFactor ) 


    #Create an aiStandardSurface and name it properly
    shader=cmds.shadingNode( 'aiStandardSurface', asShader=1, name='COLO_'+"%03d" % index )

    #define 3 random numbers for RGB values
    r = [random.random() for i in range (3)]

    #set Shader values with the previous random variable 
    cmds.setAttr( (shader + '.baseColor'), r[0], r[1], r[2], type='double3' )
    #select mesh
    cmds.select( "%s_%03d" % ( desiredName , index ))
    #Apply shader
    cmds.hyperShade(a=shader)





    #clear selection
    cmds.select( cl=True )

    #update Index
    index +=1 