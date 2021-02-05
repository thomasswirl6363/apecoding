from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

answer=random.randrange(0,16)
myID=mc.getPlayerEntityId("Thomasswirl6363")
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data>answer:
            mc.postToChat('HAHA,LOSER!')
        elif data<answer:
            mc.postToChat('HAHA,LOSER!')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,'Okay,you won!')
            break