#autoRigModuleAdvancedArmIKFK.py

import maya.cmds as cmds

#beforehand create "clavicle_GUID", "humerus_GUID", "radius_GUID", "wrist_GUID", "ikUpVectorArm_GUID", "armGuid_GRP", "humerus_FK_CON", 'hand_IK_CON', 'ikUpVectorArm_CON', 'clavicle_CON' , "referenceFinger_CON"

#initiate namespace variable 
nspc = "L_arm"

#initiate namespace
cmds.namespace( add=f"{nspc}")
cmds.namespace( set=f"{nspc}")


#creates FK controllers 
cmds.duplicate( "humerus_FK_CON", n="radius_FK_CON" )
cmds.duplicate( "humerus_FK_CON", n="wrist_FK_CON" )

#create hand controllers
cmds.duplicate( "referenceFinger_CON", n="metacarpalThumb_CON") 
cmds.duplicate( "referenceFinger_CON", n="thumb001_CON") 
cmds.duplicate( "referenceFinger_CON", n="thumb002_CON") 
 
cmds.duplicate( "referenceFinger_CON", n="metacarpalIndex_CON") 
cmds.duplicate( "referenceFinger_CON", n="index001_CON") 
cmds.duplicate( "referenceFinger_CON", n="index002_CON") 
cmds.duplicate( "referenceFinger_CON", n="index003_CON") 
 
cmds.duplicate( "referenceFinger_CON", n="metacarpalMajor_CON") 
cmds.duplicate( "referenceFinger_CON", n="major001_CON") 
cmds.duplicate( "referenceFinger_CON", n="major002_CON") 
cmds.duplicate( "referenceFinger_CON", n="major003_CON") 
 
cmds.duplicate( "referenceFinger_CON", n="metacarpalAnnular_CON") 
cmds.duplicate( "referenceFinger_CON", n="annular001_CON") 
cmds.duplicate( "referenceFinger_CON", n="annular002_CON") 
cmds.duplicate( "referenceFinger_CON", n="annular003_CON") 
 
cmds.duplicate( "referenceFinger_CON", n="metacarpalPinky_CON") 
cmds.duplicate( "referenceFinger_CON", n="pinky001_CON") 
cmds.duplicate( "referenceFinger_CON", n="pinky002_CON") 
cmds.duplicate( "referenceFinger_CON", n="pinky003_CON") 


#add _CON to namespace 
cmds.rename( 'hand_IK_CON', f":{nspc}:hand_IK_CON" )
cmds.rename( 'ikUpVectorArm_CON', f":{nspc}:upVector_IK_CON" )
cmds.rename( 'clavicle_CON', f":{nspc}:clavicle_CON" )

cmds.rename( 'humerus_FK_CON', f":{nspc}:humerus_FK_CON" )

#create groups
cmds.group( em=True, n="module")
cmds.group( em=True, n="setup_BUF")

cmds.group( em=True, n="controllers_GRP")
cmds.group( em=True, n="IK_GRP")
cmds.group( em=True, n="humerusRootAttach_BUF")
cmds.group( em=True, n="root_IK_BUF")
cmds.group( em=True, n="ikUpVector_parentAttach_BUF")
cmds.group( em=True, n="ikHand_parentAttach_BUF")
cmds.group( em=True, n="FK_GRP")
cmds.group( em=True, n="humerusFKAttach_BUF")
cmds.group( em=True, n="bones_GRP")
cmds.group( em=True, n="algo_GRP ")
cmds.group( em = True, n="hidden_GRP")
cmds.group( em=True , n="handParentAttach_BUF")
cmds.group( em=True, n="clavicle_parentAttach_BUF" )
cmds.group( em=True, n="clavicle_childAttach_BUF")

