#autoRigModuleAdvancedLeg.py

#autoRig {nspc} 
import maya.cmds as cmds

#initiate namespace variable 
nspc = 'R_Leg'

#initiate namespace
cmds.namespace( add=f'{nspc}')
cmds.namespace( set=f'{nspc}')

#add _CON to namespace 
cmds.rename( 'ikFoot_CON1', f':{nspc}:ikFoot_CON' )
cmds.rename( 'ikUpVectorLeg_CON1', f':{nspc}:ikUpVector_CON' )


#create module groups with the proper naming 
cmds.group( em=True, n='module')
cmds.group( em=True, n='controllers')
cmds.group( em=True, n='joints')
cmds.group( em=True, n='hidden')
cmds.group( em=True, n='ikFootParentAttach_BUF ')
cmds.group( em=True, n='ikUpVectorParentAttach_BUF')
cmds.group( em=True, n='parentAttach_BUF ')

cmds.group( em=True, n='heelTwist_BUF')
cmds.group( em=True, n='endFootTwist_BUF')
cmds.group( em=True, n='midFootTwist_BUF')

cmds.group( em=True, n='exterior_BUF')
cmds.group( em=True, n='interior_BUF')
cmds.group( em=True, n='heel_BUF')
cmds.group( em=True, n='endToes_BUF')

cmds.group( em=True, n='upVectorIKToes_BUF')
cmds.group( em=True, n='midFootTorsion_BUF')

cmds.group( em=True, n='midFoot_BUF')

cmds.group( em=True, n='ikAnkle_BUF')
cmds.group( em=True, n='upVectorIKAnckle_BUF')










#Structure hierarchy /!\ update hierarchy
cmds.parent( f"{nspc}:controllers", f"{nspc}:module")
cmds.parent( f"{nspc}:joints", f"{nspc}:module")
cmds.parent( f"{nspc}:hidden", f"{nspc}:module")
cmds.parent( f"{nspc}:parentAttach_BUF ", f"{nspc}:controllers")
cmds.parent( f"{nspc}:ikUpVectorParentAttach_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:ikFootParentAttach_BUF", f"{nspc}:controllers")
#cmds.parent( f"{nspc}:ikFoot_CON", f"{nspc}:controllers")

#Structure Foot roll hierarchy 
cmds.parent( f"{nspc}:heelTwist_BUF", f"{nspc}:ikFoot_CON")
cmds.parent( f"{nspc}:endFootTwist_BUF", f"{nspc}:heelTwist_BUF")
cmds.parent( f"{nspc}:midFootTwist_BUF", f"{nspc}:endFootTwist_BUF")

cmds.parent( f"{nspc}:exterior_BUF", f"{nspc}:midFootTwist_BUF")
cmds.parent( f"{nspc}:interior_BUF", f"{nspc}:exterior_BUF")
cmds.parent( f"{nspc}:heel_BUF", f"{nspc}:interior_BUF")
cmds.parent( f"{nspc}:endToes_BUF", f"{nspc}:heel_BUF")

cmds.parent( f"{nspc}:midFootTorsion_BUF", f"{nspc}:endToes_BUF")

cmds.parent( f"{nspc}:midFoot_BUF", f"{nspc}:midFootTorsion_BUF")
cmds.parent( f"{nspc}:ikAnkle_BUF", f"{nspc}:midFoot_BUF")

# /!\ verify with teacher 
cmds.parent(f'{nspc}:upVectorIKToes_BUF', f'{nspc}:endToes_BUF')
cmds.parent(f'{nspc}:upVectorIKAnckle_BUF', f'{nspc}:midFoot_BUF')

#color _BUF groups the proper colors
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikFootParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikFootParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f'{nspc}:heel_BUF' + ".useOutlinerColor" , True)
cmds.setAttr ( f'{nspc}:heel_BUF' + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f'{nspc}:endToes_BUF' + ".useOutlinerColor" , True)
cmds.setAttr ( f'{nspc}:endToes_BUF' + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f'{nspc}:midFoot_BUF' + ".useOutlinerColor" , True)
cmds.setAttr ( f'{nspc}:midFoot_BUF' + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f'{nspc}:ikAnkle_BUF' + ".useOutlinerColor" , True)
cmds.setAttr ( f'{nspc}:ikAnkle_BUF' + ".outlinerColor" , 0,100,100)

