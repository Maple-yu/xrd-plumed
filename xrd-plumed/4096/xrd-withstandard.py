import numpy as np
import matplotlib.pyplot as plt
def withstandard(atom):
    xrd = np.loadtxt('')
    
    plt.figure(figsize=(12.8,10.8),dpi=300)
    grid = plt.GridSpec(6, 1, wspace=0.3, hspace=0.3)
    def x_tick():
        my_x_ticks = np.arange(10,120,5)
        plt.xticks(my_x_ticks)

    '''
    plt.title('4096 atoms')
    plt.xlabel('2Theta')
    plt.ylabel('intensity')
    '''

    #plt.subplot(3,1,1)
    plt.subplot(grid[0,0])
    l1,=plt.plot(xrd[:,0],xrd[:,1],color='red',label='liq')
    x_tick()
    plt.legend()

    #plt.subplot(3,1,2)
    plt.subplot(grid[1,0])
    diamond=np.array(((43.8429,100),(75.129,25.954),(91.267,8.0572)))
    diamond[:,1] = 0.001*diamond[:,1]
    plt.bar(diamond[:,0],diamond[:,1],width=0.2, align = 'center') 
    l2,=plt.plot(xrd[:,0],xrd[:,2],color='blue',label='dia')
    x_tick()
    plt.legend()

    #plt.subplot(3,1,3)
    plt.subplot(grid[3:7,0])
    graphite=np.array(((20.4349,100),(41.5586,9.2796),(43.578,1.1166),(64.3022,1.6761),(80.9338,0.7878),(93.1562,0.1103),(122.288,0.1141)))
    graphite[:,1] = 0.02*graphite[:,1]
    plt.bar(graphite[:,0],graphite[:,1],width=0.2, align = 'center') 
    l3,=plt.plot(xrd[:,0],xrd[:,3],color='green',label='gra')
    x_tick()
    plt.legend()

    #plt.subplot(3,1,3)
    plt.subplot(grid[2,0])
    graphite=np.array(((41.5586,9.2796),(43.578,1.1166),(64.3022,1.6761),(80.9338,0.7878),(93.1562,0.1103),(122.288,0.1141)))
    graphite[:,1] = 0.02*graphite[:,1]
    plt.bar(graphite[:,0],graphite[:,1],width=0.2, align = 'center') 
    xrd = xrd[200:,:]
    l3,=plt.plot(xrd[:,0],xrd[:,3],color='green',label='gra')
    x_tick()
    plt.legend()

plt.savefig('4096.png')
