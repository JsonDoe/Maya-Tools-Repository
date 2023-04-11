

import maya.cmds as cmds

# place the suffix you want to add between '  '
suffix = '_MI'

# List all selected objects
sel = cmds.ls(sl=1)

# For each item in the list add the suffix
for item in sel:
    cmds.rename(item,'{0}{1}'.format(item,suffix))