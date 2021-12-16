def verifica_primo(n): 
 c=0 
 x=2 
 if n>=2: 
  while x<=n/2: 
   if n%x==0: 
    c=c+1 
    x=x+1 
   else: 
    x=x+1 
  if c==0: 
   return True 
  else: 
   return False 
 else: 
  return False 
 
 
def genera_primos(n): 
 lp=[] 
 x=2 
 while n!=0: 
  if verifica_primo(x)==True: 
   lp.append(x) 
   x=x+1 
   n=n-1 
  else: 
   x=x+1 
 return lp 
 
     
def pyq(): 
  
 p=int(input("\tValor de (p)=")) 
 while verifica_primo(p)==False: 
  print("\t(p) tiene que ser un numero primo !!!") 
  p=int(input("\tValor de (p)=")) 
 q=int(input("\tValor de (q)=")) 
 while verifica_primo(q)==False or q==p: 
  print("\t(q) tiene que ser un numero primo diferente de (p) !!!") 
  q=int(input("\tValor de (q)=")) 
 lpq=[p,q] 
 return lpq 
  
def calculae(o): 
 e=2 
 le=[] 
 while e>1 and e<o : 
  if mcd(e,o)==1: 
   le.append(e) 
   e=e+1 
  else: 
   e=e+1 
 print("\nVALORES PARA (e)="+str(le)) 
 e=int(input("\n\tValor de (e)=")) 
 while mcd(e,o)!=1: 
  print("\n\tEliga un valor de la lista !!!") 
  e=int(input("\n\tValor de (e)=")) 
 return e 
 
def mcd(e,o): 
 m=o%e 
 while m!=0: 
  o=e 
  e=m 
  m=o%e 
 return e 
 
def congruente(e,o): 
 k=1 
 m=(1+(k)*(o))%(e) 
 while m!=0: 
  k=k+1 
  m=(1+(k)*(o))%(e) 
 d=int((1+(k)*(o))/(e)) 
 return d 
 
def cifrarmensaje(msj,key): 
 msj=msj.upper() 
 lm=msj.split(" ") 
 cmc="" 
 lmc=[] 
 for i in lm: 
  pal=cifrarpalabra(i,key) 
  lmc.append(pal) 
 for j in lmc: 
  cmc=cmc+str(j)+" " 
 return cmc 
 
def cifrarpalabra(m,k): 
 lpc=[] 
 lp=[] 
 n,e=k 
 cpc="" 
 for i in m: 
  x=buscarpos(i) 
  lp.append(x) 
 for j in lp: 
  c=(j**e)%n 
  lpc.append(c) 
 for k in lpc: 
  cpc=cpc+str(k)+" " 
 return cpc  
  
 
def buscarpos(x): 
 alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0987654321!@#$%^&*()_+=-][}{;?><.,/" 
 c=0 
 for i in alf: 
  if x==i: 
   return c 
  else: 
   c=c+1  
 
def descifrarmensaje(msj,key): 
 msj=msj.upper() 
 lm=msj.split("  ") 
 cmc="" 
 lmc=[] 
 for i in lm: 
  pal=descifrarnumero(i,key) 
  lmc.append(pal) 
 for j in lmc: 
  cmc=cmc+str(j)+" " 
 return cmc 
 
def descifrarnumero(m,k): 
 lnc=[] 
 ln=[] 
 n,d=k 
 cnc="" 
 men=m.split(" ") 
 for i in men: 
  x=int(i) 
  ln.append(x) 
 for j in ln: 
  m=(j**d)%n 
  lnc.append(m) 
 for k in lnc: 
  l=buscarlet(k) 
  cnc=cnc+str(l) 
 return cnc 
 
def buscarlet(x): 
 alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0987654321!@#$%^&*()_+=-][}{;?><.,/" 
 c=0 
 for i in alf: 
  if x==c: 
   return i 
  else: 
   c=c+1
l= []
l = "[23861, 23353]"
rep =l.replace('[', '').replace(']', '').split(",")
d =  [int(i) for i in rep]
print( d)
print(cifrarmensaje("HOLA MUNDO", d))
# print(descifrarmensaje("fsdf", [23861, 23353]))