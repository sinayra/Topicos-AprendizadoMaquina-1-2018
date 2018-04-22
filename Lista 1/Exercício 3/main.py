import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.font_manager import FontProperties

a = 0
b = 1

media = 2
variancia = 1

priori_mais_1 = 0.4
priori_menos_1 = 0.6

def posteriori_c_mais_1(i):
    numerador = priori_mais_1 * (1/(1 * m.sqrt(2 * m.pi))) * m.pow(m.e, (-1/2) * m.pow((i - 1), 2))
    denumerador = priori_mais_1 * (1/(1 * m.sqrt(2 * m.pi))) * m.pow(m.e, (-1/2) * m.pow((i - 1), 2)) * priori_mais_1
    denumerador += priori_menos_1 * 1
    
    prob = numerador/denumerador
    
    return prob

def posteriori_c_menos_1(i):
    numerador = priori_menos_1 * 1
    denumerador = priori_mais_1 * (1/(1 * m.sqrt(2 * m.pi))) * m.pow(m.e, (-1/2) * m.pow((i - 1), 2)) * priori_mais_1
    denumerador += priori_menos_1 * 1
    
    prob = numerador/denumerador
    
    return prob



s = np.random.uniform(a,b)
hist, bins = np.histogram(s)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='red', label="Uniforme")
plt.fill_between(bins, np.ones_like(bins), facecolor='red', alpha=.3)



sigma = m.sqrt(variancia)
x = np.linspace(media - 3*sigma, media + 3*sigma)
plt.plot(x,mlab.normpdf(x, media, sigma), label="Gaussiana",  color='blue')
plt.fill(x,mlab.normpdf(x, media, sigma), alpha=.3, facecolor='blue')
#plt.savefig("distribuicao.png", bbox_inches='tight')  

fontP = FontProperties()
fontP.set_size('small')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop=fontP)
plt.show()

C_mais_1 = []
C_menos_1 = []
C_mais_ou_menos = np.array([])
for i in x:
    if i < 0:
        C_mais_1.append(i)
    elif i > 1:
        C_mais_1.append(i)
    else:
        prob_c_mais_1 = posteriori_c_mais_1(i)
        prob_c_menos_1 = posteriori_c_menos_1(i)
                        
        if prob_c_mais_1 > prob_c_menos_1:
            C_mais_1.append(i)
        elif prob_c_mais_1 < prob_c_menos_1:
            C_menos_1.append(i)


plt.scatter(C_mais_1, C_mais_1, label="C+1", color='red')
plt.scatter(C_menos_1, C_menos_1, label="C-1", color='blue')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop=fontP)
plt.show()
#plt.savefig("bayer.png", bbox_inches='tight')  