#color _BUF groups 
cmds.setAttr ( f"{nspc}:ikUpVector_parentAttach_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikUpVector_parentAttach_BUF " + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikHand_parentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikHand_parentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:clavicle_parentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:clavicle_parentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:humerusRootAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:humerusRootAttach_BUF" + ".outlinerColor" , 0,100,100)

cmds.setAttr ( f"{nspc}:handParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:handParentAttach_BUF" + ".outlinerColor" , 0,100,100)

cmds.setAttr ( f"{nspc}:humerusFKAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:humerusFKAttach_BUF" + ".outlinerColor" , 0,100,100)

cmds.setAttr ( f"{nspc}:setup_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:setup_BUF" + ".outlinerColor" , 255,87,51)

cmds.setAttr ( f"{nspc}:clavicle_childAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:clavicle_childAttach_BUF" + ".outlinerColor" , 255,0,0)




#create joints chains 
cmds.joint(n="clavicle_JNT", rad=0.5 )
cmds.joint(n="humerus", rad=0.5)
cmds.joint(n="radius", rad=0.5)
cmds.setAttr(f"{nspc}:radius.preferredAngleY", -90)
cmds.joint(n="wrist", rad=0.5)

#create IK joints
cmds.joint(n="humerus_IK_JNT", rad=0.2)
cmds.joint(n="radius_IK_JNT", rad=0.2)
cmds.setAttr(f"{nspc}:radius_IK_JNT.preferredAngleY", -90)
cmds.joint(n="wrist_IK_JNT", rad=0.2)

#create arm joints 
cmds.joint(n="metacarpalThumb_JNT", rad=0.15)
cmds.joint(n="thumb001_JNT", rad=0.15)
cmds.joint(n="thumb002_JNT", rad=0.15)
 
cmds.joint(n="metacarpalIndex_JNT", rad=0.15)
cmds.joint(n="index001_JNT", rad=0.15)
cmds.joint(n="index002_JNT", rad=0.15)
cmds.joint(n="index003_JNT", rad=0.15)
 
cmds.joint(n="metacarpalMajor_JNT", rad=0.15)
cmds.joint(n="major001_JNT", rad=0.15)
cmds.joint(n="major002_JNT", rad=0.15)
cmds.joint(n="major003_JNT", rad=0.15)
 
cmds.joint(n="metacarpalAnnular_JNT", rad=0.15)
cmds.joint(n="annular001_JNT", rad=0.15)
cmds.joint(n="annular002_JNT", rad=0.15)
cmds.joint(n="annular003_JNT", rad=0.15)
 
cmds.joint(n="metacarpalPinky_JNT", rad=0.15)
cmds.joint(n="pinky001_JNT", rad=0.15)
cmds.joint(n="pinky002_JNT", rad=0.15)
cmds.joint(n="pinky003_JNT", rad=0.15)


#Structure hierarchy 

#parent hand joints with joint group 
cmds.parent( f"{nspc}:metacarpalThumb_JNT", f"{nspc}:bones_GRP")
cmds.parent( f"{nspc}:metacarpalIndex_JNT", f"{nspc}:bones_GRP")
cmds.parent( f"{nspc}:metacarpalMajor_JNT", f"{nspc}:bones_GRP")
cmds.parent( f"{nspc}:metacarpalAnnular_JNT", f"{nspc}:bones_GRP")
cmds.parent( f"{nspc}:metacarpalPinky_JNT", f"{nspc}:bones_GRP")

#parent hand controllers together properly
cmds.parent( f"{nspc}:thumb001_CON", f"{nspc}:metacarpalThumb_CON")
cmds.parent( f"{nspc}:thumb002_CON", f"{nspc}:thumb001_CON")
 
cmds.parent( f"{nspc}:index001_CON", f"{nspc}:metacarpalIndex_CON")
cmds.parent( f"{nspc}:index002_CON", f"{nspc}:index001_CON")
cmds.parent( f"{nspc}:index003_CON", f"{nspc}:index002_CON")
 
cmds.parent( f"{nspc}:major001_CON", f"{nspc}:metacarpalMajor_CON")
cmds.parent( f"{nspc}:major002_CON", f"{nspc}:major001_CON")
cmds.parent( f"{nspc}:major003_CON", f"{nspc}:major002_CON")
 
cmds.parent( f"{nspc}:annular001_CON", f"{nspc}:metacarpalAnnular_CON")
cmds.parent( f"{nspc}:annular002_CON", f"{nspc}:annular001_CON")
cmds.parent( f"{nspc}:annular003_CON", f"{nspc}:annular002_CON")
 
cmds.parent( f"{nspc}:pinky001_CON", f"{nspc}:metacarpalPinky_CON")
cmds.parent( f"{nspc}:pinky002_CON", f"{nspc}:pinky001_CON")
cmds.parent( f"{nspc}:pinky003_CON", f"{nspc}:pinky002_CON")


# groups 
cmds.parent( f"{nspc}:setup_BUF" , f"{nspc}:module" )
cmds.parent( f"{nspc}:controllers_GRP" , f"{nspc}:module" )

cmds.parent( f"{nspc}:IK_GRP" , f"{nspc}:controllers_GRP" )
cmds.parent( f"{nspc}:humerusRootAttach_BUF" , f"{nspc}:IK_GRP" )
cmds.parent( f"{nspc}:root_IK_BUF" , f"{nspc}:humerusRootAttach_BUF" )

cmds.parent( f"{nspc}:ikUpVector_parentAttach_BUF" , f"{nspc}:IK_GRP" )
cmds.parent( f"{nspc}:ikHand_parentAttach_BUF" , f"{nspc}:IK_GRP" )
cmds.parent ( f"{nspc}:clavicle_childAttach_BUF", f"{nspc}:controllers_GRP" )


cmds.parent( f"{nspc}:bones_GRP" , f"{nspc}:module" )
cmds.parent( f"{nspc}:algo_GRP" , f"{nspc}:module" )
cmds.parent( f"{nspc}:hidden_GRP" , f"{nspc}:module" )

cmds.parent( f"{nspc}:hand_IK_CON" , f"{nspc}:ikHand_parentAttach_BUF" )
cmds.parent( f"{nspc}:upVector_IK_CON" , f"{nspc}:ikUpVector_parentAttach_BUF" )

cmds.parent( f"{nspc}:FK_GRP" , f"{nspc}:controllers_GRP" )

cmds.parent( f"{nspc}:humerusFKAttach_BUF", f"{nspc}:FK_GRP" )

cmds.parent( f"{nspc}:humerus_FK_CON" , f"{nspc}:humerusFKAttach_BUF" )
cmds.parent( f"{nspc}:radius_FK_CON" , f"{nspc}:humerus_FK_CON" )
cmds.parent( f"{nspc}:wrist_FK_CON" , f"{nspc}:radius_FK_CON" )

cmds.parent(f"{nspc}:handParentAttach_BUF" , f"{nspc}:controllers_GRP" )

cmds.parent(f"{nspc}:clavicle_parentAttach_BUF" , f"{nspc}:controllers_GRP" )
cmds.parent(f"{nspc}:clavicle_CON" , f"{nspc}:clavicle_parentAttach_BUF" )

cmds.parent(f"{nspc}:clavicle_JNT", f"{nspc}:bones_GRP")
cmds.parent(f"{nspc}:humerus_IK_JNT", f"{nspc}:algo_GRP")

#parent controllers with Hand Parent Attach buffer 
cmds.parent( f"{nspc}:metacarpalThumb_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalIndex_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalMajor_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalAnnular_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalPinky_CON", f"{nspc}:handParentAttach_BUF")

#match joints with the _GUID tools 

# SCRIPT ADDITION 03/06/2023 MATCH PARENT ATTACH AT THE REQUIRED SPACES 

cmds.matchTransform(f"{nspc}:ikHand_parentAttach_BUF", "wrist_GUID")
cmds.matchTransform(f"{nspc}:clavicle_parentAttach_BUF", "clavicle_GUID")
cmds.matchTransform(f"{nspc}:humerusRootAttach_BUF", "humerus_GUID")
cmds.matchTransform(f"{nspc}:handParentAttach_BUF", "wrist_GUID")
cmds.matchTransform(f"{nspc}:humerusFKAttach_BUF", "humerus_GUID")
cmds.matchTransform(f"{nspc}:clavicle_childAttach_BUF", "clavicle_GUID")


cmds.matchTransform(f"{nspc}:root_IK_BUF","humerus_GUID") 
cmds.matchTransform(f"{nspc}:clavicle_JNT","clavicle_GUID")



cmds.matchTransform(f"{nspc}:clavicle_CON","clavicle_GUID")
cmds.matchTransform(f"{nspc}:hand_IK_CON", "wrist_GUID")
cmds.matchTransform(f"{nspc}:upVector_IK_CON", "ikUpVectorArm_GUID")


cmds.matchTransform(f"{nspc}:humerus_IK_JNT","humerus_GUID")
cmds.matchTransform(f"{nspc}:radius_IK_JNT","radius_GUID")
cmds.matchTransform(f"{nspc}:wrist_IK_JNT","wrist_GUID")

cmds.matchTransform(f"{nspc}:humerus_FK_CON","humerus_GUID")
cmds.matchTransform(f"{nspc}:radius_FK_CON","radius_GUID")
cmds.matchTransform(f"{nspc}:wrist_FK_CON","wrist_GUID")







#select the setup
cmds.select( f"{nspc}:setup_BUF" )

#set the setup attributes /!\ I adjusted the values 
cmds.addAttr( at="float", ln="b1Length", nn="B1 Length", dv=4, k=True)
cmds.addAttr( at="float", ln="b2Length", nn="B2 Length", dv=4, k=True)

cmds.addAttr( at="float", ln="b1Scale", nn="B1 Scale", dv=1, k=True)
cmds.addAttr( at="float", ln="b2Scale", nn="B2 Scale", dv=1, k=True)

cmds.addAttr( at="float", ln="stretch", nn="Stretch", min=0, max=1, dv=0, k=True)

cmds.addAttr( at="float", ln="globalScale", nn="Global Scale", dv=1, k=True)

cmds.addAttr( at="float", ln="blendFKIK", nn="Blend FK <-> IK", min=0, max=1, dv=0, k=True)

cmds.addAttr( at="enum", ln="rigState", nn="Rig State", en="rig:Anim:" , dv=0, k=True)


#Lock and hide useless parameters in the channel box
cmds.setAttr( f"{nspc}:setup_BUF.tx", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.ty", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.tz", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.rx", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.ry", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.rz", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.sx", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.sy", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.sz", l=True , k=False , cb=False)
cmds.setAttr( f"{nspc}:setup_BUF.v", l=True , k=False , cb=False)

#clear selection
cmds.select( cl=True )

#create nodes to properly use setup settings 
#Bones scale/length and stretch factor 
#Multiply global scale by bone length 
cmds.shadingNode( "floatMath", au=True, n="B1GlobalScaled" )
cmds.setAttr( f"{nspc}:B1GlobalScaled.operation", 2 )
cmds.connectAttr( f"{nspc}:setup_BUF.b1Length", f"{nspc}:B1GlobalScaled.floatA" )
cmds.connectAttr( f"{nspc}:setup_BUF.globalScale", f"{nspc}:B1GlobalScaled.floatB" )

cmds.shadingNode( "floatMath", au=True, n="B2GlobalScaled" )
cmds.setAttr( f"{nspc}:B2GlobalScaled.operation", 2 )
cmds.connectAttr( f"{nspc}:setup_BUF.b2Length", f"{nspc}:B2GlobalScaled.floatA" )
cmds.connectAttr( f"{nspc}:setup_BUF.globalScale", f"{nspc}:B2GlobalScaled.floatB" )

#multiply outfloat by bone scale 
cmds.shadingNode( "floatMath", au=True, n="B1Scaled" )
cmds.setAttr( f"{nspc}:B1Scaled.operation", 2 )
cmds.connectAttr( f"{nspc}:B1GlobalScaled.outFloat", f"{nspc}:B1Scaled.floatA" )
cmds.connectAttr( f"{nspc}:setup_BUF.b1Scale", f"{nspc}:B1Scaled.floatB" )

cmds.shadingNode( "floatMath", au=True, n="B2Scaled" )
cmds.setAttr( f"{nspc}:B2Scaled.operation", 2 )
cmds.connectAttr( f"{nspc}:B2GlobalScaled.outFloat", f"{nspc}:B2Scaled.floatA" )
cmds.connectAttr( f"{nspc}:setup_BUF.b2Scale", f"{nspc}:B2Scaled.floatB" )


#create floatMath that add both outFloat values 
cmds.shadingNode( "floatMath", au=True, n="maxChainLength" )
cmds.setAttr( f"{nspc}:maxChainLength.operation", 0 )
cmds.connectAttr( f"{nspc}:B1Scaled.outFloat", f"{nspc}:maxChainLength.floatA" )
cmds.connectAttr( f"{nspc}:B2Scaled.outFloat", f"{nspc}:maxChainLength.floatB" )

# create and connect root_IK and hand_IK worldMatrix to distanceBetween inMatrix
cmds.shadingNode( "distanceBetween", au=True, n="ikLength" )

cmds.connectAttr( f"{nspc}:root_IK_BUF.worldMatrix", f"{nspc}:ikLength.inMatrix1" )
cmds.connectAttr( f"{nspc}:hand_IK_CON.worldMatrix", f"{nspc}:ikLength.inMatrix2" )

#divide ikLength by maxChainLength
cmds.shadingNode( "floatMath", au=True, n="stretchFactor")
cmds.setAttr( f"{nspc}:stretchFactor.operation", 3 )
cmds.connectAttr( f"{nspc}:maxChainLength.outFloat", f"{nspc}:stretchFactor.floatB" )

#creates float logic verifying if ikLength is > than the maxChainLength
cmds.shadingNode( "floatLogic", au=True, n="ifGreaterThanMaxLength")
cmds.setAttr( f"{nspc}:ifGreaterThanMaxLength.operation", 3 )
cmds.connectAttr( f"{nspc}:maxChainLength.outFloat", f"{nspc}:ifGreaterThanMaxLength.floatB" )

#creates setRange with min X at 1
cmds.shadingNode( "setRange", au=True, n="activateStretch")
cmds.setAttr( f"{nspc}:activateStretch.minX", 1 ) #I seted the value 
cmds.setAttr( f"{nspc}:activateStretch.oldMaxX", 1 ) #I seted the value 

cmds.connectAttr( f"{nspc}:stretchFactor.outFloat", f"{nspc}:activateStretch.maxX" )
cmds.connectAttr( f"{nspc}:setup_BUF.stretch", f"{nspc}:activateStretch.valueX" )

#create float condition verifying if we activate stretch or not 
cmds.shadingNode( "floatCondition", au=True, n="useStretchFactorORNeutralFactor")
cmds.setAttr( f"{nspc}:useStretchFactorORNeutralFactor.floatB", 1 ) 
cmds.connectAttr( f"{nspc}:ifGreaterThanMaxLength.outBool", f"{nspc}:useStretchFactorORNeutralFactor.condition" )
cmds.connectAttr( f"{nspc}:activateStretch.outValueX", f"{nspc}:useStretchFactorORNeutralFactor.floatA" )

#create nodes to multiply values 
cmds.shadingNode( "floatMath", au=True, n="B1Stretched")
cmds.setAttr( f"{nspc}:B1Stretched.operation", 2 ) 
cmds.connectAttr( f"{nspc}:B1Scaled.outFloat", f"{nspc}:B1Stretched.floatA" )
cmds.connectAttr( f"{nspc}:useStretchFactorORNeutralFactor.outFloat", f"{nspc}:B1Stretched.floatB" )

cmds.shadingNode( "floatMath", au=True, n="B2Stretched")
cmds.setAttr( f"{nspc}:B2Stretched.operation", 2 ) 
cmds.connectAttr( f"{nspc}:B2Scaled.outFloat", f"{nspc}:B2Stretched.floatA" )
cmds.connectAttr( f"{nspc}:useStretchFactorORNeutralFactor.outFloat", f"{nspc}:B2Stretched.floatB" )

#connects the outFloat to the joints transX to apply effect 
cmds.connectAttr( f"{nspc}:B1Stretched.outFloat", f"{nspc}:radius_IK_JNT.translateX" )
cmds.connectAttr( f"{nspc}:B2Stretched.outFloat", f"{nspc}:wrist_IK_JNT.translateX" )
#verified


#FKIK switch 

#Humerus nodes and connection setup 
cmds.shadingNode( "blendMatrix", au=True, n="humerusBlendFKIK")
cmds.connectAttr( f"{nspc}:setup_BUF.blendFKIK", f"{nspc}:humerusBlendFKIK.envelope" )
cmds.connectAttr( f"{nspc}:humerus_IK_JNT.worldMatrix[0]", f"{nspc}:humerusBlendFKIK.target[0].targetMatrix" )
cmds.connectAttr( f"{nspc}:humerus_FK_CON.worldMatrix[0]", f"{nspc}:humerusBlendFKIK.inputMatrix" )

cmds.shadingNode( "multMatrix", au=True, n="humerusLocalMatrix")
cmds.connectAttr( f"{nspc}:humerusBlendFKIK.outputMatrix", f"{nspc}:humerusLocalMatrix.matrixIn[0]" )
cmds.connectAttr( f"{nspc}:clavicle_JNT.worldInverseMatrix[0]", f"{nspc}:humerusLocalMatrix.matrixIn[1]" )  #doesn't work, correct it 

cmds.connectAttr( f"{nspc}:humerusLocalMatrix.matrixSum", f"{nspc}:humerus.offsetParentMatrix" )

#radius nodes and connection setup 
cmds.shadingNode( "multMatrix", au=True, n="radiusFKFullLocalMatrix") 
cmds.connectAttr( f"{nspc}:radius_FK_CON.matrix", f"{nspc}:radiusFKFullLocalMatrix.matrixIn[0]" )
cmds.connectAttr( f"{nspc}:radius_FK_CON.offsetParentMatrix", f"{nspc}:radiusFKFullLocalMatrix.matrixIn[1]" )

cmds.shadingNode( "blendMatrix", au=True, n="radiusBlendFKIK")
cmds.connectAttr( f"{nspc}:setup_BUF.blendFKIK", f"{nspc}:radiusBlendFKIK.envelope" )
cmds.connectAttr( f"{nspc}:radius_IK_JNT.matrix", f"{nspc}:radiusBlendFKIK.target[0].targetMatrix" )
cmds.connectAttr( f"{nspc}:radiusFKFullLocalMatrix.matrixSum", f"{nspc}:radiusBlendFKIK.inputMatrix" )

cmds.connectAttr( f"{nspc}:radiusBlendFKIK.outputMatrix", f"{nspc}:radius.offsetParentMatrix" )

#wrist nodes and connection setup 
cmds.shadingNode( "multMatrix", au=True, n="wristFKFullLocalMatrix")
cmds.connectAttr( f"{nspc}:wrist_FK_CON.matrix", f"{nspc}:wristFKFullLocalMatrix.matrixIn[0]" )
cmds.connectAttr( f"{nspc}:wrist_FK_CON.offsetParentMatrix", f"{nspc}:wristFKFullLocalMatrix.matrixIn[1]" )

cmds.shadingNode( "blendMatrix", au=True, n="wristBlendFKIK")
cmds.connectAttr( f"{nspc}:setup_BUF.blendFKIK", f"{nspc}:wristBlendFKIK.envelope" )
cmds.connectAttr( f"{nspc}:wrist_IK_JNT.matrix", f"{nspc}:wristBlendFKIK.target[0].targetMatrix" )
cmds.connectAttr( f"{nspc}:wristFKFullLocalMatrix.matrixSum", f"{nspc}:wristBlendFKIK.inputMatrix" )

cmds.connectAttr( f"{nspc}:wristBlendFKIK.outputMatrix", f"{nspc}:wrist.offsetParentMatrix" )
#verified


#Shape visibility 
#Create node that verify the entering value
cmds.shadingNode( "floatLogic", au=True, n="rigStateTest")
cmds.setAttr( f"{nspc}:rigStateTest.operation", 0 ) 
cmds.setAttr( f"{nspc}:rigStateTest.floatB", 0 ) 
cmds.connectAttr( f"{nspc}:setup_BUF.rigState", f"{nspc}:rigStateTest.floatA" )

#create floatCondition 
cmds.shadingNode( "floatCondition", au=True, n="rigStateValue")
cmds.setAttr( f"{nspc}:rigStateValue.floatA", 0.5 ) 
cmds.connectAttr( f"{nspc}:rigStateTest.outBool", f"{nspc}:rigStateValue.condition" )
cmds.connectAttr( f"{nspc}:setup_BUF.blendFKIK", f"{nspc}:rigStateValue.floatB" )

# node filtering FK display depending on the previous value 
cmds.shadingNode( "floatLogic", au=True, n="displayFKControllers")
cmds.setAttr( f"{nspc}:displayFKControllers.operation", 1 ) 
cmds.setAttr( f"{nspc}:displayFKControllers.floatB", 1 ) 
cmds.connectAttr( f"{nspc}:rigStateValue.outFloat", f"{nspc}:displayFKControllers.floatA" )

# node filtering IK display depending on the previous value 
cmds.shadingNode( "floatLogic", au=True, n="displayIKControllers")
cmds.setAttr( f"{nspc}:displayIKControllers.operation", 1 ) 
cmds.setAttr( f"{nspc}:displayIKControllers.floatB", 0 ) 
cmds.connectAttr( f"{nspc}:rigStateValue.outFloat", f"{nspc}:displayIKControllers.floatA" )

# Connect display outBool to controllers shapes 
cmds.connectAttr( f"{nspc}:displayFKControllers.outBool", f"{nspc}:radius_FK_CONShape.visibility" )
cmds.connectAttr( f"{nspc}:displayFKControllers.outBool", f"{nspc}:wrist_FK_CONShape.visibility" )
cmds.connectAttr( f"{nspc}:displayFKControllers.outBool", f"{nspc}:humerus_FK_CONShape.visibility" )

cmds.connectAttr( f"{nspc}:displayIKControllers.outBool", f"{nspc}:hand_IK_CONShape.visibility" )
cmds.connectAttr( f"{nspc}:displayIKControllers.outBool", f"{nspc}:upVector_IK_CONShape.visibility" )

#script ADDITION 03/06/2023

cmds.shadingNode("decomposeMatrix", au=True, n="getClavicleScale")

cmds.shadingNode("floatMath", au=True, n="divideByGlobalScale")
cmds.setAttr( f"{nspc}:divideByGlobalScale.operation", 3 ) 

cmds.connectAttr( f"{nspc}:clavicle_CON.worldMatrix[0]", f"{nspc}:getClavicleScale.inputMatrix" )

cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:humerus.scale" )
cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:radius.scale" )
cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:wrist.scale" )

cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:humerus_IK_JNT.scale" )
cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:radius_IK_JNT.scale" )
cmds.connectAttr( f"{nspc}:getClavicleScale.outputScale", f"{nspc}:wrist_IK_JNT.scale" )

cmds.connectAttr( f"{nspc}:ikLength.distance", f"{nspc}:divideByGlobalScale.floatA" )
cmds.connectAttr( f"{nspc}:getClavicleScale.outputScaleX", f"{nspc}:divideByGlobalScale.floatB" )


cmds.connectAttr( f"{nspc}:divideByGlobalScale.outFloat", f"{nspc}:stretchFactor.floatA" )
cmds.connectAttr( f"{nspc}:divideByGlobalScale.outFloat", f"{nspc}:ifGreaterThanMaxLength.floatA" )

#additionnal constraints based on classes module

cmds.parentConstraint(f"{nspc}:clavicle_CON", f"{nspc}:clavicle_JNT", mo=False) 

cmds.parentConstraint(f"{nspc}:clavicle_CON", f"{nspc}:humerusRootAttach_BUF", mo=True) 

cmds.parentConstraint(f"{nspc}:clavicle_CON", f"{nspc}:humerusFKAttach_BUF", mo=True) 

cmds.pointConstraint(f"{nspc}:root_IK_BUF", f"{nspc}:humerus_IK_JNT", mo=False) 

cmds.orientConstraint(f"{nspc}:hand_IK_CON", f"{nspc}:wrist_IK_JNT", mo=False) 


#create the clavicle/ikHand constraints.
#cmds.orientConstraint(f"{nspc}:clavicle_CON", f"{nspc}:clavicle_JNT", mo=True) 
cmds.ikHandle( sj=f"{nspc}:humerus_IK_JNT", ee=f"{nspc}:wrist_IK_JNT", p=1, w=1, pw=1, n="ikHandleHumerusWrist" )

cmds.pointConstraint(f"{nspc}:hand_IK_CON", f"{nspc}:ikHandleHumerusWrist", mo=False) 
cmds.poleVectorConstraint( f"{nspc}:upVector_IK_CON", f"{nspc}:ikHandleHumerusWrist" ) 
#add orient constraint to the hand parentAttach
cmds.orientConstraint(f"{nspc}:hand_IK_CON", f"{nspc}:wrist_IK_JNT", mo=False, n="orientConstrainthandIKWrist") 


cmds.parent( f"{nspc}:ikHandleHumerusWrist", f"{nspc}:hidden_GRP" )

#create constraints for handParentAttach_BUF
cmds.pointConstraint(f"{nspc}:wrist", f"{nspc}:handParentAttach_BUF", mo=False, n="pointConstraintWrist")
cmds.orientConstraint( f"{nspc}:wrist", f"{nspc}:handParentAttach_BUF",mo=False, n="orientConstraintIkHand" )
 
#place constraints in the right file 
cmds.parent(f"{nspc}:pointConstraintWrist", f"{nspc}:hidden_GRP")
cmds.parent(f"{nspc}:orientConstraintIkHand", f"{nspc}:hidden_GRP")

#match joints with the _GUID tools 
cmds.matchTransform(f"{nspc}:metacarpalThumb_JNT","metacarpalThumb_GUID")
cmds.matchTransform(f"{nspc}:thumb001_JNT","thumb001_GUID")
cmds.matchTransform(f"{nspc}:thumb002_JNT","thumb002_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalIndex_JNT","metacarpalIndex_GUID")
cmds.matchTransform(f"{nspc}:index001_JNT","index001_GUID")
cmds.matchTransform(f"{nspc}:index002_JNT","index002_GUID")
cmds.matchTransform(f"{nspc}:index003_JNT","index003_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalMajor_JNT","metacarpalMajor_GUID")
cmds.matchTransform(f"{nspc}:major001_JNT","major001_GUID")
cmds.matchTransform(f"{nspc}:major002_JNT","major002_GUID")
cmds.matchTransform(f"{nspc}:major003_JNT","major003_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalAnnular_JNT","metacarpalAnnular_GUID")
cmds.matchTransform(f"{nspc}:annular001_JNT","annular001_GUID")
cmds.matchTransform(f"{nspc}:annular002_JNT","annular002_GUID")
cmds.matchTransform(f"{nspc}:annular002_JNT","annular002_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalPinky_JNT","metacarpalPinky_GUID")
cmds.matchTransform(f"{nspc}:pinky001_JNT","pinky001_GUID")
cmds.matchTransform(f"{nspc}:pinky002_JNT","pinky002_GUID")
cmds.matchTransform(f"{nspc}:pinky002_JNT","pinky002_GUID")
 
 
#match _CON with the _GUID tools 
cmds.matchTransform(f"{nspc}:metacarpalThumb_CON","metacarpalThumb_GUID")
cmds.matchTransform(f"{nspc}:thumb001_CON","thumb001_GUID")
cmds.matchTransform(f"{nspc}:thumb002_CON","thumb002_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalIndex_CON","metacarpalIndex_GUID")
cmds.matchTransform(f"{nspc}:index001_CON","index001_GUID")
cmds.matchTransform(f"{nspc}:index002_CON","index002_GUID")
cmds.matchTransform(f"{nspc}:index003_CON","index003_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalMajor_CON","metacarpalMajor_GUID")
cmds.matchTransform(f"{nspc}:major001_CON","major001_GUID")
cmds.matchTransform(f"{nspc}:major002_CON","major002_GUID")
cmds.matchTransform(f"{nspc}:major003_CON","major003_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalAnnular_CON","metacarpalAnnular_GUID")
cmds.matchTransform(f"{nspc}:annular001_CON","annular001_GUID")
cmds.matchTransform(f"{nspc}:annular002_CON","annular002_GUID")
cmds.matchTransform(f"{nspc}:annular003_CON","annular003_GUID")
 
cmds.matchTransform(f"{nspc}:metacarpalPinky_CON","metacarpalPinky_GUID")
cmds.matchTransform(f"{nspc}:pinky001_CON","pinky001_GUID")
cmds.matchTransform(f"{nspc}:pinky002_CON","pinky002_GUID")
cmds.matchTransform(f"{nspc}:pinky003_CON","pinky003_GUID")


#create constraints between controllers and finger joints
cmds.parentConstraint(f"{nspc}:metacarpalThumb_CON",f"{nspc}:metacarpalThumb_JNT", n="parentConstraintMetacarpalThumb")
cmds.parentConstraint(f"{nspc}:thumb001_CON",f"{nspc}:thumb001_JNT", n="parentConstraintThumb001")
cmds.parentConstraint(f"{nspc}:thumb002_CON",f"{nspc}:thumb002_JNT", n="parentConstraintThumb002")
 
cmds.parentConstraint(f"{nspc}:metacarpalIndex_CON",f"{nspc}:metacarpalIndex_JNT", n="parentConstraintMetacarpalIndex")
cmds.parentConstraint(f"{nspc}:index001_CON",f"{nspc}:index001_JNT", n="parentConstraintIndex001")
cmds.parentConstraint(f"{nspc}:index002_CON",f"{nspc}:index002_JNT", n="parentConstraintIndex002")
cmds.parentConstraint(f"{nspc}:index003_CON",f"{nspc}:index003_JNT", n="parentConstraintIndex003")
 
cmds.parentConstraint(f"{nspc}:metacarpalMajor_CON",f"{nspc}:metacarpalMajor_JNT", n="parentConstraintMetacarpalMajor")
cmds.parentConstraint(f"{nspc}:major001_CON",f"{nspc}:major001_JNT", n="parentConstraintMajor001")
cmds.parentConstraint(f"{nspc}:major002_CON",f"{nspc}:major002_JNT", n="parentConstraintMajor002")
cmds.parentConstraint(f"{nspc}:major003_CON",f"{nspc}:major003_JNT", n="parentConstraintMajor003")
 
cmds.parentConstraint(f"{nspc}:metacarpalAnnular_CON",f"{nspc}:metacarpalAnnular_JNT", n="parentConstraintMetacarpalAnnular")
cmds.parentConstraint(f"{nspc}:annular001_CON",f"{nspc}:annular001_JNT", n="parentConstraintAnnular001")
cmds.parentConstraint(f"{nspc}:annular002_CON",f"{nspc}:annular002_JNT", n="parentConstraintAnnular002")
cmds.parentConstraint(f"{nspc}:annular003_CON",f"{nspc}:annular003_JNT", n="parentConstraintAnnular003")
 
cmds.parentConstraint(f"{nspc}:metacarpalPinky_CON",f"{nspc}:metacarpalPinky_JNT", n="parentConstraintMetacarpalPinky")
cmds.parentConstraint(f"{nspc}:pinky001_CON",f"{nspc}:pinky001_JNT", n="parentConstraintPinky001")
cmds.parentConstraint(f"{nspc}:pinky002_CON",f"{nspc}:pinky002_JNT", n="parentConstraintPinky002")
cmds.parentConstraint(f"{nspc}:pinky003_CON",f"{nspc}:pinky003_JNT", n="parentConstraintPinky003")



cmds.scaleConstraint(f"{nspc}:metacarpalThumb_CON",f"{nspc}:metacarpalThumb_JNT", n="parentConstraintMetacarpalThumb")
cmds.scaleConstraint(f"{nspc}:thumb001_CON",f"{nspc}:thumb001_JNT", n="parentConstraintThumb001")
cmds.scaleConstraint(f"{nspc}:thumb002_CON",f"{nspc}:thumb002_JNT", n="parentConstraintThumb002") 
cmds.scaleConstraint(f"{nspc}:metacarpalIndex_CON",f"{nspc}:metacarpalIndex_JNT", n="parentConstraintMetacarpalIndex")
cmds.scaleConstraint(f"{nspc}:index001_CON",f"{nspc}:index001_JNT", n="parentConstraintIndex001")
cmds.scaleConstraint(f"{nspc}:index002_CON",f"{nspc}:index002_JNT", n="parentConstraintIndex002")
cmds.scaleConstraint(f"{nspc}:index003_CON",f"{nspc}:index003_JNT", n="parentConstraintIndex003") 
cmds.scaleConstraint(f"{nspc}:metacarpalMajor_CON",f"{nspc}:metacarpalMajor_JNT", n="parentConstraintMetacarpalMajor")
cmds.scaleConstraint(f"{nspc}:major001_CON",f"{nspc}:major001_JNT", n="parentConstraintMajor001")
cmds.scaleConstraint(f"{nspc}:major002_CON",f"{nspc}:major002_JNT", n="parentConstraintMajor002")
cmds.scaleConstraint(f"{nspc}:major003_CON",f"{nspc}:major003_JNT", n="parentConstraintMajor003") 
cmds.scaleConstraint(f"{nspc}:metacarpalAnnular_CON",f"{nspc}:metacarpalAnnular_JNT", n="parentConstraintMetacarpalAnnular")
cmds.scaleConstraint(f"{nspc}:annular001_CON",f"{nspc}:annular001_JNT", n="parentConstraintAnnular001")
cmds.scaleConstraint(f"{nspc}:annular002_CON",f"{nspc}:annular002_JNT", n="parentConstraintAnnular002")
cmds.scaleConstraint(f"{nspc}:annular003_CON",f"{nspc}:annular003_JNT", n="parentConstraintAnnular003") 
cmds.scaleConstraint(f"{nspc}:metacarpalPinky_CON",f"{nspc}:metacarpalPinky_JNT", n="parentConstraintMetacarpalPinky")
cmds.scaleConstraint(f"{nspc}:pinky001_CON",f"{nspc}:pinky001_JNT", n="parentConstraintPinky001")
cmds.scaleConstraint(f"{nspc}:pinky002_CON",f"{nspc}:pinky002_JNT", n="parentConstraintPinky002")
cmds.scaleConstraint(f"{nspc}:pinky003_CON",f"{nspc}:pinky003_JNT", n="parentConstraintPinky003")





cmds.scaleConstraint( f"{nspc}:clavicle_CON", f"{nspc}:clavicle_JNT" )

cmds.scaleConstraint( f"{nspc}:wrist_FK_CON", f"{nspc}:handParentAttach_BUF" )

#setup clavicle child attach 

cmds.scaleConstraint( f"{nspc}:clavicle_JNT", f"{nspc}:clavicle_childAttach_BUF", mo=False , n="scConClavicleChildAttach")
cmds.parentConstraint( f"{nspc}:clavicle_JNT", f"{nspc}:clavicle_childAttach_BUF", mo=False, n="paConClavicleChildAttach")

cmds.scaleConstraint( f"{nspc}:clavicle_childAttach_BUF", f"{nspc}:humerusFKAttach_BUF", mo=True, n="paConClavicleChildAttach")


# delete arm guids 
cmds.delete( "clavicle_GUID", "humerus_GUID", "radius_GUID", "wrist_GUID", "ikUpVectorArm_GUID", "armGuid_GRP" )

#delete _GUID and creation tools
cmds.delete("metacarpalThumb_GUID", "thumb001_GUID", "thumb002_GUID", "metacarpalMajor_GUID", "major001_GUID", "major002_GUID", "major003_GUID", "metacarpalAnnular_GUID", "annular001_GUID", "annular002_GUID", "annular003_GUID", "metacarpalPinky_GUID", "pinky001_GUID", "pinky002_GUID", "pinky003_GUID", "metacarpalIndex_GUID", "index001_GUID", "index002_GUID", "index003_GUID", "referenceFinger_CON")
 



#after the script is runned use the tranX value of the L_arm:radius_FK_CON and L_arm:wrist_FK_CON and place the value in B1 and B2 length then store rest pose 

#Add space switch receiver

cmds.group(n="ikUpVectorSpaceSwitch_BUF", em=True)
cmds.matchTransform(f"{nspc}:ikUpVectorSpaceSwitch_BUF" , f"{nspc}:ikUpVector_parentAttach_BUF")
cmds.parent(f"{nspc}:ikUpVectorSpaceSwitch_BUF", f"{nspc}:ikUpVector_parentAttach_BUF")
cmds.parent(f"{nspc}:upVector_IK_CON", f"{nspc}:ikUpVectorSpaceSwitch_BUF")



cmds.group(n="clavicleRotationSpace_BUF", em=True)
cmds.matchTransform(f"{nspc}:clavicleRotationSpace_BUF" , f"{nspc}:clavicle_CON")
cmds.parent(f"{nspc}:clavicleRotationSpace_BUF", f"{nspc}:clavicle_CON")
cmds.parentConstraint(f"{nspc}:clavicle_CON",f"{nspc}:clavicleRotationSpace_BUF" ,n="clavicleRotationSpace_paCns" )
cmds.scaleConstraint(f"{nspc}:clavicle_CON",f"{nspc}:clavicleRotationSpace_BUF" ,n="clavicleRotationSpace_scCns" )


cmds.group(n="ikHandSpaceSwitch_BUF", em=True)
cmds.matchTransform(f"{nspc}:ikHandSpaceSwitch_BUF" , f"{nspc}:ikHand_parentAttach_BUF")
cmds.parent(f"{nspc}:ikHandSpaceSwitch_BUF", f"{nspc}:ikHand_parentAttach_BUF")
cmds.parent(f"{nspc}:hand_IK_CON", f"{nspc}:ikHandSpaceSwitch_BUF")


cmds.setAttr ( f"{nspc}:ikUpVectorSpaceSwitch_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikUpVectorSpaceSwitch_BUF " + ".outlinerColor" , 255,255,0)

cmds.setAttr ( f"{nspc}:clavicleRotationSpace_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:clavicleRotationSpace_BUF " + ".outlinerColor" , 255,255,0)

cmds.setAttr ( f"{nspc}:ikHandSpaceSwitch_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikHandSpaceSwitch_BUF " + ".outlinerColor" , 255,255,0)


bone1Length = (cmds.getAttr("%s:radius_FK_CON.translateX"% nspc) ) 
cmds.setAttr(f"{nspc}:setup_BUF.b1Length", bone1Length )

bone2Length = (cmds.getAttr("%s:wrist_FK_CON.translateX"% nspc) ) 
cmds.setAttr(f"{nspc}:setup_BUF.b2Length", bone2Length )


cmds.namespace( set=':')
