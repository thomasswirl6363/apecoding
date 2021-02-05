from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random,time


while True:
    C=random.randrange(0,9)
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,x,y,z,38)
    time.sleep(0.2)

