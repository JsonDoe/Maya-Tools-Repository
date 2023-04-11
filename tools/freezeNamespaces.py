import maya.cmds as cmds

def freezeNSPC():

    """ freeze the namespaces then delete them
    Arg: 
        allObjs         list(str)   : list of the objs of the scene

    Return: None

    """


    #Set namespace to root to avoid errors
    cmds.namespace(set=":")

    #create a list containing all OBJs excluding shapes
    allObjs=cmds.ls(obj for obj in cmds.ls() if cmds.nodeType(obj) != "mesh")

    #loop function to rename objs containing ":"
    for obj in allObjs:
        if(obj.find(":") != -1):
            newName = obj.replace(":", "_")
            cmds.rename(obj, newName)


    #delete namespaces
    # Collect all namespaces except for the Maya built ins.
    all_namespaces = [x for x in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True) if x != "UI" and x != "shared"]

    if all_namespaces:
        # Sort by hierarchy, deepest first.
        all_namespaces.sort(key=len, reverse=True)
        for namespace in all_namespaces:
            # When a deep namespace is removed, it also removes the root. So check here to see if these still exist.
            if cmds.namespace(exists=namespace) is True:
                cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=True)
        


freezeNSPC()