#cmds.setAttr ( f'{nspc}:ikFoot_CON' + ".useOutlinerColor" , True)
#cmds.setAttr ( f'{nspc}:ikFoot_CON' + ".outlinerColor" , 255,87,51)

#create joints with the right naming and parent them together
cmds.joint(n='femur_JNT')
cmds.joint(n='tibia_JNT')
cmds.setAttr(f"{nspc}:tibia_JNT.preferredAngleX", 90)
cmds.joint(n='ankle_JNT', rad=0.15)
cmds.joint(n='midFoot_JNT', rad=0.15)
cmds.joint(n='endToes_JNT', rad=0.15)


#parent joint with joint group
cmds.parent( f"{nspc}:femur_JNT", f"{nspc}:joints")

#parent _CON with buffers 
cmds.parent( f'{nspc}:ikFoot_CON', f'{nspc}:ikFootParentAttach_BUF' )
cmds.parent( f'{nspc}:ikUpVector_CON', f'{nspc}:ikUpVectorParentAttach_BUF' )


#match joints with the _GUID1 tools 
cmds.matchTransform(f'{nspc}:femur_JNT','femur_GUID1')
cmds.matchTransform(f'{nspc}:tibia_JNT','tibia_GUID1')
cmds.matchTransform(f'{nspc}:ankle_JNT','ankle_GUID1')
cmds.matchTransform(f'{nspc}:midFoot_JNT','midFoot_GUID1')
cmds.matchTransform(f'{nspc}:endToes_JNT','endToes_GUID1')
cmds.matchTransform(f'{nspc}:ikFoot_CON', f'{nspc}:ankle_JNT')
cmds.matchTransform(f'{nspc}:ikUpVector_CON', 'ikUpVectorLeg_GUID1')
cmds.matchTransform(f'{nspc}:parentAttach_BUF', f'{nspc}:femur_JNT')


cmds.matchTransform(f'{nspc}:heelTwist_BUF', 'heel_GUID1')
cmds.matchTransform(f'{nspc}:endFootTwist_BUF', 'endToes_GUID1')
cmds.matchTransform(f'{nspc}:midFootTwist_BUF', 'midFoot_GUID1')

cmds.matchTransform(f'{nspc}:exterior_BUF', 'exterior_GUID1')
cmds.matchTransform(f'{nspc}:interior_BUF', 'interior_GUID1')
cmds.matchTransform(f'{nspc}:heel_BUF', 'heel_GUID1')
cmds.matchTransform(f'{nspc}:endToes_BUF', f'{nspc}:endToes_JNT')

cmds.matchTransform(f'{nspc}:upVectorIKToes_BUF', 'upVectorIKToes_GUID1')
cmds.matchTransform(f'{nspc}:midFootTorsion_BUF', 'midFoot_GUID1')

cmds.matchTransform(f'{nspc}:midFoot_BUF', f'{nspc}:midFoot_JNT')
cmds.matchTransform(f'{nspc}:ikAnkle_BUF', f'{nspc}:ankle_JNT')
cmds.matchTransform(f'{nspc}:upVectorIKAnckle_BUF', 'upVectorIKAnkle_GUID1')



############################## 

#add attributes on the setup
cmds.select( f"{nspc}:ikFoot_CON" )

#Foot Roll Attributes /!\ update attributes #done
cmds.addAttr( at="float", ln="footRoll", nn="Foot Roll", dv=0, k=True)

cmds.addAttr( at="float", ln="footRollEndFoot", nn="Foot Roll End Foot", dv=0, k=True)
cmds.addAttr( at="float", ln="footRollEndFootBreak", nn="Foot Roll End Foot Break", dv=90, k=True)

cmds.addAttr( at="float", ln="footRollHeel", nn="Foot Roll Heel", dv=0, k=True)
cmds.addAttr( at="float", ln="footRollHeelBreak", nn="Foot Roll Heel Break", dv=90, k=True)

cmds.addAttr( at="float", ln="footRollMidFoot", nn="Foot Roll Mid Foot", dv=0, k=True)
cmds.addAttr( at="float", ln="footRollMidFootBreak", nn="Foot Roll Mid Foot Break", dv=70, k=True)

