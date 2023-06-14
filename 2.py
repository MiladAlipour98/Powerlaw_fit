import matplotlib.pyplot as plt
import math
import powerlaw

def powerlaw_seq_creation(path): #Creating powerlaw degree sequence from dataset

    file = open(path, "r")
    lines = file.read().strip().split()
    ds = [int(float(i)) for i in lines] #Making list of degree sequence
    n = len(ds)
    ds_dict = dict((i, ds.count(i)) for i in set(ds)) #making dictionary of nodes and number of each node

    x = list(ds_dict.keys()) #Unique nodes
    k = list(ds_dict.values()) #number of unique nodes
    k = [element / n for element in k] #proportion of each degree
    s = sum(k)
    print(s)

    x_log=[math.log10(i) for i in x]
    k_log=[math.log10(i) for i in k]

    k_cdf =[]
    for i in range(len(k)): #calculating ccdf of each degree
       k_cdf.append(sum(k[i:]))


    k_cdf_log=[math.log10(i) for i in k_cdf] #calculating log form of each degree cdf

    return ds, x, k, x_log, k_log,k_cdf,k_cdf_log




def main():

    ds, x, k, x_log, k_log,k_cdf,k_cdf_log = powerlaw_seq_creation("terrorism.txt")
    print(len(ds))
    print(len(k))
    print(k_cdf)
    se = sum(k_cdf)
    print(se)


    plt.figure(figsize=(5, 20))
    plt.plot(x_log, k_cdf_log, 'ro', linewidth=1, markersize=6)
    plt.xlabel("$log(K)$")
    plt.ylabel("$log(p(k)$")
    plt.title("log-log CDF")
    plt.show()


    plt.figure(figsize=(5,20))
    plt.plot(x_log,k_log,'ro', linewidth=1, markersize=6)
    plt.xlabel("$log(K)$")
    plt.ylabel("$log(p(k)$")
    plt.title("log-log PDF")
    plt.show()

    plt.figure(figsize=(5, 20))
    plt.plot(x,k,'ro',linewidth=1, markersize=6)
    powerlaw.plot_pdf(ds)
    plt.xlabel("$K$")
    plt.ylabel("$p(k)$")
    plt.title("Fitted PDF")
    plt.show()

    plt.figure(figsize=(5, 20))
    plt.plot(x,k_cdf,'ro',linewidth=1, markersize=6)
    powerlaw.plot_ccdf(ds)
    plt.xlabel("$K$")
    plt.ylabel("$p(k)$")
    plt.title("Fitted CDF")
    plt.show()

if __name__ == '__main__':
    main()

