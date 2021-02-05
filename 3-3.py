from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(20):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x+10,y-1,z-7,x+12,y+9,z+7,57)
mc.setBlocks(x+5,y,z-6,x+8,y+8,z+6,0)
