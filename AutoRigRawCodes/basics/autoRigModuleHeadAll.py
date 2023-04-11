#autoRigHeadOnly

import maya.cmds as cmds 

#set namespace variable 
nspc = 'head'

#initiate namespace
cmds.namespace( add=f'{nspc}')
cmds.namespace( set=f'{nspc}')

#duplicate _CON 
cmds.duplicate( "referenceHead1_CON", n="baseNeck_CON") 
cmds.duplicate( "referenceHead1_CON", n="neck_CON") 
cmds.duplicate( "referenceHead1_CON", n="head_CON") 
cmds.duplicate( "referenceHead2_CON", n="jaw_CON") 

cmds.rename( "R_eyeLookAt_CON", ":head:R_eyeLookAt_CON" )
cmds.rename( "L_eyeLookAt_CON", ":head:L_eyeLookAt_CON" )
cmds.rename( "lookAt_CON", ":head:lookAt_CON" )

#create module groups 
cmds.group( em=True, n="module")
cmds.group( em=True, n="controllers")
cmds.group( em=True, n="joints")
cmds.group( em=True, n="hidden")
cmds.group( em=True, n="parentAttach_BUF")
cmds.matchTransform(f"{nspc}:parentAttach_BUF","baseNeck_GUID")

cmds.group( em=True, n="R_eyeLookAt_BUF")
cmds.group( em=True, n="R_eyePivot_BUF")
cmds.group( em=True, n="R_eyeUpVector_BUF")
cmds.group( em=True, n="L_eyeLookAt_BUF")
cmds.group( em=True, n="L_eyePivot_BUF")
cmds.group( em=True, n="L_eyeUpVector_BUF")
cmds.group( em=True, n="lookAtParentAttach_BUF")


#Structure hierarchy
cmds.parent( f"{nspc}:controllers", f"{nspc}:module")
cmds.parent( f"{nspc}:joints", f"{nspc}:module")
cmds.parent( f"{nspc}:hidden", f"{nspc}:module")
cmds.parent( f"{nspc}:parentAttach_BUF ", f"{nspc}:controllers")
cmds.parent( f"{nspc}:lookAtParentAttach_BUF", f"{nspc}:controllers")
#parent head controllers
cmds.parent( f"{nspc}:neck_CON", f"{nspc}:baseNeck_CON" )
cmds.parent( f"{nspc}:head_CON", f"{nspc}:neck_CON" )
cmds.parent( f"{nspc}:jaw_CON", f"{nspc}:head_CON" )
cmds.parent( f"{nspc}:baseNeck_CON", f"{nspc}:parentAttach_BUF")


#parent look at controllers
cmds.parent( f"{nspc}:R_eyePivot_BUF", f"{nspc}:head_CON" )
cmds.parent( f"{nspc}:R_eyeLookAt_BUF", f"{nspc}:R_eyePivot_BUF" )
cmds.parent( f"{nspc}:R_eyeUpVector_BUF", f"{nspc}:head_CON")

#parent look at buffers
cmds.parent( f"{nspc}:L_eyePivot_BUF", f"{nspc}:head_CON" )
cmds.parent( f"{nspc}:L_eyeLookAt_BUF", f"{nspc}:L_eyePivot_BUF" )
cmds.parent( f"{nspc}:L_eyeUpVector_BUF", f"{nspc}:head_CON")


cmds.parent( f"{nspc}:R_eyeLookAt_CON", f"{nspc}:lookAt_CON" )
cmds.parent( f"{nspc}:L_eyeLookAt_CON", f"{nspc}:lookAt_CON" )
cmds.parent( f"{nspc}:lookAt_CON", f"{nspc}:lookAtParentAttach_BUF" )

#color _BUF groups the proper colors
cmds.setAttr ( f"{nspc}:parentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:parentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:lookAtParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:lookAtParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:R_eyeLookAt_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:R_eyeLookAt_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:R_eyePivot_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:R_eyePivot_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:R_eyeUpVector_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:R_eyeUpVector_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:L_eyeLookAt_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:L_eyeLookAt_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:L_eyePivot_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:L_eyePivot_BUF" + ".outlinerColor" , 0,100,100)


cmds.setAttr ( f"{nspc}:L_eyeUpVector_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:L_eyeUpVector_BUF" + ".outlinerColor" , 0,100,100)


#create joints 
cmds.joint(n="baseNeck_JNT")
cmds.joint(n="neck_JNT")
cmds.joint(n="head_JNT")
cmds.joint(n="jaw_JNT")
cmds.joint(n="R_eye_JNT")
cmds.joint(n="L_eye_JNT")


#Parent joints 
cmds.parent( f"{nspc}:baseNeck_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:R_eye_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:L_eye_JNT", f"{nspc}:joints")



