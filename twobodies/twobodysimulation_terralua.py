import scipy
import scipy.integrate #resolve a EDO
import plot
import animation

def TwoBodyEquations(parametros,t,G,m1,m2): #Função para as equações de movimento
    
    #divide o vetor parametros para selecionar os vetores posição e velocidade
    r1=parametros[:3]
    r2=parametros[3:6]
    v1=parametros[6:9]
    v2=parametros[9:12]
    
    r=scipy.linalg.norm(r2-r1) #modulo do vetor r (distancia entre os objetos)
    
    derivada_v1=ND1*m2*(r2-r1)/r**3
    derivada_v2=ND1*m1*(r1-r2)/r**3
    derivada_r1=ND2*v1
    derivada_r2=ND2*v2
    
    r_derivadas=scipy.concatenate((derivada_r1,derivada_r2))
    derivadas=scipy.concatenate((r_derivadas,derivada_v1,derivada_v2))
    return derivadas


G=6.67408e-11 #Constante Gravitação Universal
m_nd=5.972e+24 #Massa da terra
r_nd=384e+6 #Distancia em metros entre os dois corpos
v_nd=5022 #Velocidade relativa do corpo 2 em relação ao corpo 1. Usando o valor de referencia da terra e lua
t_nd=27*24*3600 #Periodo orbital, usando valor do alpha centauri A

#Constantes de não-dimensionalização
ND1=G*t_nd*m_nd/(r_nd**2*v_nd) 
ND2=v_nd*t_nd/r_nd

#Massas
m1=1.0 #Massa da Terra
m2=0.012 #Massa da lua em relação a massa da terra

#Posições iniciais: As posições são escolhidas à mão para que o gráfico possa ser feito.
r1=[-0,0,0] #metros
r2=[1,0,0] #metros

#Convertendo para array float64 para utilizar array slicing depois
r1=scipy.array(r1,dtype="float64")
r2=scipy.array(r2,dtype="float64")

#Centro de massa
r_cm=(m1*r1+m2*r2)/(m1+m2)

#Velocidades Iniciais: São escolhas à mão para que o corpo não escape da atração gravitacional do outro
v1=[0.001,0.001,0] #metros por segundo 
v2=[-0.1,0,-0.2] #metros por segundo valor referencia [-0.05, -0.1]

#Convertendo denovo
v1=scipy.array(v1,dtype="float64")
v2=scipy.array(v2,dtype="float64")

#Velocidade do centro de massa
v_cm=(m1*v1+m2*v2)/(m1+m2)

#Parametros iniciais para a função de orbita
inicial_parametros=scipy.array([r1,r2,v1,v2]) #Array com posições e velocidades iniciais
inicial_parametros=inicial_parametros.flatten()
time=scipy.linspace(0,8,5000) #8 periodos orbitais no total, com 500 pontos para a orbita ficar mais certinha

two_body_sol=scipy.integrate.odeint(TwoBodyEquations,inicial_parametros,time,args=(G,m1,m2)) #aqui a gente resolve a E.D.O

r1_sol=two_body_sol[:,:3] #aqui a gente pega as soluções que calculamos na linha acima
r2_sol=two_body_sol[:,3:6] #mesma coisa

# Plot da figura

plot.plot_figure(r1_sol,r2_sol)

#Animação

animation.animate(r1_sol,r2_sol)


