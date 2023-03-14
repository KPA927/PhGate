import matplotlib.pyplot as plt

def plotP(t, res, save = False):
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
    if save:
        print("Введите название сохраняемого файла населенностей: ")
        s = str(input())
        if s!= '-':
            plt.savefig(s+ ".pdf")
    
def plot_Full(t, res, save = False, scale = 1):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.subplots_adjust(top=0.9)
    N = int(scale*np.size(t))

    axes[0, 0].plot(t[:N], res[:N, 0], label = r'$\downarrow \downarrow$', color = 'r')
    axes[0, 0].set(xlabel = "Gate time (mus)" , ylabel = "Level population")
    axes[0, 0].grid()
    axes[0, 0].legend()

    axes[1, 0].plot(t[:N], res[:N, 1], label = r'$\uparrow \downarrow$', color = 'b')
    axes[1, 0].set(xlabel = "Gate time (mus)" , ylabel = "Level population")
    axes[1, 0].grid()
    axes[1, 0].legend()

    axes[0, 1].plot(t[:N], res[:N, 2], label = r'$\downarrow \uparrow$', color = 'g')
    axes[0, 1].set(xlabel = "Gate time (mus)" , ylabel = "Level population")
    axes[0, 1].grid()
    axes[0, 1].legend()

    axes[1, 1].plot(t[:N], res[:N, 3], label = r'$\uparrow \uparrow$', color = 'y')
    axes[1, 1].set(xlabel = "Gate time (mus)" , ylabel = "Level population")
    axes[1, 1].grid()
    axes[1, 1].legend()


    fig.suptitle('Зависимость заселенностей Фазового Гейта от времени',
                 fontsize = 30)

    plt.show()
    if save:
        print("Введите название сохраняемого файла: ")
        s = str(input())
        if s!= '-':
            fig.savefig(s+ ".pdf")


def Fid_plot(t, res, save = False):
    plt.figure(figsize= (10, 5))

    plt.plot(t, 1-res[:, 4])
    plt.grid()
    plt.xlabel("Gate time (mus)")
    plt.ylabel("Fidelity")
    if save:
        print("Введите название сохраняемого файла фиделити: ")
        s = str(input())
        if s!= '-':
            plt.savefig(s+ ".pdf")