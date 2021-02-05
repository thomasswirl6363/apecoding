from mcpi.minecraft import Minecraft
mc = Minecraft.create()

R=[]
K=[]
D=[]

for i in range(1,4):
    R.append(2*i)
for i in range(2,5):
    K.append(3*i)
for i in range(3,6):
    D.append(4*i)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,7,str(R),str(K),str(D))