#side roll Attributes
cmds.addAttr( at="float", ln="sideRoll", nn="Side Roll", dv=0, k=True)
cmds.addAttr( at="float", ln="sideRollExterior", nn="Side Roll Exterior", dv=0, k=True)
cmds.addAttr( at="float", ln="sideRollInterior", nn="Side Roll Interior", dv=0, k=True)

#Twist Attributes 
cmds.addAttr( at="float", ln="twistEndFoot", nn="Twist End Foot", dv=0, k=True)
cmds.addAttr( at="float", ln="twistHeel", nn="Twist Heel", dv=0, k=True)
cmds.addAttr( at="float", ln="twistMidToes", nn="Twist Mid Toes", dv=0, k=True)

#Mid Foot Torsion attribute 
cmds.addAttr( at="float", ln="midFootTorsion", nn="Mid Foot Torsion", dv=0, k=True)


#clear selection
cmds.select( cl=True )

#Lock and hide useless parameters in the channel box
#cmds.setAttr( f"{nspc}:ikFoot_CON.tx", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.ty", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.tz", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.rx", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.ry", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.rz", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.sx", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.sy", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.sz", l=True , k=False , cb=False)
#cmds.setAttr( f"{nspc}:ikFoot_CON.v", l=True , k=False , cb=False)

#Twist /!\ update twists and add midFootTorsion connection #done
#connect nodes twist attributes to the twist buffers properly
cmds.connectAttr(f"{nspc}:ikFoot_CON.twistHeel", f"{nspc}:heelTwist_BUF.rotateY")
cmds.connectAttr(f"{nspc}:ikFoot_CON.twistEndFoot", f"{nspc}:endFootTwist_BUF.rotateY")
cmds.connectAttr(f"{nspc}:ikFoot_CON.twistMidToes", f"{nspc}:midFootTwist_BUF.rotateY")

#Torsion 
#connect attribute with rotate Z of the buffer 
cmds.connectAttr(f"{nspc}:ikFoot_CON.midFootTorsion", f"{nspc}:midFootTorsion_BUF.rotateZ")


#Side Roll
#create nodes and connect them properly

#create float logic node, verify if the value is >=, connect it properly
cmds.shadingNode( "floatLogic", au=True, n="floatLogicSideRollExt" )
cmds.setAttr(f"{nspc}:floatLogicSideRollExt.operation", 4)
cmds.setAttr(f"{nspc}:floatLogicSideRollExt.floatB", 0)
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRoll", f"{nspc}:floatLogicSideRollExt.floatA")



cmds.shadingNode( "floatCondition", au=True, n="floatConditionSideRollExt" )
cmds.connectAttr(f"{nspc}:floatLogicSideRollExt.outBool", f"{nspc}:floatConditionSideRollExt.condition")
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRoll", f"{nspc}:floatConditionSideRollExt.floatA")

#create foat Math node to add side Roll exterior and side roll value before applying it to the exterior_BUF rotZ value
cmds.shadingNode( "floatMath", au=True, n="floatMathSideRollExt" )
cmds.connectAttr(f"{nspc}:floatConditionSideRollExt.outFloat", f"{nspc}:floatMathSideRollExt.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRollExterior", f"{nspc}:floatMathSideRollExt.floatB")

#connect value to exterior_BUF rotZ
cmds.connectAttr(f"{nspc}:floatMathSideRollExt.outFloat", f"{nspc}:exterior_BUF.rotateZ")


#create float logic node, verify if the value is <=, connect it properly
cmds.shadingNode( "floatLogic", au=True, n="floatLogicSideRollInt" )
cmds.setAttr(f"{nspc}:floatLogicSideRollInt.operation", 5)
cmds.setAttr(f"{nspc}:floatLogicSideRollInt.floatB", 0)
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRoll", f"{nspc}:floatLogicSideRollInt.floatA")


cmds.shadingNode( "floatCondition", au=True, n="floatConditionSideRollInt" )
cmds.connectAttr(f"{nspc}:floatLogicSideRollInt.outBool", f"{nspc}:floatConditionSideRollInt.condition")
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRoll", f"{nspc}:floatConditionSideRollInt.floatA")

#create foat Math node to add side Roll Interior and side roll value before applying it to the interior_BUF rotZ value
cmds.shadingNode( "floatMath", au=True, n="floatMathSideRollInt" )
cmds.connectAttr(f"{nspc}:floatConditionSideRollInt.outFloat", f"{nspc}:floatMathSideRollInt.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.sideRollInterior", f"{nspc}:floatMathSideRollInt.floatB")

