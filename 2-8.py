from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a=input('HOW ARE YOU?')
mc.postToChat('hi,'+a)
x,y,z=mc.player.getPos()

mc.setBlocks(x,y,z,x+10,y+10,z+10,22)

mc.setBlocks(x+1,y+1,z+1,x+9,y+9,z+9,0)
mc.setBlocks(x+5,y+1,z,x+5,y+2,z,0)
mc.setBlocks(x,y+5,z,x+10,y+5,z+10,22)