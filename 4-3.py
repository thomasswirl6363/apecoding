from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


y-=1




for i in range(50):
    x,y,z=mc.player.getPos()
    x+=i
    for j in range(50):
        color=random.randrange(0,16)
        z+=1
        mc.setBlock(x,y,z,35,color)
       
        
        