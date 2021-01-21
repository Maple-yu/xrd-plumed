import numpy as np
import matplotlib.pyplot as plt
def getdata(atoms):
    
    x = np.arange(10,120.1,0.1).reshape(1101,1)

    liq = np.loadtxt('./%a/liq'%(atoms))[1:].reshape(1101,1)
    dia = np.loadtxt('./%a/dia'%(atoms))[1:].reshape(1101,1)
    gra = np.loadtxt('./%a/gra'%(atoms))[1:].reshape(1101,1)

    xrd = np.concatenate((x,liq,dia,gra),axis=1)

    np.savetxt('./%a/xrd.txt'%(atoms),xrd,header='2THETA liq dia gra')

def plotxrd(atoms,fignum):

    plt.subplot(4,1,fignum)
    xrd = np.loadtxt('./%a/xrd.txt'%(atoms))
    xrd = xrd[100:,:]

    plt.title('%a atoms'%(atoms))
    my_x_ticks = np.arange(10,120,5)
    plt.xticks(my_x_ticks)
    plt.xlabel('2Theta')
    plt.ylabel('intensity')
    plt.ylim(-0.05,0.16)
    xrd[:,0]=2*xrd[:,0]
    #l1,=plt.plot(xrd[:,0],xrd[:,1],color='red')
    l2,=plt.plot(xrd[:,0],xrd[:,2],color='blue')
    #l3,=plt.plot(xrd[:,0],xrd[:,3],color='green')
    #plt.legend(handles=[l1,l2,l3],labels=['liq','dia','gra'],loc='best')

plt.figure(figsize=(8,20),dpi=300)
plt.subplots_adjust(wspace =0, hspace =0.2)
j = 1
for i in [512,4096,13824,32768]:
    plotxrd(i,j)
    j = j + 1

plt.savefig('./xrd.png')