#match transfo Objs with _GUIDs
cmds.matchTransform(f"{nspc}:baseNeck_JNT","baseNeck_GUID")
cmds.matchTransform(f"{nspc}:neck_JNT","neck_GUID")
cmds.matchTransform(f"{nspc}:head_JNT","head_GUID")
cmds.matchTransform(f"{nspc}:jaw_JNT","jaw_GUID")

#match head controllers with joints 
cmds.matchTransform(f"{nspc}:baseNeck_CON", f"{nspc}:baseNeck_JNT")
cmds.matchTransform(f"{nspc}:neck_CON", f"{nspc}:neck_JNT")
cmds.matchTransform(f"{nspc}:head_CON", f"{nspc}:head_JNT")
cmds.matchTransform(f"{nspc}:jaw_CON", f"{nspc}:jaw_JNT")

#match transfo Objs with _GUIDs for eyes

#joints
cmds.matchTransform(f"{nspc}:R_eye_JNT","R_eye_GUID")
cmds.matchTransform(f"{nspc}:L_eye_JNT","L_eye_GUID")

#buffers
cmds.matchTransform(f"{nspc}:R_eyePivot_BUF","R_eye_GUID")
cmds.matchTransform(f"{nspc}:R_eyeLookAt_BUF","R_eye_GUID")
cmds.matchTransform(f"{nspc}:R_eyeUpVector_BUF","R_eyeUpVector_GUID")


cmds.matchTransform(f"{nspc}:L_eyePivot_BUF","L_eye_GUID")
cmds.matchTransform(f"{nspc}:L_eyeLookAt_BUF","L_eye_GUID")
cmds.matchTransform(f"{nspc}:L_eyeUpVector_BUF","L_eyeUpVector_GUID")

#controllers
cmds.matchTransform(f"{nspc}:lookAt_CON","lookAt_GUID")
cmds.matchTransform(f"{nspc}:R_eyeLookAt_CON","R_eyeLookAt_GUID")
cmds.matchTransform(f"{nspc}:L_eyeLookAt_CON","L_eyeLookAt_GUID")


#create constraints 

cmds.parentConstraint(f"{nspc}:baseNeck_CON",f"{nspc}:baseNeck_JNT", mo=False)
cmds.parentConstraint(f"{nspc}:neck_CON",f"{nspc}:neck_JNT", mo=False)
cmds.parentConstraint(f"{nspc}:head_CON",f"{nspc}:head_JNT", mo=False)
cmds.parentConstraint(f"{nspc}:jaw_CON",f"{nspc}:jaw_JNT", mo=False)

cmds.scaleConstraint(f"{nspc}:baseNeck_CON",f"{nspc}:baseNeck_JNT", mo=False)
cmds.scaleConstraint(f"{nspc}:neck_CON",f"{nspc}:neck_JNT", mo=False)
cmds.scaleConstraint(f"{nspc}:head_CON",f"{nspc}:head_JNT", mo=False)
cmds.scaleConstraint(f"{nspc}:jaw_CON",f"{nspc}:jaw_JNT", mo=False)

cmds.aimConstraint( f"{nspc}:R_eyeLookAt_CON ", f"{nspc}:R_eyeLookAt_BUF", aimVector=(0,0,1), upVector = (0,1,0), worldUpObject=(f"{nspc}:R_eyeUpVector_BUF"))
cmds.aimConstraint( f"{nspc}:L_eyeLookAt_CON ", f"{nspc}:L_eyeLookAt_BUF", aimVector=(0,0,1), upVector = (0,1,0), worldUpObject=(f"{nspc}:L_eyeUpVector_BUF"))

cmds.parentConstraint( f"{nspc}:R_eyeLookAt_BUF", f"{nspc}:R_eye_JNT", mo=False )
cmds.parentConstraint( f"{nspc}:L_eyeLookAt_BUF", f"{nspc}:L_eye_JNT", mo=False )

cmds.scaleConstraint( f"{nspc}:R_eyeLookAt_BUF", f"{nspc}:R_eye_JNT", mo=False )
cmds.scaleConstraint( f"{nspc}:L_eyeLookAt_BUF", f"{nspc}:L_eye_JNT", mo=False )


cmds.delete( "baseNeck_GUID", "neck_GUID" , "head_GUID" , "jaw_GUID", "referenceHead1_CON", "referenceHead2_CON", "R_eyeLookAt_GUID", "L_eyeLookAt_GUID", "L_eye_GUID", "R_eye_GUID", "R_eyeUpVector_GUID", "L_eyeUpVector_GUID", "lookAt_GUID" )

cmds.namespace( set=":")