#connect value to Interior_BUF rotZ
cmds.connectAttr(f"{nspc}:floatMathSideRollInt.outFloat", f"{nspc}:interior_BUF.rotateZ")



#Foot Roll
#Foot roll heel 
cmds.shadingNode( "floatMath", au=True, n="negateFootRollBreak")
cmds.setAttr(f"{nspc}:negateFootRollBreak.operation", 2)
cmds.setAttr(f"{nspc}:negateFootRollBreak.floatB", -1)
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollHeelBreak", f"{nspc}:negateFootRollBreak.floatA")

cmds.shadingNode( "clamp", au=True, n="clampFootRollHeel" )
cmds.connectAttr(f"{nspc}:negateFootRollBreak.outFloat", f"{nspc}:clampFootRollHeel.minR")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRoll", f"{nspc}:clampFootRollHeel.inputR")

cmds.shadingNode( "floatMath", au=True, n="floatMathFootRollHeel" )
cmds.setAttr(f"{nspc}:floatMathFootRollHeel.operation", 0)
cmds.connectAttr(f"{nspc}:clampFootRollHeel.outputR", f"{nspc}:floatMathFootRollHeel.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollHeel", f"{nspc}:floatMathFootRollHeel.floatB")

cmds.connectAttr(f"{nspc}:floatMathFootRollHeel.outFloat", f"{nspc}:heel_BUF.rotateX")


#foot Roll Mid Foot
#instance and connect floatMaths addition
cmds.shadingNode( "floatMath", au=True, n="addBreakFoots")
cmds.setAttr(f"{nspc}:addBreakFoots.operation", 0)
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollEndFootBreak", f"{nspc}:addBreakFoots.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:addBreakFoots.floatB")

#instance and connect floatLogic
cmds.shadingNode( "floatLogic", au=True, n="floatLogicFootRollMidFoot" )
cmds.setAttr(f"{nspc}:floatLogicFootRollMidFoot.operation", 4)
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRoll", f"{nspc}:floatLogicFootRollMidFoot.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:floatLogicFootRollMidFoot.floatB")

#instance and connect setRange
cmds.shadingNode( "setRange", au=True, n="setRangeMidFoot" )
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:setRangeMidFoot.maxX")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:setRangeMidFoot.minY")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:setRangeMidFoot.oldMaxX")
cmds.connectAttr(f"{nspc}:addBreakFoots.outFloat", f"{nspc}:setRangeMidFoot.oldMaxY")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:setRangeMidFoot.oldMinY")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRoll", f"{nspc}:setRangeMidFoot.valueX")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRoll", f"{nspc}:setRangeMidFoot.valueY")

#instance and connect floatCondition
cmds.shadingNode( "floatCondition", au=True, n="floatConditionFootRollMidFoot")
cmds.connectAttr(f"{nspc}:floatLogicFootRollMidFoot.outBool", f"{nspc}:floatConditionFootRollMidFoot.condition")
cmds.connectAttr(f"{nspc}:setRangeMidFoot.outValueX", f"{nspc}:floatConditionFootRollMidFoot.floatA")
cmds.connectAttr(f"{nspc}:setRangeMidFoot.outValueY", f"{nspc}:floatConditionFootRollMidFoot.floatB")

#instance and connect floatMathMidFoot addition
cmds.shadingNode( "floatMath", au=True, n="floatMathMidFoot")
cmds.setAttr(f"{nspc}:floatMathMidFoot.operation", 0)
cmds.connectAttr(f"{nspc}:floatConditionFootRollMidFoot.outFloat", f"{nspc}:floatMathMidFoot.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFoot", f"{nspc}:floatMathMidFoot.floatB")

#connect final result to midFoot_BUF
cmds.connectAttr(f"{nspc}:floatMathMidFoot.outFloat", f"{nspc}:midFoot_BUF.rotateX")


#Foot Roll End Toes
#create and connect setRangeEndFoot using the existing addBreakFoots node
cmds.shadingNode( "setRange", au=True, n="setRangeEndFoot" )
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollEndFootBreak", f"{nspc}:setRangeEndFoot.maxX")
cmds.connectAttr(f"{nspc}:addBreakFoots.outFloat", f"{nspc}:setRangeEndFoot.oldMaxX")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollMidFootBreak", f"{nspc}:setRangeEndFoot.oldMinX")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRoll", f"{nspc}:setRangeEndFoot.valueX")

