import maya.cmds as cmds 
from maya.api     import OpenMaya
from frankenstein import RigUtils

#enter props name that will be used for the namespace
PropsName = "PropsName"

cmds.namespace( add=PropsName)
cmds.namespace( set=PropsName)

ru            = RigUtils()
ctrl          = ru.createRigController(8)
ctrl.color    = OpenMaya.MColor([1.0, 1.0, 0.0, 1.0])
ctrl.name     = 'global_CON'

ru            = RigUtils()
ctrl          = ru.createRigController(7)
ctrl.color    = OpenMaya.MColor([236.0, 65.0, 0.0, 1.0])
ctrl.name     = 'local_CON'


cmds.group( em=True, n='asset_rig')
cmds.group( em=True, n='meshes_GRP')
cmds.group( em=True, n='HI_GRP')
cmds.group( em=True, n='MI_GRP')
cmds.group( em=True, n='LO_GRP')
cmds.group( em=True, n='Technical_GRP')
cmds.group( em=True, n='rig_GRP')
cmds.group( em=True, n='bones_GRP')


cmds.group( em=True, n='module')
cmds.group( em=True, n='controllers')
cmds.group( em=True, n='joints')
cmds.group( em=True, n='hidden')

#Structure hierarchy

cmds.parent( "{PropsName}:meshes_GRP", "{PropsName}:asset_rig")
cmds.parent( "{PropsName}:rig_GRP", "{PropsName}:asset_rig")
cmds.parent( "{PropsName}:bones_GRP", "{PropsName}:asset_rig")
cmds.parent( "{PropsName}:HI_GRP", "{PropsName}:meshes_GRP")
cmds.parent( "{PropsName}:MI_GRP", "{PropsName}:meshes_GRP")
cmds.parent( "{PropsName}:LO_GRP", "{PropsName}:meshes_GRP")
cmds.parent( "{PropsName}:Technical_GRP", "{PropsName}:meshes_GRP")
cmds.parent( "{PropsName}:controllers", "{PropsName}:module")

cmds.parent( "{PropsName}:controllers", "{PropsName}:module")
cmds.parent( "{PropsName}:joints", "{PropsName}:module")
cmds.parent( "{PropsName}:hidden", "{PropsName}:module")
cmds.parent( "{PropsName}:parentAttach_BUF ", "{PropsName}:controllers")
cmds.parent( "{PropsName}:module ", "{PropsName}:rig_GRP")

cmds.setAttr ( "{PropsName}:parentAttach_BUF " + ".useOutlinerColor" , True)
cmds.setAttr ( "{PropsName}:parentAttach_BUF " + ".outlinerColor" , 0,1,0)

cmds.parent( "{PropsName}:local_CON ", "{PropsName}:global_CON")
cmds.parent( "{PropsName}:global_CON ", "{PropsName}:parentAttach_BUF")

