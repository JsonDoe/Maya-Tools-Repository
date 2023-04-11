#autoRigModuleAdvancedSpine.py
#with stretch and squatch 
#don't forget to create reference node "hips_GUID", "hipsDepth_GUID", "middle_GUID", "chestDepth_GUID", "chest_GUID", "referenceFilterScaleBone0" (reference ramp texture nod)

#beforehand create : 

import maya.cmds as cmds 

#set namespace variable 
nspc = "spine"

#initiate namespace
cmds.namespace( add=f"{nspc}")
cmds.namespace( set=f"{nspc}")

cmds.duplicate( "hips_CON", n="middle_CON") 
cmds.duplicate( "hipsDepth_CON", n="chestDepth_CON") 

cmds.rename("upperBody_CON", f":{nspc}:upperBody_CON")
cmds.rename("hips_CON", f":{nspc}:hips_CON" )
cmds.rename("hipsDepth_CON", f":{nspc}:hipsDepth_CON" )
cmds.rename("chest_CON",  f":{nspc}:chest_CON")


#create module groups 
cmds.group( em=True, n="module")
cmds.group( em=True, n="controllers")
cmds.group( em=True, n="joints")
cmds.group( em=True, n="hidden")
cmds.group( em=True, n="parentAttachUpperBody_BUF")
cmds.group( em=True, n="childAttachLastVertebra_BUF")
cmds.group( em=True, n="childAttachFirstVertebra_BUF")
cmds.group( em=True, n="setup_BUF" )

