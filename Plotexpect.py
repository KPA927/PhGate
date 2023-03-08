import matplotlib.pyplot as plt
import os
import numpy as np

def plotP(t, res, N):
    plt.figure(figsize= (10, 5))
    plt.plot(t, res[:, 0],  label = r'$\downarrow \downarrow$')
    plt.plot(t, res[:, 1],  label = r'$\downarrow \uparrow$',)
    plt.plot(t, res[:, 2],  label = r'$\uparrow \downarrow$',)
    plt.plot(t, res[:, 3],  label = r'$\uparrow \uparrow$',)
    plt.grid()
    plt.legend()
    #plt.plot(1e3*times, np.transpose(result.expect)[5], label = '1')
    plt.xlabel("Gate time (mus)")
    plt.ylabel("Level population")
    s = str(N)
    plt.savefig("Results/"+ s+ "/P"+s+ ".pdf")
            
def Fid_plot(t, res, N):
    plt.figure(figsize= (10, 5))

    plt.plot(t, 1-res[:, 4])
    plt.grid()
    plt.xlabel("Gate time (mus)")
    plt.ylabel("Fidelity")
    s = str(N)
    plt.savefig("Results/"+ s+ "/F"+s+ ".pdf")
            
def save_all(t, res, N):
    arr = np.concatenate((t.reshape((res.shape[0], 1)), res), axis = 1)
    s = str(N)
    if os.path.exists("Results/"+ s)==0: 
        os.mkdir("Results/"+s)
    np.savetxt("Results/"+ s+ "/"+s +".txt", arr)
    plotP(t, res, N)
    Fid_plot(t, res, N)

