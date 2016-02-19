import maya.cmds as cmds


# clear up the scene
cmds.select(all=True)
cmds.delete()

branch=cmds.polyCylinder()
cylHeight=cmds.getAttr(branch[1]+'.height')
#forward on local y axis
cmds.move(0,cylHeight/2,0)

bbox = cmds.exactWorldBoundingBox(branch)
bottom = [(bbox[0]+bbox[3])/2, bbox[1], (bbox[2]+bbox[5])/2] #(xmin,xmax)/2 , (zmin,zmax)/2
#now set pivot to the bottom of the cylinder
cmds.xform(branch[0], piv=bottom, ws=True)
cmds.rotate(45,0,0)

#save pos,rot
curPos=cmds.xform(branch[0], translation=True, query=True)
curRot=cmds.xform(branch[0], rotation=True, query=True)

#create a second one
branch2=cmds.polyCylinder()
cylHeight2=cmds.getAttr(branch2[1]+'.height')

#move to where we were before
cmds.move(curPos[0],curPos[1],curPos[2])

#set its rotation pivot to the bottom
bbox = cmds.exactWorldBoundingBox(branch2)
bottom = [(bbox[0]+bbox[3])/2, bbox[1], (bbox[2]+bbox[5])/2] #(xmin,xmax)/2 , (zmin,zmax)/2
#now set pivot to the bottom of the cylinder
cmds.xform(branch2[0], piv=bottom, ws=True)

#rotate to where we were before
cmds.rotate(curRot[0],curRot[1],curRot[2])

#forward on local y axis
cmds.move(curPos[0],curPos[1]+cylHeight2/2,curPos[2] ,os=True, r=True)

#perform another rotation (if wanted)
cmds.rotate(curRot[0],curRot[1]+45,curRot[2])

