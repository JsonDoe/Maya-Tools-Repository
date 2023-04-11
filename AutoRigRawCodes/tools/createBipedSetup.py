import maya.cmds as cmds
from frankenstein import RigUtils
from maya.api     import OpenMaya

cmds.namespace( set='SRT')


ru                  = RigUtils()
ctrl                = ru.createRigController(13)
ctrl.color          = OpenMaya.MColor(227,61,148,1)
ctrl.transparency   = 0.1
ctrl.globalScale    = 1
ctrl.wireWidth      = 1  
ctrl.name           = "setup_BUF"

cmds.select( "SRT:setup_BUF" )

#set the setup attributes 
#leftArm
cmds.addAttr( at="float", ln="leftB1Length",        nn="Left B1 Length",                            dv=4, k=True)
cmds.addAttr( at="float", ln="leftB2Length",        nn="Left B2 Length",                            dv=4, k=True)

cmds.addAttr( at="float", ln="leftB1Scale",         nn="Left B1 Scale",                             dv=1, k=True)
cmds.addAttr( at="float", ln="leftB2Scale",         nn="Left B2 Scale",                             dv=1, k=True)

cmds.addAttr( at="float", ln="leftStretch",         nn="Left Stretch",              min=0, max=1,   dv=0, k=True)

cmds.addAttr( at="float", ln="leftGlobalScale",     nn="Left Global Scale",                         dv=1, k=True)

cmds.addAttr( at="float", ln="leftBlendFKIK",       nn="Left Blend FK <-> IK",      min=0, max=1,   dv=0, k=True)

#Rarm
cmds.addAttr( at="float", ln="rightB1Length",       nn="Right B1 Length",                           dv=4,               k=True)
cmds.addAttr( at="float", ln="rightB2Length",       nn="Right B2 Length",                           dv=4,               k=True)
cmds.addAttr( at="float", ln="rightB1Scale",        nn="Right B1 Scale",                            dv=1,               k=True)
cmds.addAttr( at="float", ln="rightB2Scale",        nn="Right B2 Scale",                            dv=1,               k=True)
cmds.addAttr( at="float", ln="rightStretch",        nn="Right Stretch",             min=0, max=1,   dv=0,               k=True)
cmds.addAttr( at="float", ln="rightGlobalScale",    nn="Right Global Scale",                        dv=1,               k=True)
cmds.addAttr( at="float", ln="rightBlendFKIK",      nn="Right Blend FK <-> IK",     min=0, max=1,   dv=0,               k=True)

#spine
cmds.addAttr( at="float", ln="restLength",          nn="Rest Length" ,                              dv=4.8,             k=True)
cmds.addAttr( at="long",  ln="bonesCount",          nn="Bones Count" ,                              dv=6,               k=True)
cmds.addAttr( at="float", ln="maxStretchFactor",    nn="Max Stretch Factor" ,                       dv=1.2,             k=True)
cmds.addAttr( at="float", ln="minStretchFactor",    nn="Min Stretch Factor" ,                       dv=0.8,             k=True)
cmds.addAttr( at="float", ln="stretchScale",        nn="Stretch Scale" ,                            dv=0.2,             k=True)
cmds.addAttr( at="float", ln="squashScale",         nn="Squash Scale" ,                             dv=2,               k=True)

#SpaceSwitchs
#toAdd : 'leftHandRotationSpaceSwitch', 'lookAtRotationSpaceSwitch', 'leftArmIKUpVectorSpaceSwitch', 'LeftLegIKUpVectorSpaceSwitch', 'RightLegIKUpVectorSpaceSwitch', 
# 'RightArmIKUpVectorSpaceSwitch', 'rightHandRotationSpaceSwitch']
cmds.addAttr( at="enum", ln="leftHandRotationSpaceSwitch",      nn="Left Hand Rotation Space Switch",       en="hand:clavicle:chest:upperBody:head:world:" ,    dv=0,  k=True)
cmds.addAttr( at="enum", ln="leftArmIKUpVectorSpaceSwitch",     nn="Left Arm IK UpVector Space Switch",     en="world:hand:" ,    dv=0,  k=True)

cmds.addAttr( at="enum", ln="rightHandRotationSpaceSwitch",      nn="Right Hand Rotation Space Switch",       en="hand:clavicle:chest:upperBody:head:world:" ,    dv=0,  k=True)
cmds.addAttr( at="enum", ln="rightArmIKUpVectorSpaceSwitch",     nn="Right Arm IK UpVector Space Switch",     en="world:hand:" ,    dv=0,  k=True)


cmds.addAttr( at="enum", ln="lookAtRotationSpaceSwitch",        nn="Look At Rotation Space Switch",           en="world:head:" ,    dv=0,  k=True)
cmds.addAttr( at="enum", ln="headRotationSpaceSwitch",          nn="Head Rotation Space Switch",              en="neck:chest:upperBody:world:" ,    dv=0,  k=True)


cmds.addAttr( at="enum", ln="leftLegIKUpVectorSpaceSwitch",     nn="Left Leg IK Up Vector Space Switch",    en="world:foot:" ,    dv=0,  k=True)
cmds.addAttr( at="enum", ln="rightLegIKUpVectorSpaceSwitch",    nn="Right Leg IK Up Vector Space Switch",   en="world:foot:" ,    dv=0,  k=True)


cmds.addAttr( at="enum", ln="rigState",             nn="Rig State",             en="rig:Anim:" ,    dv=0,               k=True)


leftBone1Length = (cmds.getAttr("L_arm:radius_FK_CON.translateX") ) 
cmds.setAttr("SRT:setup_BUF.leftB1Length", leftBone1Length )

leftBone2Length = (cmds.getAttr("L_arm:wrist_FK_CON.translateX") ) 
cmds.setAttr("SRT:setup_BUF.leftB2Length", leftBone2Length )

rightBone1Length = (cmds.getAttr("R_arm:radius_FK_CON.translateX") ) 
cmds.setAttr("SRT:setup_BUF.rightB1Length", rightBone1Length )

rightBone2Length = (cmds.getAttr("R_arm:wrist_FK_CON.translateX") ) 
cmds.setAttr("SRT:setup_BUF.rightB2Length", rightBone2Length )

restLength = (cmds.getAttr("spine:hipsDepth_CON.translateY") ) * 4
cmds.setAttr("SRT:setup_BUF.restLength", restLength )

