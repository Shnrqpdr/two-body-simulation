import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

def plot_figure(r1_sol,r2_sol):
	#Criando a caixa do eixo                                                                                                
	fig=plt.figure(figsize=(15,15)) 
	#Criando eixo cartesiano
	ax=fig.add_subplot(111,projection="3d")
	#plotando                                                                                                               
	ax.plot(r1_sol[:,0],r1_sol[:,1],r1_sol[:,2],color="tab:blue")
	ax.plot(r2_sol[:,0],r2_sol[:,1],r2_sol[:,2],color="tab:red")
	#Posição final dos vetores
	ax.scatter(r1_sol[-1,0],r1_sol[-1,1],r1_sol[-1,2],color="tab:blue",marker="o",s=400,label="m1 = 1.0 Massa Terra")       
	ax.scatter(r2_sol[-1,0],r2_sol[-1,1],r2_sol[-1,2],color="tab:red",marker="o",s=100,label="m2 = 0.012 Massa Terra")      
	#Adicionando legendas
	ax.set_xlabel("x",fontsize=14)
	ax.set_ylabel("y",fontsize=14)                                                                                          
	ax.set_zlabel("z",fontsize=14)
	ax.set_title("Simulação para o problema de dois corpos: Terra-Lua\n",fontsize=14)
	ax.legend(loc="upper left",fontsize=14)
	                                                                                                                       
	plt.show() #plota o png


