from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getPos()

mc.setBlocks(x-50,y-50,z-50,x+50,y+50,z+50,95)

mc.setBlocks(x-49,y-49,z-49,x+49,y+49,z+49,95)
mc.setBlocks(x-50,y-25,z-50,x+50,y+25,z+50)