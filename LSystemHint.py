import maya.cmds as cmds
import math

# clear up the scene
cmds.select(all=True)
cmds.delete()
cmds.refresh()

#create a cylinder
branch=cmds.polyCylinder()
#get its height
cylHeight=cmds.getAttr(branch[1]+'.height')
#forward on local y axis
cmds.move(0,cylHeight/2,0)

#set its pivot to the bottom
bbox = cmds.exactWorldBoundingBox(branch)
bottom = [(bbox[0]+bbox[3])/2, bbox[1], (bbox[2]+bbox[5])/2] #(xmin,xmax)/2 , (zmin,zmax)/2
#now set pivot to the bottom of the cylinder
cmds.xform(branch[0], piv=bottom, ws=True)



            
#rotate it based on specified local-axis, and an angle given
print 'specify axis to rotate about : ex. 1 0 0  or  0 1 0  or 0 0 1 '
axis=[]
axis = raw_input()
axis = map(int, axis.split())
print axis
x=axis[0]
y=axis[1]
z=axis[2]
print 'specify axis to rotate about'
angle=0
angle=raw_input(angle)
angle=float(angle)*(math.pi /180.0)


#extract euler angle from axis-angle
heading = math.atan2(y * math.sin(angle)- x * z * (1 - math.cos(angle)) , 1 - (y*y + z*z ) * (1 - math.cos(angle)))
attitude = math.asin(x * y * (1 - math.cos(angle)) + z * math.sin(angle))
bank = math.atan2(x * math.sin(angle)-y * z * (1 - math.cos(angle)) , 1 - (x*x + z*z) * (1 - math.cos(angle))) 

#perform the actual rotation
cmds.rotate(bank*(180.0/math.pi), heading*(180.0/math.pi), attitude*(180.0/math.pi))

#save pos,rot
curPos=cmds.xform(branch[0], translation=True, query=True)
curRot=cmds.xform(branch[0], rotation=True, query=True)

#create a second cylinder
branch2=cmds.polyCylinder()
#get its height
cylHeight2=cmds.getAttr(branch2[1]+'.height')

#move to where the previous cylinder was
cmds.move(curPos[0],curPos[1],curPos[2])

#set rotation pivot to the bottom of the cylinder
bbox = cmds.exactWorldBoundingBox(branch2)
bottom = [(bbox[0]+bbox[3])/2, bbox[1], (bbox[2]+bbox[5])/2] #(xmin,xmax)/2 , (zmin,zmax)/2
cmds.xform(branch2[0], piv=bottom, ws=True)

#orient it based on how the previous cylinder was oriented
cmds.rotate(curRot[0],curRot[1],curRot[2])

#move forward on local y axis
cmds.move(curPos[0],curPos[1]+cylHeight2/2,curPos[2] ,os=True, r=True)

#perform another  rotation (if wanted)
cmds.rotate(curRot[0],curRot[1],curRot[2], r=True)


    
