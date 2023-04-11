#autoRigModuleSpine.py

import maya.cmds as cmds 

#set namespace variable 
nspc = 'spine'

#initiate namespace
cmds.namespace( add=f'{nspc}')
cmds.namespace( set=f'{nspc}')

cmds.duplicate( "hips_CON", n="middle_CON") 
cmds.duplicate( "hipsDepth_CON", n="chestDepth_CON") 

cmds.rename("upperBody_CON", ":spine:upperBody_CON")
cmds.rename("hips_CON", ":spine:hips_CON" )
cmds.rename("hipsDepth_CON", ":spine:hipsDepth_CON" )
cmds.rename("chest_CON", ":spine:chest_CON")


#create module groups 
cmds.group( em=True, n="module")
cmds.group( em=True, n="controllers")
cmds.group( em=True, n="joints")
cmds.group( em=True, n="hidden")
cmds.group( em=True, n="parentAttachUpperBody_BUF")
cmds.group( em=True, n="childAttachLastVertebra_BUF")
cmds.group( em=True, n="childAttachFirstVertebra_BUF")

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

cmds.parent( f"{nspc}:upperBody_CON" , f"{nspc}:parentAttachUpperBody_BUF")
cmds.parent( f"{nspc}:hips_CON" , f"{nspc}:upperBody_CON" )
cmds.parent( f"{nspc}:hipsDepth_CON" , f"{nspc}:hips_CON" )

cmds.parent( f"{nspc}:middle_CON" , f"{nspc}:upperBody_CON" )
cmds.parent( f"{nspc}:chestDepth_CON" , f"{nspc}:middle_CON" )
cmds.parent( f"{nspc}:chest_CON" , f"{nspc}:chestDepth_CON" )

#match position of controllers with GUIDs
cmds.matchTransform(f"{nspc}:upperBody_CON","hips_GUID")
cmds.matchTransform(f"{nspc}:hips_CON","hips_GUID")
cmds.matchTransform(f"{nspc}:hipsDepth_CON","hipsDepth_GUID")
cmds.matchTransform(f"{nspc}:middle_CON","middle_GUID")
cmds.matchTransform(f"{nspc}:chestDepth_CON","chestDepth_GUID")
cmds.matchTransform(f"{nspc}:chest_CON","chest_GUID")

#create joints 
cmds.joint(n="spine001_JNT", p=(0, 0, 0) )
cmds.joint(n="spine002_JNT", p=(0, 0.804, 0) )
cmds.joint(n="spine003_JNT", p=(0, 1.608, 0) )
cmds.joint(n="spine004_JNT", p=(0, 2.412, 0) )
cmds.joint(n="spine005_JNT", p=(0, 3.216, 0) )
cmds.joint(n="spine006_JNT", p=(0, 4.020, 0) )

#Place joint in the right folder 
cmds.parent( f"{nspc}:spine001_JNT" , f"{nspc}:joints" )

#match joint with hips
cmds.matchTransform(f"{nspc}:spine001_JNT", f"{nspc}:hips_CON" )

#create curve
cmds.curve( p=[(0, 0, 0), (0, 1.5, 0), (0, 3, 0), (0, 4.5, 0), (0, 6, 0)], n="controlCurve")

#Place curve in the right folder 
cmds.parent(f"{nspc}:controlCurve", f"{nspc}:hidden")

#creat ikHandle for the spine joints
cmds.ikHandle( sol="ikSplineSolver", sj=f"{nspc}:spine001_JNT", ee=f"{nspc}:spine006_JNT", p=1, w=1, pw=1, n="ikHandleSpine" )

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

#connect elements with the ikHandle 
cmds.connectAttr( f"{nspc}:controlCurve.worldSpace[0]", f"{nspc}:ikHandleSpine.inCurve", f=True )

cmds.connectAttr( f"{nspc}:hips_CON.worldMatrix[0] ", f"{nspc}:ikHandleSpine.dWorldUpMatrix" )
cmds.connectAttr( f"{nspc}:chestDepth_CON.worldMatrix[0] ", f"{nspc}:ikHandleSpine.dWorldUpMatrixEnd" )


cmds.delete("hips_GUID", "hipsDepth_GUID", "middle_GUID", "chestDepth_GUID", "chest_GUID" )

cmds.namespace( set=":")
