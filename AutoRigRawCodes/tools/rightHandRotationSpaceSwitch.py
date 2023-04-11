import maya.cmds as cmds 

#rightHandRotationSpaceSwitch
nspc="R_arm"

cmds.namespace( set=f"{nspc}")

cmds.parentConstraint(f"{nspc}:clavicleRotationSpace_BUF", f"{nspc}:ikHandSpaceSwitch_BUF", n="rightHandSpaceSwitch_paCns", mo= True),
cmds.parentConstraint("spine:chestRotationSpace_BUF", f"{nspc}:ikHandSpaceSwitch_BUF", n="rightHandSpaceSwitch_paCns", mo= True)
cmds.parentConstraint("spine:upperBodyRotationSpace_BUF", f"{nspc}:ikHandSpaceSwitch_BUF", n="rightHandSpaceSwitch_paCns", mo= True)
cmds.parentConstraint("head:headSpaceSwitchSender_BUF", f"{nspc}:ikHandSpaceSwitch_BUF", n="rightHandSpaceSwitch_paCns", mo= True)
cmds.parentConstraint("SRT:local_CON", f"{nspc}:ikHandSpaceSwitch_BUF", n="rightHandSpaceSwitch_paCns", mo= True)

cmds.createNode("floatLogic", n="checkHandSpaceStatus1")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus1.operation", 0)
cmds.connectAttr("SRT:setup_BUF.rightHandRotationSpaceSwitch",f"{nspc}:checkHandSpaceStatus1.floatA")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus1.floatB", 1 )
cmds.connectAttr(f"{nspc}:checkHandSpaceStatus1.outBool", f"{nspc}:rightHandSpaceSwitch_paCns.clavicleRotationSpace_BUFW0" )

cmds.createNode("floatLogic", n="checkHandSpaceStatus2")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus2.operation", 0)
cmds.connectAttr("SRT:setup_BUF.rightHandRotationSpaceSwitch",f"{nspc}:checkHandSpaceStatus2.floatA")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus2.floatB", 2 )
cmds.connectAttr(f"{nspc}:checkHandSpaceStatus2.outBool", f"{nspc}:rightHandSpaceSwitch_paCns.chestRotationSpace_BUFW1" )

cmds.createNode("floatLogic", n="checkHandSpaceStatus3")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus3.operation", 0)
cmds.connectAttr("SRT:setup_BUF.rightHandRotationSpaceSwitch",f"{nspc}:checkHandSpaceStatus3.floatA")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus3.floatB", 3 )
cmds.connectAttr(f"{nspc}:checkHandSpaceStatus3.outBool", f"{nspc}:rightHandSpaceSwitch_paCns.upperBodyRotationSpace_BUFW2" )

cmds.createNode("floatLogic", n="checkHandSpaceStatus4")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus4.operation", 0)
cmds.connectAttr("SRT:setup_BUF.rightHandRotationSpaceSwitch",f"{nspc}:checkHandSpaceStatus4.floatA")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus4.floatB", 4 )
cmds.connectAttr(f"{nspc}:checkHandSpaceStatus4.outBool", f"{nspc}:rightHandSpaceSwitch_paCns.headSpaceSwitchSender_BUFW3" )

cmds.createNode("floatLogic", n="checkHandSpaceStatus5")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus5.operation", 0)
cmds.connectAttr("SRT:setup_BUF.rightHandRotationSpaceSwitch",f"{nspc}:checkHandSpaceStatus5.floatA")
cmds.setAttr(f"{nspc}:checkHandSpaceStatus5.floatB", 5 )
cmds.connectAttr(f"{nspc}:checkHandSpaceStatus5.outBool", f"{nspc}:rightHandSpaceSwitch_paCns.local_CONW4")


cmds.namespace( set=":")