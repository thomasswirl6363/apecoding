from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z+1,57)
mc.setBlock(x+1,y,z-1,57)
mc.setBlock(x-1,y,z+1,57)
mc.setBlock(x-1,y,z-1,57)
mc.setBlock(x+2,y,z,57)
mc.setBlock(x-2,y,z,57)
mc.setBlock(x,y,z+2,57)
mc.setBlock(x,y,z-2,57)