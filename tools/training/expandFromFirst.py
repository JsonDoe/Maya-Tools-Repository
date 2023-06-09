#expandFromFirst.py 

import maya.cmds as cmds 

selectionList = cmds.ls( orderedSelection=True, type='transform')

if len( selectionList ) >= 2:

    targetName = selectionList[0]

    selectionList.remove( targetName )

    locatorGroupName = cmds.group( empty=True, n='expansion_locator_grp#' )

    maxExpansion = 100

    newAttributeName = 'expansion'

    if not cmds.objExists( '%s.%s' % ( targetName, newAttributeName ) ):

        cmds.select( targetName )

        cmds.addAttr( longName=newAttributeName, shortName='exp',
                        attributeType='double', min=0, max=maxExpansion, 
                        defaultValue=maxExpansion, keyable=True )

    for objectName in selectionList: 

        coords = cmds.getAttr( '%s.translate' % ( objectName ) )[0]

        locatorName = cmds.spaceLocator( position=coords, n='%s_loc#' % ( objectName ) )[0]

        cmds.xform ( locatorName, centerPivots=True )

        cmds.parent( locatorName, locatorGroupName )

    pointConstraintName = cmds.pointConstraint( [targetName, locatorName] , objectName, n='%s_pointConstraint#' % (objectName) )[0]


    cmds.xform( locatorGroupName , centerPivots=True )



else: 

    print('Print select two or more objects.')
