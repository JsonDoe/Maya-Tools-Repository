#autoRig L_arm 
import maya.cmds as cmds

#set namespace variable
nspc = 'L_arm'

#initiate namespace
cmds.namespace( add=f'{nspc}')
cmds.namespace( set=f'{nspc}')

#add _CON to namespace 
cmds.rename( "ikHand_CON", ":L_arm:ikHand_CON" )
cmds.rename( "ikUpVectorArm_CON", ":L_arm:ikUpVector_CON" )
cmds.rename( "clavicle_CON", ":L_arm:clavicle_CON" )

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

#create module groups with the proper naming 
cmds.group( em=True, n="module")
cmds.group( em=True, n="controllers")
cmds.group( em=True, n="joints")
cmds.group( em=True, n="hidden")
cmds.group( em=True, n="parentAttach_BUF ")
cmds.group( em=True, n="ikUpVectorParentAttach_BUF")
cmds.group( em=True, n="clavicleParentAttach_BUF")
cmds.group( em=True, n="handParentAttach_BUF")

#Structure hierarchy
cmds.parent( f"{nspc}:controllers", f"{nspc}:module")
cmds.parent( f"{nspc}:joints", f"{nspc}:module")
cmds.parent( f"{nspc}:hidden", f"{nspc}:module")
cmds.parent( f"{nspc}:parentAttach_BUF ", f"{nspc}:controllers")
cmds.parent( f"{nspc}:ikUpVectorParentAttach_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:clavicleParentAttach_BUF", f"{nspc}:controllers")
cmds.parent( f"{nspc}:handParentAttach_BUF" , f"{nspc}:controllers")

#color _BUF groups in green 
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:parentAttach_BUF " + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:ikUpVectorParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:clavicleParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:clavicleParentAttach_BUF" + ".outlinerColor" , 0,1,0)

cmds.setAttr ( f"{nspc}:handParentAttach_BUF" + ".useOutlinerColor" , True)
cmds.setAttr ( f"{nspc}:handParentAttach_BUF" + ".outlinerColor" , 0,100,100)

#create hand joints with the right naming and parent them together
cmds.joint(n="clavicle_JNT", rad=0.15)
cmds.joint(n="humerus_JNT", rad=0.15)
cmds.joint(n="radius_JNT", rad=0.15)
cmds.joint(n="wrist_JNT", rad=0.15)

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

#parent joint with joint group
cmds.parent( f"{nspc}:clavicle_JNT", f"{nspc}:joints")

#parent hand joints with joint group 
cmds.parent( f"{nspc}:metacarpalThumb_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:metacarpalIndex_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:metacarpalMajor_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:metacarpalAnnular_JNT", f"{nspc}:joints")
cmds.parent( f"{nspc}:metacarpalPinky_JNT", f"{nspc}:joints")

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

#parent _CON with buffers 
cmds.parent( f"{nspc}:clavicle_CON", f"{nspc}:clavicleParentAttach_BUF" )
cmds.parent( f"{nspc}:ikHand_CON", f"{nspc}:parentAttach_BUF " )
cmds.parent( f"{nspc}:ikUpVector_CON", f"{nspc}:ikUpVectorParentAttach_BUF" )

#parent controllers with Hand Parent Attach buffer 
cmds.parent( f"{nspc}:metacarpalThumb_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalIndex_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalMajor_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalAnnular_CON", f"{nspc}:handParentAttach_BUF")
cmds.parent( f"{nspc}:metacarpalPinky_CON", f"{nspc}:handParentAttach_BUF")
 

#match joints with the _GUID tools 
cmds.matchTransform(f"{nspc}:clavicle_JNT","clavicle_GUID")
cmds.matchTransform(f"{nspc}:humerus_JNT","humerus_GUID")
cmds.matchTransform(f"{nspc}:radius_JNT","radius_GUID")
cmds.matchTransform(f"{nspc}:wrist_JNT","wrist_GUID")
cmds.matchTransform(f"{nspc}:clavicle_CON",f"{nspc}:clavicle_JNT")
cmds.matchTransform(f"{nspc}:ikHand_CON", f"{nspc}:wrist_JNT")
cmds.matchTransform(f"{nspc}:ikUpVector_CON", "ikUpVectorArm_GUID")
cmds.matchTransform( f"{nspc}:handParentAttach_BUF", "wrist_GUID")


#create the clavicle/ikHand constraints.
cmds.orientConstraint(f"{nspc}:clavicle_CON", f"{nspc}:clavicle_JNT", mo=False) 
cmds.ikHandle( sj=f"{nspc}:humerus_JNT", ee=f"{nspc}:wrist_JNT", p=1, w=1, pw=1, n="ikHandleHumerusWrist" )

cmds.parentConstraint(f"{nspc}:ikHand_CON", f"{nspc}:ikHandleHumerusWrist", mo=False) 
cmds.poleVectorConstraint( f"{nspc}:ikUpVector_CON", f"{nspc}:ikHandleHumerusWrist" ) 

cmds.parent( f"{nspc}:ikHandleHumerusWrist", f"{nspc}:hidden" )

cmds.delete( "clavicle_GUID", "humerus_GUID", "radius_GUID", "wrist_GUID", "ikUpVectorArm_GUID", "armGuid_GRP" )
 
 
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
 

#delete _GUID and creation tools
cmds.delete("metacarpalThumb_GUID", "thumb001_GUID", "thumb002_GUID", "metacarpalMajor_GUID", "major001_GUID", "major002_GUID", "major003_GUID", "metacarpalAnnular_GUID", "annular001_GUID", "annular002_GUID", "annular003_GUID", "metacarpalPinky_GUID", "pinky001_GUID", "pinky002_GUID", "pinky003_GUID", "metacarpalIndex_GUID", "index001_GUID", "index002_GUID", "index003_GUID", "referenceFinger_CON")
 
#create constraints 
cmds.pointConstraint(f"{nspc}:wrist_JNT", f"{nspc}:handParentAttach_BUF", mo=False, n="pointConstraintWrist")
cmds.orientConstraint( f"{nspc}:ikHand_CON", f"{nspc}:handParentAttach_BUF",mo=False, n="orientConstraintIkHand" )
 
#place constraints in the right file 
cmds.parent(f"{nspc}:pointConstraintWrist", f"{nspc}:hidden")
cmds.parent(f"{nspc}:orientConstraintIkHand", f"{nspc}:hidden")
 
cmds.namespace( set=":")
