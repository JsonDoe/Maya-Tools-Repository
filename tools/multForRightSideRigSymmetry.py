import maya.cmds as cmds 

#MULT all by -1 except ty and tZ, then rotate Y all by 180 to get the proper invert axis to animate 

selections = cmds.ls(sl=True)
for item in selections:
    cmds.setAttr(f"{item}.tx", cmds.getAttr(f"{item}.tx") *-1)
    cmds.setAttr(f"{item}.rx", cmds.getAttr(f"{item}.rx") *-1)
    cmds.setAttr(f"{item}.ry", cmds.getAttr(f"{item}.ry") *-1)
    cmds.setAttr(f"{item}.rz", cmds.getAttr(f"{item}.rz") *-1)

    current_rotateY = cmds.getAttr(item + '.rotateY')
    new_rotateY = current_rotateY + 180
    cmds.setAttr(item + '.rotateY', new_rotateY)




