#autoRigModuleLeg.py

#to add : create _CON without Frankenstein

#autoRig L_Leg 
import maya.cmds as cmds

#set namespace variable 
nspc = "L_Leg"

#initiate namespace
cmds.namespace( add=f"{nspc}")
cmds.namespace( set=f"{nspc}")

#add _CON to namespace 
cmds.rename( "ikFoot_CON", ":L_Leg:ikFoot_CON" )
cmds.rename( "ikUpVectorLeg_CON", ":L_Leg:ikUpVector_CON" )

#create module groups with the proper naming 
cmds.group( em=True, n="module")
cmds.group( em=True, n="controllers")
cmds.group( em=True, n="joints")
cmds.group( em=True, n="hidden")
cmds.group( em=True, n="ikFootParentAttach_BUF ")
cmds.group( em=True, n="ikUpVectorParentAttach_BUF")
cmds.group( em=True, n="parentAttach_BUF ")
cmds.group( em=True, n="heel_BUF")
cmds.group( em=True, n="endFoot_BUF")
cmds.group( em=True, n="midFoot_BUF")
cmds.group( em=True, n="ikAnkle_BUF")

#Structure hierarchy
cmds.parent( f"{nspc}:controllers", f"{nspc}:module")
cmds.parent( f"{nspc}:joints", f"{nspc}:module")
cmds.parent( f"{nspc}:hidden", f"{nspc}:module")
cmds.parent( f"{nspc}:parentAttach_BUF ", f"{nspc}:controllers")
cmds.parent( f"{nspc}:ikUpVectorParentAttach_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:ikFootParentAttach_BUF", f"{nspc}:controllers")

#Structure Foot roll hierarchy 
cmds.parent( f"{nspc}:heel_BUF", f"{nspc}:ikFoot_CON")
cmds.parent( f"{nspc}:endFoot_BUF", f"{nspc}:heel_BUF")
cmds.parent( f"{nspc}:midFoot_BUF", f"{nspc}:endFoot_BUF")
cmds.parent( f"{nspc}:ikAnkle_BUF", f"{nspc}:midFoot_BUF")

#color _BUF groups the proper colors
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikFootParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikFootParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:heel_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:heel_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:endFoot_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:endFoot_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:midFoot_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:midFoot_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:ikAnkle_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikAnkle_BUF" + ".outlinerColor" , 0,100,100)

#create joints with the right naming and parent them together
cmds.joint(n="femur_JNT")
cmds.joint(n="tibia_JNT")
cmds.joint(n="ankle_JNT")
cmds.joint(n="midFoot_JNT")
cmds.joint(n="endFoot_JNT")


#parent joint with joint group
cmds.parent( f"{nspc}:femur_JNT", f"{nspc}:joints")

#parent _CON with buffers 
cmds.parent( f"{nspc}:ikFoot_CON", f"{nspc}:ikFootParentAttach_BUF" )
cmds.parent( f"{nspc}:ikUpVector_CON", f"{nspc}:ikUpVectorParentAttach_BUF" )


#match joints with the _GUID tools 
cmds.matchTransform(f"{nspc}:femur_JNT","femur_GUID")
cmds.matchTransform(f"{nspc}:tibia_JNT","tibia_GUID")
cmds.matchTransform(f"{nspc}:ankle_JNT","ankle_GUID")
cmds.matchTransform(f"{nspc}:midFoot_JNT","midFoot_GUID")
cmds.matchTransform(f"{nspc}:endFoot_JNT","endFoot_GUID")
cmds.matchTransform(f"{nspc}:ikFoot_CON", f"{nspc}:ankle_JNT")
cmds.matchTransform(f"{nspc}:ikUpVector_CON", "ikUpVectorLeg_GUID")

cmds.matchTransform(f"{nspc}:parentAttach_BUF", f"{nspc}:femur_JNT")

cmds.matchTransform(f"{nspc}:heel_BUF", "heel_GUID")
cmds.matchTransform(f"{nspc}:endFoot_BUF", f"{nspc}:endFoot_JNT")
cmds.matchTransform(f"{nspc}:midFoot_BUF", f"{nspc}:midFoot_JNT")
cmds.matchTransform(f"{nspc}:ikAnkle_BUF", f"{nspc}:ankle_JNT")


#create all foot constraints
cmds.ikHandle( sj=f"{nspc}:femur_JNT", ee=f"{nspc}:ankle_JNT", p=1, w=1, pw=1, n="ikHandleFemur" )
cmds.ikHandle( sj=f"{nspc}:ankle_JNT", ee=f"{nspc}:midFoot_JNT", p=1, w=1, pw=1, n="ikHandleAnckle" )
cmds.ikHandle( sj=f"{nspc}:midFoot_JNT", ee=f"{nspc}:endFoot_JNT", p=1, w=1, pw=1, n= "ikHandleToes")
cmds.parentConstraint(f"{nspc}:ikFoot_CON", f"{nspc}:ikHandleFemur", mo=False) 
cmds.poleVectorConstraint( f"{nspc}:ikUpVector_CON", f"{nspc}:ikHandleFemur" ) 
cmds.parentConstraint(f"{nspc}:endFoot_BUF", f"{nspc}:ikHandleToes", mo=False)
cmds.parentConstraint(f"{nspc}:midFoot_BUF", f"{nspc}:ikHandleAnckle", mo=False)
cmds.parentConstraint(f"{nspc}:ikAnkle_BUF", f"{nspc}:ikHandleFemur", mo=False)

#place ikHandles in the right place 
cmds.parent( f"{nspc}:ikHandleFemur", f"{nspc}:hidden" )
cmds.parent( f"{nspc}:ikHandleAnckle", f"{nspc}:hidden" )
cmds.parent( f"{nspc}:ikHandleToes", f"{nspc}:hidden" )

cmds.delete( "femur_GUID", "tibia_GUID", "ankle_GUID", "endFoot_GUID", "ikUpVectorLeg_GUID", "heel_GUID", "midFoot_GUID", "legGuid_GRP" )


cmds.select( f"{nspc}:ikFoot_CON" )
cmds.addAttr( at="float", ln="footRollHeel", nn="Foot Roll Heel", dv=0, k=True)
cmds.addAttr( at="float", ln="footRollMidFoot", nn="Foot Roll Mid Foot", dv=0, k=True)
cmds.addAttr( at="float", ln="footRollEndFoot", nn="Foot Roll End Foot", dv=0, k=True)

cmds.connectAttr( f"{nspc}:ikFoot_CON.footRollHeel", f"{nspc}:heel_BUF.rotateX" )
cmds.connectAttr( f"{nspc}:ikFoot_CON.footRollMidFoot", f"{nspc}:midFoot_BUF.rotateX" )
cmds.connectAttr( f"{nspc}:ikFoot_CON.footRollEndFoot", f"{nspc}:endFoot_BUF.rotateX" )
cmds.select( cl=True )

cmds.namespace( set=":")
