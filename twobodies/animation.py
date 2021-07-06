import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from progress.spinner import Spinner

def animate(r1_sol,r2_sol):
	state = 'unknow'
	spinner = Spinner('Loading ') ##Pra ver se esta rodando
 
	print("\n")
    
	spinner.next()
	# bora que bora
    
	#Criando a caixa do eixo
	fig=plt.figure(figsize=(15,15))
	#Criando eixo cartesiano
	ax=fig.add_subplot(111,projection="3d")
    
	#Criar novos arrays das soluções te da a flexibilidade de reduzir o numero de pontos da sua orbita
	#isto é, voce pode escolher ir pulando alguns pontos. De forma bem simplificada, serve pra diminuir o tempo de execução do codigo da animação.
	r1_sol_anim = r1_sol[:,:].copy()
	r2_sol_anim = r2_sol[:,:].copy()
    
	#Faz as bolinhas na posição inicial
	bolinha1=[ax.scatter(r1_sol_anim[0,0],r1_sol_anim[0,1],r1_sol_anim[0,2],color="tab:blue",marker="o",s=400,label="m1 = 1.0 Massa Terra")]
	bolinha2=[ax.scatter(r2_sol_anim[0,0],r2_sol_anim[0,1],r2_sol_anim[0,2],color="tab:red",marker="o",s=100,label="m2 = 0.012 Massa Terra")]

	#Cria a função pra animar
	def Animate(i,bolinha1,bolinha2):
    		#Remove as bolinhas, essa parte é responsavel por ir removendo as bolinhas anteriores e ir marcando as novas
    		bolinha1[0].remove()
    		bolinha2[0].remove()
            
    		#Orbitas
    		traco1=ax.plot(r1_sol_anim[:i,0],r1_sol_anim[:i,1],r1_sol_anim[:i,2],color="tab:blue")
    		traco2=ax.plot(r2_sol_anim[:i,0],r2_sol_anim[:i,1],r2_sol_anim[:i,2],color="tab:red")
         
    		#Bolinhas
    		bolinha1[0]=ax.scatter(r1_sol_anim[i-1,0],r1_sol_anim[i-1,1],r1_sol_anim[i-1,2],color="tab:blue",marker="o",s=400,label="m1=1.0 Massa Terra")
    		bolinha2[0]=ax.scatter(r2_sol_anim[i-1,0],r2_sol_anim[i-1,1],r2_sol_anim[i-1,2],color="tab:red",marker="o",s=100,label="m2=0.012 Massa Terra")

    		return traco1,traco2,bolinha1,bolinha2,
    
    
	ax.set_xlabel("x",fontsize=14)
	ax.set_ylabel("y",fontsize=14)
	ax.set_zlabel("z",fontsize=14)
	ax.set_title("Simulação para o problema de dois corpos: Terra-Lua\n",fontsize=14)
	ax.legend(loc="upper left",fontsize=14)
    
	twobody_animation = animation.FuncAnimation(fig,Animate, 2000, fargs=(bolinha1,bolinha2),interval=25,blit=False) #valor referencia é 800 interações

	#Salvando como mp4
	twobody_animation.save('two_body_simulation_terralua.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    
    
	print("\nFinished\n")
    
	state = 'FINISHED' #Encerrando o programa.
