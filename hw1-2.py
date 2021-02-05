import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    mc.postToChat('You are in x:'+str(x)+'y:'+str(y)+'z:'+str(z))
    time.sleep(0.3)