cmds.shadingNode( "floatMath", au=True, n="floatMathEndFoot" )
cmds.setAttr(f"{nspc}:floatMathEndFoot.operation", 0)
cmds.connectAttr(f"{nspc}:setRangeEndFoot.outValueX", f"{nspc}:floatMathEndFoot.floatA")
cmds.connectAttr(f"{nspc}:ikFoot_CON.footRollEndFoot", f"{nspc}:floatMathEndFoot.floatB")

cmds.connectAttr(f"{nspc}:floatMathEndFoot.outFloat", f"{nspc}:endToes_BUF.rotateX")

#######################


#create all foot constraints to verify /!\
cmds.ikHandle( sj=f'{nspc}:femur_JNT', ee=f'{nspc}:ankle_JNT', p=1, w=1, pw=1, n="ikHandleFemur" )
cmds.ikHandle( sj=f'{nspc}:ankle_JNT', ee=f'{nspc}:midFoot_JNT', p=1, w=1, pw=1, n="ikHandleAnckle" )
cmds.ikHandle( sj=f'{nspc}:midFoot_JNT', ee=f'{nspc}:endToes_JNT', p=1, w=1, pw=1, n= "ikHandleToes")
cmds.poleVectorConstraint( f"{nspc}:ikUpVector_CON", f"{nspc}:ikHandleFemur", n="poleVectorConstraintVectorIKHandleFemur" ) 
cmds.parentConstraint(f"{nspc}:ikAnkle_BUF", f"{nspc}:ikHandleFemur", mo=False, n="parentConstraintIKHandleFemur")
cmds.parentConstraint(f"{nspc}:endToes_BUF", f"{nspc}:ikHandleToes", mo=False, n="parentConstraintIKHandleToes")
cmds.parentConstraint(f"{nspc}:midFoot_BUF", f"{nspc}:ikHandleAnckle", mo=False, n="parentConstraintIKHandleAnckle")


# /!\ verify with teacher #supposed to be OK 
cmds.poleVectorConstraint( f"{nspc}:upVectorIKToes_BUF", f"{nspc}:ikHandleToes", n="poleVectorConstraintIKHandleToes" )
cmds.poleVectorConstraint( f"{nspc}:upVectorIKAnckle_BUF", f"{nspc}:ikHandleAnckle", n="poleVectorConstraintIKHandleAnckle" )

#place ikHandles in the right place 
cmds.parent( f'{nspc}:ikHandleFemur', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:ikHandleAnckle', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:ikHandleToes', f'{nspc}:hidden' )

cmds.parent( f'{nspc}:parentConstraintIKHandleToes', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:parentConstraintIKHandleAnckle', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:parentConstraintIKHandleFemur', f'{nspc}:hidden' )

cmds.parent( f'{nspc}:poleVectorConstraintVectorIKHandleFemur', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:poleVectorConstraintIKHandleToes', f'{nspc}:hidden' )
cmds.parent( f'{nspc}:poleVectorConstraintIKHandleAnckle', f'{nspc}:hidden' )

cmds.delete( "femur_GUID1", "tibia_GUID1", "ankle_GUID1", "endToes_GUID1", "ikUpVectorLeg_GUID1", "heel_GUID1", "midFoot_GUID1", "midToes_GUID1", "exterior_GUID1", "interior_GUID1", "upVectorIKToes_GUID1", "upVectorIKAnkle_GUID1" )

#Add space switch receiver
cmds.group(n="IKUpVectorSpaceSwitch_BUF", em=True)
cmds.matchTransform(f"{nspc}:IKUpVectorSpaceSwitch_BUF" , f"{nspc}:ikUpVectorParentAttach_BUF")
cmds.parent(f"{nspc}:IKUpVectorSpaceSwitch_BUF", f"{nspc}:ikUpVectorParentAttach_BUF")
cmds.parent(f"{nspc}:ikUpVector_CON", f"{nspc}:IKUpVectorSpaceSwitch_BUF")

cmds.setAttr ( f"{nspc}:IKUpVectorSpaceSwitch_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:IKUpVectorSpaceSwitch_BUF " + ".outlinerColor" , 255,255,0)

#set back the namespace in default  
cmds.namespace( set=':')
