import numpy as np
import powerlaw
import matplotlib.pyplot as plt
import math

with open('words.txt', 'r') as f:
    xx = f.read().strip().split()
    s=[int(float(i)) for i in xx]

results = powerlaw.Fit(s)


print(s)
count_s=[[x, s.count(x)] for x in set(s)]
print(count_s)

x_label=[]
y_label=[]
for i in range(len(count_s)):
    x_label.append(count_s[i][0])
    y_label.append(count_s[i][1]/len(s))

x_label_log=[]
y_label_log=[]
for i in range(len(x_label)):
    x_label_log.append(math.log(x_label[i],10))
    y_label_log.append(math.log(y_label[i],10))


y_label_ccdf =[]
for i in range(len(y_label)):
    y_label_ccdf.append(sum(y_label[i:]))


y_label_ccdf_log=[]
for i in range(len(y_label_ccdf)):
    y_label_ccdf_log.append(math.log(y_label_ccdf[i],10))




plt.plot(x_label_log,y_label_ccdf_log,'ro')
plt.plot(np.unique(x_label_log), np.poly1d(np.polyfit(x_label_log, y_label_ccdf_log, 1))(np.unique(x_label_log)))
plt.xlabel('K (log)')
plt.ylabel('p(k) in (log) form')
plt.title('Log-Log Scale, Cumulative (CCDF) and <<BLIND FITTING>>')
plt.show()


plt.plot(x_label_log,y_label_log,'bo')
plt.plot(np.unique(x_label_log), np.poly1d(np.polyfit(x_label_log, y_label_log, 1))(np.unique(x_label_log)))
plt.xlabel('K (log)')
plt.ylabel('p(k) in (log) form')
plt.title('Log-Log Scale and <<BLIND FITTING>>')
plt.show()


powerlaw.plot_ccdf(s, color='g',linestyle='--')
plt.plot(x_label,y_label_ccdf,'ro')
plt.xlabel('K ')
plt.ylabel('p(k)')
plt.title('cumulative (CCDF) and Fitting')
plt.show()


powerlaw.plot_pdf(s, color='g',linestyle='--')
plt.plot(x_label,y_label,'ro')
plt.xlabel('K ')
plt.ylabel('p(k)')
plt.title('PDF and Fitting')
plt.show()


print("powerlaw function estimated Gamma:", results.power_law.alpha)
print("powerlaw function estimated Kmin:", results.power_law.xmin)
