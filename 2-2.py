from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
Block = random.randrange(0,150)
x,y,z = mc.player.getPos()

mc.setBlocks(x-10,y-10,z-10,x+20,y+30,z+50,Block)