#color _BUF groups the proper colors
cmds.setAttr ( f"{nspc}:parentAttachUpperBody_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:parentAttachUpperBody_BUF " + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:childAttachLastVertebra_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:childAttachLastVertebra_BUF" + ".outlinerColor" , 255,0,0)


cmds.setAttr ( f"{nspc}:childAttachFirstVertebra_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:childAttachFirstVertebra_BUF" + ".outlinerColor" , 255,0,0)

#organize hierarchy 
cmds.parent( f"{nspc}:controllers", f"{nspc}:module")
cmds.parent( f"{nspc}:joints", f"{nspc}:module")
cmds.parent( f"{nspc}:hidden", f"{nspc}:module")
cmds.parent( f"{nspc}:parentAttachUpperBody_BUF ", f"{nspc}:controllers")
cmds.parent( f"{nspc}:childAttachLastVertebra_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:childAttachFirstVertebra_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:setup_BUF", f"{nspc}:module")


cmds.parent( f"{nspc}:upperBody_CON" , f"{nspc}:parentAttachUpperBody_BUF")
cmds.parent( f"{nspc}:hips_CON" , f"{nspc}:upperBody_CON" )
cmds.parent( f"{nspc}:hipsDepth_CON" , f"{nspc}:hips_CON" )

cmds.parent( f"{nspc}:middle_CON" , f"{nspc}:upperBody_CON" )
cmds.parent( f"{nspc}:chest_CON" , f"{nspc}:middle_CON" )
cmds.parent( f"{nspc}:chestDepth_CON" , f"{nspc}:chest_CON" )

#match position of controllers with GUIDs
cmds.matchTransform(f"{nspc}:upperBody_CON","hips_GUID")
cmds.matchTransform(f"{nspc}:hips_CON","hips_GUID")
cmds.matchTransform(f"{nspc}:hipsDepth_CON","hipsDepth_GUID")
cmds.matchTransform(f"{nspc}:middle_CON","middle_GUID")
cmds.matchTransform(f"{nspc}:chest_CON","chest_GUID")
cmds.matchTransform(f"{nspc}:chestDepth_CON","chestDepth_GUID")


#create joints 
cmds.joint(n="spine000_JNT", p=(0, 0, 0) , rad=0.2)
cmds.joint(n="spine001_JNT", p=(0, 0.96, 0) , rad=0.2 )
cmds.joint(n="spine002_JNT", p=(0, 1.92, 0) , rad=0.2 )
cmds.joint(n="spine003_JNT", p=(0, 2.88, 0) , rad=0.2)
cmds.joint(n="spine004_JNT", p=(0, 3.84, 0) , rad=0.2)
cmds.joint(n="spine005_JNT", p=(0, 4.8, 0) , rad=0.2)

#Place joint in the right folder 
cmds.parent( f"{nspc}:spine000_JNT" , f"{nspc}:joints" )

#match joint with hips
cmds.matchTransform(f"{nspc}:spine000_JNT", f"{nspc}:hips_CON" )

#create curve
cmds.curve( p=[(0, 0, 0), (0, 1.2, 0), (0, 2.4, 0), (0, 3.6, 0), (0, 4.8, 0)], n="controlCurve")


#Place curve in the right folder 
cmds.parent(f"{nspc}:controlCurve", f"{nspc}:hidden")

#creat ikHandle for the spine joints
cmds.ikHandle( sol="ikSplineSolver", sj=f"{nspc}:spine000_JNT", ee=f"{nspc}:spine005_JNT", p=1, w=1, pw=1, n="ikHandleSpine" )

cmds.parent( f"{nspc}:ikHandleSpine", f"{nspc}:hidden" )

#create decomposeMatrix nodes 
cmds.createNode( "decomposeMatrix", n="decomposeMatrixHips" )
cmds.createNode( "decomposeMatrix", n="decomposeMatrixHipsDepth" )
cmds.createNode( "decomposeMatrix", n="decomposeMatrixMiddle" )
cmds.createNode( "decomposeMatrix", n="decomposeMatrixChestDepth" )
cmds.createNode( "decomposeMatrix", n="decomposeMatrixChest" )

#connect controllers world matrix to decomposeMatrix nodes 
cmds.connectAttr(f"{nspc}:hips_CON.worldMatrix[0]", f"{nspc}:decomposeMatrixHips.inputMatrix" )
cmds.connectAttr(f"{nspc}:hipsDepth_CON.worldMatrix[0]", f"{nspc}:decomposeMatrixHipsDepth.inputMatrix" )
cmds.connectAttr(f"{nspc}:middle_CON.worldMatrix[0]", f"{nspc}:decomposeMatrixMiddle.inputMatrix" )
cmds.connectAttr(f"{nspc}:chestDepth_CON.worldMatrix[0]", f"{nspc}:decomposeMatrixChestDepth.inputMatrix" )
cmds.connectAttr(f"{nspc}:chest_CON.worldMatrix[0]", f"{nspc}:decomposeMatrixChest.inputMatrix" )

#connect Decompose Matrixs to spine control curve 
cmds.connectAttr( f"{nspc}:decomposeMatrixHips.outputTranslate", f"{nspc}:controlCurve.controlPoints[0]" )
cmds.connectAttr( f"{nspc}:decomposeMatrixHipsDepth.outputTranslate", f"{nspc}:controlCurve.controlPoints[1]" )
cmds.connectAttr( f"{nspc}:decomposeMatrixMiddle.outputTranslate", f"{nspc}:controlCurve.controlPoints[2]" )
cmds.connectAttr( f"{nspc}:decomposeMatrixChestDepth.outputTranslate", f"{nspc}:controlCurve.controlPoints[3]" )
cmds.connectAttr( f"{nspc}:decomposeMatrixChest.outputTranslate", f"{nspc}:controlCurve.controlPoints[4]" )




#addition
#add attributes to the setup 

cmds.select( f"{nspc}:setup_BUF" )

cmds.addAttr( at="float", ln="restLength", nn="Rest Length" , dv=4.8, k=True)

cmds.addAttr( at="long", ln="bonesCount", nn="Bones Count" , dv=6, k=True)

cmds.addAttr( at="float", ln="maxStretchFactor", nn="Max Stretch Factor" , dv=1.2, k=True)

cmds.addAttr( at="float", ln="minStretchFactor", nn="Min Stretch Factor" , dv=0.8, k=True)

cmds.addAttr( at="float", ln="stretchScale", nn="Stretch Scale" , dv=0.2, k=True)

cmds.addAttr( at="float", ln="squashScale", nn="Squash Scale" , dv=2, k=True)


#substract one from the bone number value 
cmds.createNode( "floatMath" , n="removeOneBone")
cmds.setAttr( f"{nspc}:removeOneBone.operation", 1 )
cmds.connectAttr( f"{nspc}:setup_BUF.bonesCount", f"{nspc}:removeOneBone.floatA" )


# create maths node controling the distribution value wich define the division for motion path uValue 
cmds.createNode( "floatMath" , n="distributionStep")
cmds.setAttr( f"{nspc}:distributionStep.operation", 3 )
cmds.connectAttr( f"{nspc}:removeOneBone.outFloat", f"{nspc}:distributionStep.floatB" )



#setup multiplier value for each bone 
cmds.createNode( "floatMath" , n="bone0PercentLength")
cmds.setAttr( f"{nspc}:bone0PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone0PercentLength.floatB", 0 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone0PercentLength.floatA" )

cmds.createNode( "floatMath" , n="bone1PercentLength")
cmds.setAttr( f"{nspc}:bone1PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone1PercentLength.floatB", 1 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone1PercentLength.floatA" )

cmds.createNode( "floatMath" , n="bone2PercentLength")
cmds.setAttr( f"{nspc}:bone2PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone2PercentLength.floatB", 2 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone2PercentLength.floatA" )

cmds.createNode( "floatMath" , n="bone3PercentLength")
cmds.setAttr( f"{nspc}:bone3PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone3PercentLength.floatB", 3 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone3PercentLength.floatA" )

cmds.createNode( "floatMath" , n="bone4PercentLength")
cmds.setAttr( f"{nspc}:bone4PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone4PercentLength.floatB", 4 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone4PercentLength.floatA" )


cmds.createNode( "floatMath" , n="bone5PercentLength")
cmds.setAttr( f"{nspc}:bone5PercentLength.operation", 2 )
cmds.setAttr( f"{nspc}:bone5PercentLength.floatB", 5 )
cmds.connectAttr( f"{nspc}:distributionStep.outFloat", f"{nspc}:bone5PercentLength.floatA" )

# un motion path par node /!!!!!!!!!!!!!!!\activer parametric length
cmds.createNode( "motionPath" , n="motionPathBone0")
cmds.setAttr( f"{nspc}:motionPathBone0.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone0.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone0PercentLength.outFloat", f"{nspc}:motionPathBone0.uValue"  )

cmds.createNode( "motionPath" , n="motionPathBone1") 
cmds.setAttr( f"{nspc}:motionPathBone1.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone1.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone1PercentLength.outFloat", f"{nspc}:motionPathBone1.uValue"  )

cmds.createNode( "motionPath" , n="motionPathBone2") 
cmds.setAttr( f"{nspc}:motionPathBone2.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone2.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone2PercentLength.outFloat", f"{nspc}:motionPathBone2.uValue"  ) #/!\ u value is not connected 

cmds.createNode( "motionPath" , n="motionPathBone3")
cmds.setAttr( f"{nspc}:motionPathBone3.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone3.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone3PercentLength.outFloat", f"{nspc}:motionPathBone3.uValue"  )

cmds.createNode( "motionPath" , n="motionPathBone4")
cmds.setAttr( f"{nspc}:motionPathBone4.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone4.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone4PercentLength.outFloat", f"{nspc}:motionPathBone4.uValue"  )

cmds.createNode( "motionPath" , n="motionPathBone5")
cmds.setAttr( f"{nspc}:motionPathBone5.fractionMode", 1  )
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:motionPathBone5.geometryPath"  )
cmds.connectAttr(  f"{nspc}:bone5PercentLength.outFloat", f"{nspc}:motionPathBone5.uValue"  )
# à corriger /!\ DONE 

#nodes pour calculer la distance 
cmds.createNode( "distanceBetween" , n="boneLength1")
cmds.connectAttr(  f"{nspc}:motionPathBone0.allCoordinates", f"{nspc}:boneLength1.point1"  )
cmds.connectAttr(  f"{nspc}:motionPathBone1.allCoordinates", f"{nspc}:boneLength1.point2"  )

cmds.createNode( "distanceBetween" , n="boneLength2")
cmds.connectAttr(  f"{nspc}:motionPathBone1.allCoordinates", f"{nspc}:boneLength2.point1"  )
cmds.connectAttr(  f"{nspc}:motionPathBone2.allCoordinates", f"{nspc}:boneLength2.point2"  )

cmds.createNode( "distanceBetween" , n="boneLength1")
cmds.connectAttr(  f"{nspc}:motionPathBone2.allCoordinates", f"{nspc}:boneLength3.point1"  )
cmds.connectAttr(  f"{nspc}:motionPathBone3.allCoordinates", f"{nspc}:boneLength3.point2"  )

cmds.createNode( "distanceBetween" , n="boneLength1")
cmds.connectAttr(  f"{nspc}:motionPathBone3.allCoordinates", f"{nspc}:boneLength4.point1"  )
cmds.connectAttr(  f"{nspc}:motionPathBone4.allCoordinates", f"{nspc}:boneLength4.point2"  )

cmds.createNode( "distanceBetween" , n="boneLength1")
cmds.connectAttr(  f"{nspc}:motionPathBone4.allCoordinates", f"{nspc}:boneLength5.point1"  )
cmds.connectAttr(  f"{nspc}:motionPathBone5.allCoordinates", f"{nspc}:boneLength5.point2"  )
#/!\corriger length en length !!!!!


#connect distance au trans Y des joints de spine (sauf bone 0)
cmds.connectAttr(  f"{nspc}:boneLength1.distance", f"{nspc}:spine001_JNT.translateY"  )
cmds.connectAttr(  f"{nspc}:boneLength2.distance", f"{nspc}:spine002_JNT.translateY"  )
cmds.connectAttr(  f"{nspc}:boneLength3.distance", f"{nspc}:spine003_JNT.translateY"  )
cmds.connectAttr(  f"{nspc}:boneLength4.distance", f"{nspc}:spine004_JNT.translateY"  )
cmds.connectAttr(  f"{nspc}:boneLength5.distance", f"{nspc}:spine005_JNT.translateY"  )


######## SCRIPT ADDITON TO MULTIPLY SCALE 

cmds.createNode( "decomposeMatrix", n="getUpperbodyConScaleX" )
cmds.connectAttr(f"{nspc}:upperBody_CON.worldMatrix[0]", f"{nspc}:getUpperbodyConScaleX.inputMatrix" )

cmds.createNode( "floatMath", n="multRestLengthByScale")
cmds.setAttr( f"{nspc}:multRestLengthByScale.operation", 2 )
cmds.connectAttr(f"{nspc}:setup_BUF.restLength", f"{nspc}:multRestLengthByScale.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:multRestLengthByScale.floatB" )



#Scale de strech : 
#lengthState
# STretch nodes :


#create  curve info to get bones locations 
cmds.createNode( "curveInfo" , n="curveLength")
cmds.connectAttr(  f"{nspc}:curveShape1.worldSpace[0]", f"{nspc}:curveLength.inputCurve"  )

#create multiplicative factors of the min and max lengths
cmds.createNode( "floatMath" , n="maxLength")
cmds.setAttr( f"{nspc}:maxLength.operation", 2 )
cmds.connectAttr(  f"{nspc}::multRestLengthByScale.outFloat", f"{nspc}:maxLength.floatA"  )
cmds.connectAttr(  f"{nspc}:setup_BUF.maxStretchFactor", f"{nspc}:maxLength.floatB"  )

cmds.createNode( "floatMath" , n="minLength")
cmds.setAttr( f"{nspc}:minLength.operation", 2 ) #/!\ verify
cmds.connectAttr(  f"{nspc}::multRestLengthByScale.outFloat", f"{nspc}:minLength.floatA"  )
cmds.connectAttr(  f"{nspc}:setup_BUF.minStretchFactor", f"{nspc}:minLength.floatB"  )


#float maths divide to verify get the current length state  !!!!!!!!!!!! connect length state  
cmds.createNode( "floatMath" , n="lengthState")
cmds.setAttr( f"{nspc}:lengthState.operation", 3 )
cmds.connectAttr(  f"{nspc}:curveLength.arcLength", f"{nspc}:lengthState.floatA"  )
cmds.connectAttr(  f"{nspc}::multRestLengthByScale.outFloat", f"{nspc}:lengthState.floatB"  )

# add select setpup /!\ add attribute for the scales DONE
cmds.addAttr( at="float", ln="stretchScale", nn="Stretch Scale" , dv=1, k=True)

cmds.addAttr( at="float", ln="squashScale", nn="Squash Scale" , dv=1, k=True)

cmds.setAttr( f"{nspc}:setup_BUF.stretchScale", 0.2 )
cmds.setAttr( f"{nspc}:setup_BUF.squashScale", 2 )


###  /!\ add all the connections to the setRange DONE /!\ set values to 1 /!\ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
cmds.createNode( "setRange" , n="setRangeLength")
cmds.connectAttr(  f"{nspc}:curveLength.arcLength", f"{nspc}:setRangeLength.valueX"  )
cmds.connectAttr(  f"{nspc}:curveLength.arcLength", f"{nspc}:setRangeLength.valueY"  )

cmds.connectAttr(  f"{nspc}:setup_BUF.stretchScale", f"{nspc}:setRangeLength.maxX"  )
cmds.connectAttr(  f"{nspc}:setup_BUF.squashScale", f"{nspc}:setRangeLength.minY"  )

cmds.connectAttr(  f"{nspc}:maxLength.outFloat", f"{nspc}:setRangeLength.oldMaxX"  )
cmds.connectAttr(  f"{nspc}::multRestLengthByScale.outFloat", f"{nspc}:setRangeLength.oldMaxY"  )

cmds.connectAttr(  f"{nspc}::multRestLengthByScale.outFloat", f"{nspc}:setRangeLength.oldMinX"  )
cmds.connectAttr(  f"{nspc}:minLength.outFloat", f"{nspc}:setRangeLength.oldMinY"  )
cmds.setAttr( f"{nspc}:setRangeLength.minX", 1 )
cmds.setAttr( f"{nspc}:setRangeLength.maxY", 1 )




#add float logic ( OutFloat --> Float A, op = 5) then float condition (float A --> outValueX, Float B --> outValueY)
#verify if length is > or < 1

cmds.createNode( "floatLogic" , n="verifyStrechSquach")
cmds.connectAttr(  f"{nspc}:lengthState.outFloat", f"{nspc}:verifyStrechSquach.floatA"  )
cmds.setAttr( f"{nspc}:verifyStrechSquach.operation", 5 )
cmds.setAttr( f"{nspc}:verifyStrechSquach.floatB", 1 )

cmds.createNode( "floatCondition" , n="conditionVerifyValue")
cmds.connectAttr(  f"{nspc}:verifyStrechSquach.outBool", f"{nspc}:conditionVerifyValue.condition"  )
cmds.connectAttr(  f"{nspc}:setRangeLength.outValueX", f"{nspc}:conditionVerifyValue.floatA"  )
cmds.connectAttr(  f"{nspc}:setRangeLength.outValueY", f"{nspc}:conditionVerifyValue.floatB"  )


#Doesn't work Find why /!\ FIXED --> I inverted Float A and Float B  sur lengthState 


#partir par la création fe substractMath
# et des outfloat de bone percent 
cmds.createNode( "floatMath" , n="SubstractMath")
cmds.connectAttr(  f"{nspc}:conditionVerifyValue.outFloat", f"{nspc}:SubstractMath.floatA"  )
cmds.setAttr( f"{nspc}:SubstractMath.operation", 1 ) #/!\ VERIFY
cmds.setAttr( f"{nspc}:SubstractMath.floatB", 1 )

# /!\ add ramp [texture] creation , till you find how to do creation properly, create node beforehand then duplicate 
#cmds.createNode( "ramp" , n="filterScaleBone0")
#cmds.setAttr( f"{nspc}:filterScaleBone0.type", 1)
#cmds.setAttr( f"{nspc}:essai1.colorEntryList[2].position", 0.5)

# setup it than connect b2PCL 
#cmds.connectAttr(  f"{nspc}:bone2PercentLenght.outFloat", f"{nspc}:filterScaleBone2.uvCoord.uCoord"  )

#connect number 2 than duplicate than connect 



cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone0" )

cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone1" )

cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone2" )

cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone3" )

cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone4" )

cmds.duplicate( "referenceFilterScaleBone0", n=f":{nspc}:filterScaleBone5" )

cmds.connectAttr(  f"{nspc}:bone0PercentLength.outFloat", f"{nspc}:filterScaleBone0.uvCoord.uCoord"  )

cmds.connectAttr(  f"{nspc}:bone1PercentLength.outFloat", f"{nspc}:filterScaleBone1.uvCoord.uCoord"  )

cmds.connectAttr(  f"{nspc}:bone2PercentLength.outFloat", f"{nspc}:filterScaleBone2.uvCoord.uCoord"  )

cmds.connectAttr(  f"{nspc}:bone3PercentLength.outFloat", f"{nspc}:filterScaleBone3.uvCoord.uCoord"  )

cmds.connectAttr(  f"{nspc}:bone4PercentLength.outFloat", f"{nspc}:filterScaleBone4.uvCoord.uCoord"  )

cmds.connectAttr(  f"{nspc}:bone5PercentLength.outFloat", f"{nspc}:filterScaleBone5.uvCoord.uCoord"  )


# create scale bone nodes and connect them 

cmds.createNode( "floatMath" , n="scaleBone0")
cmds.setAttr( f"{nspc}:scaleBone0.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone0.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone0.outColorR", f"{nspc}:scaleBone0.floatB"  )

cmds.createNode( "floatMath" , n="scaleBone1")
cmds.setAttr( f"{nspc}:scaleBone1.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone1.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone1.outColorR", f"{nspc}:scaleBone1.floatB"  )

cmds.createNode( "floatMath" , n="scaleBone2")
cmds.setAttr( f"{nspc}:scaleBone2.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone2.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone2.outColorR", f"{nspc}:scaleBone2.floatB"  )

cmds.createNode( "floatMath" , n="scaleBone3")
cmds.setAttr( f"{nspc}:scaleBone3.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone3.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone3.outColorR", f"{nspc}:scaleBone3.floatB"  )

cmds.createNode( "floatMath" , n="scaleBone4")
cmds.setAttr( f"{nspc}:scaleBone4.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone4.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone4.outColorR", f"{nspc}:scaleBone4.floatB"  )

cmds.createNode( "floatMath" , n="scaleBone5")
cmds.setAttr( f"{nspc}:scaleBone5.operation", 2 )
cmds.connectAttr(  f"{nspc}:SubstractMath.outFloat", f"{nspc}:scaleBone5.floatA"  )
cmds.connectAttr(  f"{nspc}:filterScaleBone5.outColorR", f"{nspc}:scaleBone5.floatB"  )


# create and connect fix Scale Bone

cmds.createNode( "floatMath" , n="fixScaleBone0")
cmds.setAttr( f"{nspc}:fixScaleBone0.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone0.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone0.outFloat", f"{nspc}:fixScaleBone0.floatA"  )

cmds.createNode( "floatMath" , n="fixScaleBone1")
cmds.setAttr( f"{nspc}:fixScaleBone1.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone1.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone1.outFloat", f"{nspc}:fixScaleBone1.floatA"  )

cmds.createNode( "floatMath" , n="fixScaleBone2")
cmds.setAttr( f"{nspc}:fixScaleBone2.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone2.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone2.outFloat", f"{nspc}:fixScaleBone2.floatA"  )

cmds.createNode( "floatMath" , n="fixScaleBone3")
cmds.setAttr( f"{nspc}:fixScaleBone3.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone3.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone3.outFloat", f"{nspc}:fixScaleBone3.floatA"  )

cmds.createNode( "floatMath" , n="fixScaleBone4")
cmds.setAttr( f"{nspc}:fixScaleBone4.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone4.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone4.outFloat", f"{nspc}:fixScaleBone4.floatA"  )

cmds.createNode( "floatMath" , n="fixScaleBone5")
cmds.setAttr( f"{nspc}:fixScaleBone5.operation", 0 )
cmds.setAttr( f"{nspc}:fixScaleBone5.floatB", 1 )
cmds.connectAttr(  f"{nspc}:scaleBone5.outFloat", f"{nspc}:fixScaleBone5.floatA"  )



###### ADD SCALE TO JOINT CORRECTION HERE 


cmds.createNode( "floatMath" , n="fixScalabilityBone0")
cmds.setAttr( f"{nspc}:fixScalabilityBone0.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone0.outFloat", f"{nspc}:fixScalabilityBone0.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone0.floatB" )

cmds.createNode( "floatMath" , n="fixScalabilityBone1")
cmds.setAttr( f"{nspc}:fixScalabilityBone1.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone1.outFloat", f"{nspc}:fixScalabilityBone1.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone1.floatB" )

cmds.createNode( "floatMath" , n="fixScalabilityBone2")
cmds.setAttr( f"{nspc}:fixScalabilityBone2.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone2.outFloat", f"{nspc}:fixScalabilityBone2.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone2.floatB" )

cmds.createNode( "floatMath" , n="fixScalabilityBone3")
cmds.setAttr( f"{nspc}:fixScalabilityBone3.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone3.outFloat", f"{nspc}:fixScalabilityBone3.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone3.floatB" )

cmds.createNode( "floatMath" , n="fixScalabilityBone4")
cmds.setAttr( f"{nspc}:fixScalabilityBone4.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone4.outFloat", f"{nspc}:fixScalabilityBone4.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone4.floatB" )

cmds.createNode( "floatMath" , n="fixScalabilityBone5")
cmds.setAttr( f"{nspc}:fixScalabilityBone5.operation", 2 )
cmds.connectAttr(f"{nspc}:fixScaleBone5.outFloat", f"{nspc}:fixScalabilityBone5.floatA" )
cmds.connectAttr(f"{nspc}:getUpperbodyConScaleX.outputScaleX", f"{nspc}:fixScalabilityBone5.floatB" )


# connect fix scale bone nodes to the scaleX scaleZ of the joints

cmds.connectAttr(  f"{nspc}:fixScalabilityBone0.outFloat", f"{nspc}:spine000_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone0.outFloat", f"{nspc}:spine000_JNT.scaleZ"  )

cmds.connectAttr(  f"{nspc}:fixScalabilityBone1.outFloat", f"{nspc}:spine001_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone1.outFloat", f"{nspc}:spine001_JNT.scaleZ"  )

cmds.connectAttr(  f"{nspc}:fixScalabilityBone2.outFloat", f"{nspc}:spine002_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone2.outFloat", f"{nspc}:spine002_JNT.scaleZ"  )

cmds.connectAttr(  f"{nspc}:fixScalabilityBone3.outFloat", f"{nspc}:spine003_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone3.outFloat", f"{nspc}:spine003_JNT.scaleZ"  )

cmds.connectAttr(  f"{nspc}:fixScalabilityBone4.outFloat", f"{nspc}:spine004_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone4.outFloat", f"{nspc}:spine004_JNT.scaleZ"  )

cmds.connectAttr(  f"{nspc}:fixScalabilityBone5.outFloat", f"{nspc}:spine005_JNT.scaleX"  )
cmds.connectAttr(  f"{nspc}:fixScalabilityBone5.outFloat", f"{nspc}:spine005_JNT.scaleZ"  )






#connect elements with the ikHandle 
cmds.connectAttr( f"{nspc}:controlCurve.worldSpace[0]", f"{nspc}:ikHandleSpine.inCurve", f=True )

cmds.connectAttr( f"{nspc}:hips_CON.worldMatrix[0] ", f"{nspc}:ikHandleSpine.dWorldUpMatrix" )
cmds.connectAttr( f"{nspc}:chestDepth_CON.worldMatrix[0] ", f"{nspc}:ikHandleSpine.dWorldUpMatrixEnd" )


cmds.delete("hips_GUID", "hipsDepth_GUID", "middle_GUID", "chestDepth_GUID", "chest_GUID", "referenceFilterScaleBone0" )


### SCRIPT ADDITION 03/03/2023

#match child attach at the proper place
cmds.matchTransform( f"{nspc}:childAttachLastVertebra_BUF", f"{nspc}:spine005_JNT"  )

cmds.matchTransform( f"{nspc}:childAttachFirstVertebra_BUF", f"{nspc}:spine000_JNT"  )

#add constraints 
cmds.parentConstraint( f"{nspc}:spine005_JNT", f"{nspc}:childAttachLastVertebra_BUF"  )
cmds.scaleConstraint( f"{nspc}:upperBody_CON", f"{nspc}:childAttachLastVertebra_BUF"  )

cmds.parentConstraint( f"{nspc}:spine000_JNT", f"{nspc}:childAttachFirstVertebra_BUF"  )
cmds.scaleConstraint( f"{nspc}:upperBody_CON", f"{nspc}:childAttachFirstVertebra_BUF"  )

cmds.orientConstraint( f"{nspc}:chest_CON", f"{nspc}:spine005_JNT"  )

boneLength = (cmds.getAttr("%s:hipsDepth_CON.translateY"% nspc) ) * 4
cmds.setAttr(f"{nspc}:setup_BUF.restLength", boneLength )

#ADDING SPACE SWITCH DATA SENDER
cmds.group(n="upperBodyRotationSpace_BUF", em=True)
cmds.parent(f"{nspc}:upperBodyRotationSpace_BUF", f"{nspc}:controllers")
cmds.matchTransform(f"{nspc}:upperBodyRotationSpace_BUF" , f"{nspc}:upperBody_CON")

cmds.parentConstraint(f"{nspc}:upperBody_CON",f"{nspc}:upperBodyRotationSpace_BUF" ,n="upperBodyRotationSpace_paCns" ,mo=False)
cmds.scaleConstraint(f"{nspc}:upperBody_CON",f"{nspc}:upperBodyRotationSpace_BUF" ,n="upperBodyRotationSpace_scCns" ,mo=False)

cmds.group(n="chestRotationSpace_BUF", em=True)
cmds.parent(f"{nspc}:chestRotationSpace_BUF", f"{nspc}:controllers")
cmds.matchTransform(f"{nspc}:chestRotationSpace_BUF" , f"{nspc}:chest_CON")

cmds.parentConstraint(f"{nspc}:chest_CON",f"{nspc}:chestRotationSpace_BUF" ,n="chestRotationSpace_paCns" )
cmds.scaleConstraint(f"{nspc}:chest_CON",f"{nspc}:chestRotationSpace_BUF" ,n="chestRotationSpace_scCns" )

cmds.setAttr ( f"{nspc}:upperBodyRotationSpace_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:upperBodyRotationSpace_BUF " + ".outlinerColor" , 255,255,0)

cmds.setAttr ( f"{nspc}:chestRotationSpace_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:chestRotationSpace_BUF" + ".outlinerColor" , 255,255,0)

cmds.namespace( set=":")
