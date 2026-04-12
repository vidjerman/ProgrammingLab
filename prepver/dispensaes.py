# 10.1
# a=538
# b=a//538
# c=a%60
# print (b,"h",c,"min")

# 10.2
# try:
#     a=int(input("numero intero"))
#     print (a**2)
#     print (a**3)
# except ValueError:
#     print("non e int")
#     a=0

# Esercizio 10.3. Scrivere un programma che verifica se un numero inserito
# dall’utente è pari o dispari.

# a=int(input("numero"))
# if (a%2==0): print ("pari")
# else: print ("disapri")

# Esercizio 10.4. Definire una funzione che prende come argomento una parola
# e una lettera e ritorna quante volte quella lettera è contenuta nella parola.

# def fun(par,let):
#     c=0
#     for i in par:
#         if (i==let): c+=1
#     return c
# print (fun("matematica","a"))

# Esercizio 10.5. Scrivere un programma che verifica se un numero inserito
# dall’utente è primo.

# a=int(input("numero"))
# flag=0
# for i in range (2,a-1):
#     if (a%i==0): flag=1
# if (flag==0): print ("primo")
# else: print ("no primo")

# Esercizio 10.6. Scrivere un programma che fa la somma di n numeri inseriti
# dall’utente. Di’ all’utente di scrivere 0 per fermarsi.  

# x=float(input("numero"))
# s=0.0
# while (x!=0.0):
#     s+=x
#     x=float(input("numero"))
# print ("%.2f" %s)

# Esercizio 10.7. Definire la funzione fattoriale (versione iterativa)

# def fatt (x):
#     f=1
#     for i in range (1,x+1):
#         f=f*i
#     return f
# print (fatt(5))

# Esercizio 10.8. Definire una funzione che, dati 3 numeri interi, stabilisce se
# possono essere i valori dei lati di un triangolo e, se sì, di che tipo di triangolo.

# def triangolo (a,b,c):
#     if (a+b>c and a+c>b and b+c>a):
#         if a == b == c:
#             print("Equilatero")
#         elif a == b or a == c or b == c:
#             print("Isoscele")
#         else:
#             print("Scaleno")
#     else: print ("non e triengolo")
# triangolo (5,5,5)

# Esercizio 10.9. Definire una funzione che conta quante vocali sono presenti
# in una stringa.

# def vocali (s):
#     c=0
#     s=s.lower()
#     for i in s:
#         if i in "aeiou":
#             c+=1
#     return c
# print (vocali ("mmagAare"))

'''LISTE'''
# Esercizio 11.1. Scrivere una funzione che sommi tutti gli elementi di una
# lista.
# def somma_lista (lista):
#     s=0
#     for i in lista:
#         s+=i
#     return (s)

# Esercizio 11.2. Scrivere una funzione che prende in input una stringa e
# ritorna True se è un palindromo, False altrimenti.

# def palindromo (s):
#     s2=s[::-1]
#     flag=True
#     for i,c in enumerate (s):
#         if c!=s2[i]:
#             flag=False
#     return flag
# print("palindromo" if palindromo("aanna") else "non")

# Esercizio 11.3. Definire una funzione che prende in input una lista A, indici
# i, j, e scambia il valore di A[i] con A[j].

# def scambio (lista,i,j):
#     temp=lista[:]
#     for k in range (len(lista)):
#         if (k==i):
#             temp[k]=lista[j]
#         elif (k==j):
#             temp[k]=lista[i]
#     lista=temp
#     return lista
# def scambioo(lista, i, j):
#     lista[i], lista[j] = lista[j], lista[i]
#     return lista

# l=[0,1,2,3,4,5,6]
# print(scambioo(l,1,0))

# Esercizio 11.4. Scrivere una funzione che prende in input due liste e ritorna
# True se le due liste hanno almeno un elemento in comune.

# def compare (l1,l2):
#     flag=False
#     if any (i==j for i in l1 for j in l2):
#         flag=True
#     # for i in l1:
#     #     for j in l2:
#     #         if (i==j):
#     #             flag=True
#     return flag
# l1=[1,2,3]
# l2=[4,5,6]
# print (compare(l1,l2))

# Esercizio 11.5. Definire una funzione che prende in input una lista di numeri
# interi in [0, 9] e ritorna una lista di stringhe, corrispondenti ai numeri scritti
# in Italiano, ad esempio:

# def parolee(l):
#     parole_num = ["zero","uno","due","tre","quattro",
#                   "cinque","sei","sette","otto","nove"]
#     return [parole_num[i] for i in l]
# l=[2,3,4,5]
# print (parolee (l))
        
# Esercizio 11.6. Scrivere una funzione che prende una lista di parole e resti-
# tuisce un dizionario con il conteggio delle occorrenze.

# def occorenze (l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# l=["uno","uno","due","tre","tre","tre"]
# print (occorenze (l))

'''FILE'''

# Esercizio 12.1. Definire una funzione che sommi tutti i valori delle vendite
# degli shampoo del file dato a lezione passato come argomento.

# def somma ():
#     s=0
#     data=open("shampoo_sales.csv","r")
#     data.readline()

#     for linea in data:
#         lista=linea.strip().split(",")
#         s+=float(lista[1])
#     print (s)
#     data.close()
# somma()

# Esercizio 12.2. Definire una funzione che prende in input un file e una parola
# e conta quante volte quella parola è presente nel file.

# def conta (file,parola):
#     c=0
#     for linea in file:
#         lista=linea.strip()
#         if (lista==parola):
#             c+=1
#     return c
# data=open("parole.txt","r")
# print (conta(data,"tre"))
# data.close()

# Esercizio 12.3. Definire una funzione conteggio che prende come input un
# file e ritorna un dizionario con chiavi le parole e valori il numero di volte che
# ciascuna parola è presente nel file.

# def conteggio (file):
#     d={}
#     for linea in file:
#         parola=linea.strip()
#         if (parola in d):
#             d[parola]+=1
#         else: d[parola]=1
#     return d
# data=open("parole.txt","r")
# print (conteggio (data))
# data.close()

# Esercizio 12.4. Definire una funzione che prende in input un file, rimuo-
# ve tutte le righe duplicate e scrive il risultato in un nuovo file chiamato
# unique.txt

# def controlla (file):
#     file2=open("unique.txt","w")
#     lista=[]
#     for linea in file:
#         frase=linea.strip()
#         flag=True
 
#         for i in lista:
#             if (i==frase):
#                 print (i)
#                 flag=False
#         if (flag): file2.write(frase)
#         lista+=[frase]
#     file2.close()


# data=open("C:\other\pythonreal\ProgrammingLab\prepver\parole.txt","r")
# controlla (data)
# data.close()

'''CLASSI'''

# Esercizio 13.1. Creare un oggetto CSVFile che rappresenti un file CSV, e
# che:
# 1. venga inizializzato sul nome del file CSV;
# 2. abbia un attributo name che ne contenga il nome;
# 3. abbia un metodo get_data() che torni i dati dal file CSV come lista di liste

# class CSVFile:
#     def __init__ (self,nome):
#         self.nome=nome
#     def get_data(self):
#         data=open(self.nome,"r")
#         l=[]
#         linea=data.readline()
#         while linea!="":
#             linea=linea.strip()
#             linea=linea.split(",")
#             lista=[linea]
#             l+=lista
#             linea=data.readline()
#         data.close()
#         return l

# file=CSVFile("data.csv")
# print(file.nome)
# print (file.get_data())

# Esercizio 13.2. Data la classe
# 1 class Veicolo:
# 2
# 3 def __init__(self, modello, velocita, km):
# 4 self.modello = modello
# 5 self.velocita = velocita
# 6 self.km = km
# Si crei una classe Autobus che contenga, oltre alle informazioni su un veicolo,
# la capienza massima e le informazioni sulla rotta seguita (tramite una lista).
# Si forniscano dei metodi di stampa - nella super-classe o nella sotto-classe? -
# che stampano informazione su un veicolo generico, e su un autobus

# class Veicolo:
#     def __init__(self, modello, velocita, km,anno):
#         self.modello = modello
#         self.velocita = velocita
#         self.km = km
#         self.anno=anno
#     def revisionata(self,anno):
#         return (self.anno>=anno)
#     def __str__(self):
#         return f"modello {self.modello} velocita {self.velocita} kilometri {self.km}"
# class Autobus (Veicolo):
#     def __init__(self,modello, velocita, km,anno, cap, rotta_lista):
#         super().__init__(modello, velocita, km,anno)
#         self.cap=cap
#         self.rotta_lista=rotta_lista
#     def __str__ (self):
#         auto=super().__str__()
#         return auto+f'cap= "{self.cap}" rotta= "{self.rotta_lista}"'
# veicolo=Veicolo("mecka","10a0","30akm")
# bus=Autobus("model","100","30km","2000kg",["ja","ti"])
# print(bus)

# Esercizio 13.3. Con riferimento all’esercizio precedente, si aggiunga la classe
# Auto (oltre ad Autobus) con un metodo di istanza revisionata per control-
# lare se la revisione sia stata fatta, o meno. Per verificare ciò revisionata
# 64
# prende in input l’ anno attuale (anno), e testa se il veicolo è coperto per
# l’anno in input. A tal proposito, si devono chiaramente aggiungere eventua-
# li informazioni riguardanti la revisione tramite variabili interne; si stabilisca
# vantaggi e svantaggi di metterli nella super-classe o nella sotto-classe, e si
# implementi l’approccio ritenuto migliore.
# class Auto (Veicolo):
#     def __init__(self,modello,velocita,km,anno):
#         super().__init__(modello,velocita,km,anno)
#     def revisionata(self,anno):
#         return (self.anno>=anno)
#         #     print("coperto")
#         # else: print ("scoperto")
# caras=Autobus("fiat",100,50,2027,1,2)
# print (caras)
# print(caras.revisionata(2015))

# Esercizio 13.4. Con riferimento all’esercizio precedente, vogliamo fare le re-
# visioni anche agli oggetti di classe Autobus. Si discuta se, con la soluzione
# svolta per l’esercizio precedente, l’aggiunta ora richiesta richiede tanto o poco
# aggiornamento di codice. Si risolva nuovamente questo ed il precedente eserci-
# zio per ridurre al minimo il codice necessario per avere le revisioni disponibili
# negli autobus.

# sercizio 13.5. Si crei una sotto-classe Autobus della super-class Veicolo.
# Il costo di default per una corsa completa su di un veicolo è 100 volte la
# capacità (in posti) del veicolo. Se il veicolo è un bus, c’è una maggiorazione
# del 10% sul costo di base (e.g., se la capacità del bus è di 50 posti, il costo
# dovrà essere 5500)

# class Veicolo:
#     def __init__(self, modello, km, posti):
#         self.modello = modello
#         self.km = km
#         self.posti = posti

#     def fare(self):
#         return self.posti * 100

# class Bus(Veicolo):
#     def fare(self):
#         base= super().fare()
#         return int(base *1.1)

# scuolabus = Bus("Volvo", 12, 50)
# print("Totale Bus:", scuolabus.fare())

# Esercizio 13.6 (Esponenti e potenza). Si scriva una classe potenza per
# definire le potenze di numeri con esponente sia positivo che negativo

# class potenza():
#     def __init__(self,base,esponente):
#         self.base=base
#         self.esponente=esponente
#     def calcola (self):
#         return self.base**self.esponente
# a=potenza(2,-3)
# print(a.calcola())

# Esercizio 13.8 (Compagnia di viaggi). La compagnia di viaggio “PT - Parti-
# re per non Tornare” ha ingaggiato il vostro team per realizzare un programma
# in grado di gestire i viaggi ed i clienti: i viaggi hanno molte caratteristiche in
# comune e qualche particolarità che le contraddistingue in base alla tipologia
# di viaggio (Mare, Montagna, Invernale o Estiva).
# Attributi comuni:
# • nome viaggio, identifica il titolo (a tema) di una vacanza;
# • data partenza, identifica la data di inizio della vacanza e può essere
# rappresentato come una lista di tre elementi (giorno, mese, anno);
# • data ritorno, identifica la data di conclusione della vacanza, anche essa
# può essere rappresentata come una lista di tre elementi;
# • località, identifica la destinazione per la vacanza;
# • resort, identifica l’albergo o il complesso turistico dove alloggeranno i
# clienti;
# • prezzo, identifica il prezzo, a persona, per poter partecipare alla vacanza;
# • partecipanti, identifica l’elenco dei clienti che si sono prenotati per il
# viaggio, e possono essere rappresentati attraverso una lista di cognomi;
# • responsabile viaggio, identifica un dipendente della compagnia di viaggi,
# referente del viaggio.
# Vacanza Invernale
# • skipass, identifica il prezzo di uno skipass giornaliero;
# • impianti sciistici, identifica l’elenco degli impianti sciistici convenzionati
# con l’agenzia di viaggio, rappresentabile come una lista;
# Vacanza Estiva
# • distanza, identifica la distanza, in metri, dal Resort alla spiaggia;
# • escursioni marine, identifica l’elenco delle attività marittime a cui i clien-
# ti possono partecipare gratuitamente (snorkeling, parapendio, lezioni di
# surf, etc.).
# 66
# La PT vorrebbe, inoltre, che da un viaggio fosse possibile determinare alcune
# utili informazioni.
# Metodi Viaggio:
# • stampa, funzione per stampare su schermo tutte le informazioni asso-
# ciate ad un determinato viaggio;
# • periodo, funzione per determinare quanti giorni o mesi di vacanza sono
# stati programmati, come differenza della data di partenza e quella di
# ritorno;
# • guadagno, funzione per determinare quale sia il ricavo netto dal viaggio,
# considerato che il 47% del prezzo di una prenotazione viene usato per
# coprire le spese del viaggio.
# Si adattino le precedenti funzioni per i casi distinti di vacanza invernale e
# vacanze estiva. In particolare:
# • il prezzo dello skipass pesa sulle spese del singolo ospite un ulteriore
# 15%;
# • il prezzo delle escursioni marine pesa sulle spese del singolo ospite un
# ulteriore 10%.
# Si realizzino le classi e sotto-classi necessarie per soddisfare le richieste della
# compagnia di viaggio. Inoltre, realizzare una funzione esterna che, dato il
# cognome di un preciso cliente ed una lista di tutti i viaggi organizzati dalla
# PT, determina i viaggi a cui il cliente ha partecipato e l’ammontare di denaro
# speso dal cliente per questi viaggi (la funzione non ritorna nulla).
    
# class Viaggio():
#     def __init__(self,nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio):
#         self.nome_viaggio=nome_viaggio
#         self.data_partenza=data_partenza #lista 3 el
#         self.data_ritorno=data_ritorno   #stesso
#         self.localita=localita
#         self.resort=resort
#         self.prezzo=prezzo
#         self.partecipanti=partecipanti   #lista di cognomi
#         self.responsabile_viaggio=responsabile_viaggio
#     def __str__(self):
#         return f"nome del viaggio: {self.nome_viaggio}, data partenza/ritorno: {self.data_partenza},{self.data_ritorno}, localita :{self.localita},resort: {self.resort}, prezzo: {self.prezzo} partecipanti: {self.partecipanti}, responsabile di viaggio: {self.responsabile_viaggio}"
#     def periodo(self):
#         giorni_mese = [31,28,31,30,31,30,31,31,30,31,30,31]
    
#         def totale_giorni(data):
#             g, m, a = data
#             return a*365 + sum(giorni_mese[:m-1]) + g
#         return totale_giorni(self.data_ritorno) - totale_giorni(self.data_partenza)
#     def guadagno(self):
#         c=0
#         for i in self.partecipanti: c+=1
#         return ((c*self.prezzo)*0.53)

# class Invernale(Viaggio):
#     def __init__(self,nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio,skipass,impianti_sci):
#         super().__init__(nome_viaggio,data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio)
#         self.skipass=skipass
#         self.impianti_sci=impianti_sci #lista
#     def guadagno(self):
#         base=super().guadagno()
#         return base*0.85
#     def __str__(self):
#         base=super().__str__()
#         return base+f", skipass: {self.skipass}, impianti sciistici: {self.impianti_sci}."
# class Estiva(Viaggio):
#     def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio,distanza,escursioni_marine):
#         super().__init__(nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio)
#         self.distanza=distanza
#         self.escursioni_marine=escursioni_marine
#     def guadagno(self):
#         base=super().guadagno()
#         return base*0.90
#     def __str__(self):
#         base=super().__str__()
#         return base+f", distanza: {self.distanza}, escursioni marine {self.escursioni_marine}."

# def spesatot_cliente(cognome,lista_viaggi):
#     lista_viaggi_partecipati=[]
#     denaro_speso=0
#     for i in lista_viaggi:
#         lista_partecipanti=i.partecipanti
#         for j in lista_partecipanti:
#             if (j==cognome):
#                 lista_viaggi_partecipati+=[i]
#                 denaro_speso+=i.prezzo

        
# datap=[12,5,2026]
# datar=[1,6,2027]

# sercizio 13.9 (Ornitorinchi). Vogliamo fare esperimenti sugli ornitorinchi,
# detti anche platipi. Durante la stagione riproduttiva, ogni platipo depone un
# certo numero di uova. Vogliamo costruire un modello per tenere traccia di
# quante uova ha deposto un platipo in ogni stagione.
# • implementare un classe che prende in input il nome del platipo e una
# lista contenente il numero di uova deposte in ogni stagione. Per esempio
# 1 Perry = Platipo('Perry', [3, 2, 4, 1, 2])
# • Espandere la classe Platipo con i seguenti tre metodi:
# – Uova_totali, che ritorna il numero totali di uova deposte;
# – Stagioni_feconde, che ritorna il numero di stagioni riproduttive
# in cui il platipo ha deposto almeno un uovo;
# – Deponi_uova che aggiunge le uova deposte alla lista di quelle già
# deposte.
# 67
# Sappiamo che i platipi possono deporre fino a 3 uova ogni stagione. Partendo
# dall’assunzione che ogni numero di uova ha la stessa probabilità di essere
# deposta (incluso zero), vogliamo modellare la dinamica riproduttiva di un
# gruppo di 3 platipi.
# Creare 3 oggetti platipi, scegliendo un nome e un numero di uova deposte in
# una stagione (i.e. una lista di un elemento).
# Simulare 10 stagioni riproduttive, per ogni stagione generare per ogni platipo
# un numero randomico tra 0 e 3 di uova deposte, ed aggiungerlo alla lista del
# platipo.
# Una volta che la simulazione è terminata stampare il nome, uova totali
# e stagione feconde per ogni platipo con la seguente sintassi: "Billy ha
# depositato un totale di 10 uova, in 5 stagioni riproduttive feconde"
# Nota bene. I numeri randomici possono essere generati con la funzio-
# ne randint(a,b) presente nella libreria random; a e b sono l’estremo
# inferiore e superiore.

# from random import*

# class Platipo():
#     def __init__(self,nome,lista_uova):
#         self.nome=nome
#         self.lista_uova=lista_uova
#     def Uova_totali(self):
#         s=sum(i for i in self.lista_uova)
#         return s
#     def Stagioni_feconde(self):
#         s=sum(1 for i in range(len(self.lista_uova)) if self.lista_uova[i]>0)
#         return s
#     def Deponi_uova(self,uova):
#         self.lista_uova+=[uova]
#     def __str__(self):
#         return f"{self.nome} ha depositato un totale di {self.Uova_totali()} uova, in {self.Stagioni_feconde()} stagioni riproduttive feconde"
    

# Perry1 = Platipo('Perry1', [3])#, 2, 4, 1, 2])
# Perry2 = Platipo('Perry2', [2])#, 1, 3, 0, 1])
# Perry3 = Platipo('Perry3', [1])#, 0, 2, 0, 0])
# for i in range (10):
#     a=randint(0,3)
#     Perry1.Deponi_uova(a)
#     Perry2.Deponi_uova(a)
#     Perry3.Deponi_uova(a)
# print(Perry1)
# print(Perry2)
# print(Perry3)

# Esercizio 13.10. Si crei la classe Poligono:
# • Il costruttore deve prendere solo il numero di lati
# • Deve fornire una descrizione del tipo: “Sono un poligono con X lati”
# Definire una sottoclasse Quadrilatero, modificare il costruttore in modo
# opportuno e sovrascrivere la descrizione per essere: “Sono un quadrilatero”.
# Definire una sottoclasse Rettangolo di Quadrilatero, la cui inizializzazione
# necessita di base ed altezza, modificare la descrizione per includere questa
# informazione e definire i metodi perimetro ed area.
# Definire la classe Triangolo, la cui inizializzazione necessita di 3 lati. Mo-
# dificare la descrizione per includere la lunghezza dei lati. Fornire un metodo
# perimetro e un metodo is_equilatero (restituisce True se il triangolo è
# equilatero).

# class Poligono():
#     def __init__(self,n):
#         self.n=n
#     def __str__(self):
#         return (f"sono un poligono con {self.n} lati")
# class Quadrilatero (Poligono):
#     def __init__(self,n):
#         super().__init__(n)
#     def __str__(self):
#         return ("sono un quadrilatero")
    
# class Rettangolo_di_Quadrilatero(Poligono):
#     def __init__(self,n,base,altezza):
#         super().__init__(n)
#         self.base=base
#         self.altezza=altezza
#     def __str__(self):
#         return (f"sono un quadrilatero con base {self.base} e altezza {self.altezza}")
#     def perimetro(self):
#         return 2*self.base+2*self.altezza
#     def are(self):
#         return self.base*self.altezza
# class Triangolo(Poligono):
#     def __init__(self,n,a,b,c):
#         super().__init__(n)
#         self.a=a
#         self.b=b
#         self.c=c
#     def __str__(self):
#         base=super().__str__()
#         return base+(f"sono un triangolo di lati a={self.a} b={self.b} e c={self.c}")
#     def perimetro(self):
#         return self.a+self.b+self.c
#     def is_equilatero(self):
#         if (self.a==self.b and self.a==self.c):
#             return True
#         else: return False
# triangolo=Poligono(3)
# # quadro=Quadrilatero(4)
# # tri=Triangolo(3,10,20,30)
# # print (quadro)
# # print (tri)
# # print(triangolo)
# calco=Rettangolo_di_Quadrilatero(3,10,20)
# print(calco.perimetro())
# #quadrato=Poligono(4)

'''LIST COMPREHENSION'''

# Esercizio 14.1. Si crei una lista di elementi nell’intervallo da 1000 a 2500 con
# step di 130, utilizzando la list comprehension. Si ragioni se la comprehension
# serva davvero in questo caso, o meno.

# l=[i for i in range(1000,2501,130)]
# print(l)

# Esercizio 14.2. Si costruisca una funzione che prende in input una lista
# ed una costante c, e restituisca la lista degli stessi elementi aumentati di c,
# mediante comprehension

# def aumento (l,c):
#     return [i*c for i in l]
# l=[1,2,3,4]
# print(aumento(l,2))

# Esercizio 14.3. Data una lista di numeri, usare una list comprehension per
# restituire i numeri dispari. 
# def disp(l):
#     return [i for i in l if i%2!=0]
# input = [0,1,2,3,4,5,6,7,8]
# print(disp(input))
# # output atteso: [1,3,5,7]

# Esercizio 14.4. Usare una list comprehension per effettuare il flattening di
# una lista di liste e trasformarla in una lista unica.


# input = [[1,2,3], [4,5], [6,7,8,1]]
# flat=[j for i in input for j in i]
# print (flat)
# # output atteso: [1,2,3,4,5,6,7,8,1]

# Esercizio 14.5. Date due liste, creare una lista con il prodotto x * y solo
# se il prodotto è maggiore di 10.

# lista_a = [1,3,5,7]
# lista_b = [2,4,6]
# l=[x*y for x in lista_a for y in lista_b if x*y>10]
# print (l)

# Esercizio 14.6. Usando una list comprehension, trovare tutte le triplette
# pitagoriche (a, b, c) con valori di a, b, c compresi tra 1 e 20.

# l=[(a,b,c) for a in range (1,21) for b in range (1,21) for c in range (1,21) if a*a+b*b==c*c]
# print(l)

# Esercizio 14.7. Date due liste, una di interi e una di lettere, creare le coppie
# (x, y) solo dove x è pari e l’indice di y è dispari.


# lista_a = [0,1,3,4]
# lista_b = ['a', 'b', 'c']

# pari=[(a,lista_b[b]) for a in lista_a for b in range(len(lista_b)) if a%2==0 and b%2!=0]
# print(pari)
# # output atteso: [(0, 'b'), (4, 'b')]

# Esercizio 14.8. Date due liste di parole, trovare tutte le coppie che sono
# anagrammi l’una dell’altra. Ad esempio:

# lista_a = ["listen", "hello", "race", "dusty"]
# lista_b = ["enlist", "world", "care", "study"]

# anagrammi=[(a,b) for a in lista_a for b in lista_b if sorted(a)==sorted(b)]
# print (anagrammi)

# # output atteso:
# # [("listen", "enlist"), ("race", "care"), ("dusty", "study")]

# Esercizio 14.9. Date due liste di stringhe, creare tutte le coppie dove le due
# parole non iniziano con la stessa lettera e la lunghezza combinata è maggiore
# di 8

# lista_a = ["listen", "lello", "race", "lusty","lsasasa"]
# lista_b = ["lnlist", "lorld", "care", "ltudy","lasasasas"]
# coppie=[]

# for a in lista_a:
#         for b in lista_b:
#             flag=False
#             flag2=False
#             if a[0]!=b[0]:
#                   flag=True
#             for i in range(len(a)):
#                 for j in range (len(b)):
#                       if i+1+j+1>8:
#                         print ("entr")
#                         flag2=True
#             if flag and flag2:
#                  coppie+=[(a,b)]
# print (coppie)

# Esercizio 14.10. Utilizzando la comprehension, si costruisca una lista dei
# quadrati degli elementi di un’altra lista solamente se il valore del quadrato
# supera 100.

# test=[2,3,4,5,10,15,20,30]
# quad=[a**2 for a in test if a**2>100]
# print (quad)

# x=[x for x in "This is my string"]
# nums = [i for i in range(1,1001)]
# string = "Stringa per l'esercizio pratico di list comprehension."
# div=[i for i in nums if i%8==0]
# cifra=[i for i in nums if "6" in str(i)]
# strin=sum(1 for i in string if i==" ")
# no_voc="".join (x for x in string if x.lower() not in "aeiou")
# piccole=[x for x in string.split(" ") if len(x)<5]
# numeri=[x for x in nums if [y for y in range(2,10) if x % y == 0]]              

# Esercizio 14.12. Data una frase, usare una dict comprehension per contare
# quante volte ogni parola appare. Ad esempio:

# sentence = "the cat sat on the mat the cat"
# d={key: sentence.split(" ").count(key) for key in sentence.split(" ")}
# print (d)
# output atteso:
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Esercizio 14.13. Data una lista di parole, creare un dizionario dove ogni
# lettera mappa alla lista di parole che la contengono, considerando solo le
# lettere presenti in almeno due parole. Ad esempio:

# parole = ["gatto", "tigre", "topo", "orso", "gru"]
# output atteso:
# {
# 't': ['gatto', 'tigre', 'topo'],
# 'o': ['gatto', 'topo', 'orso'],
# 'g': ['gatto', 'gru'],
# 'r': ['tigre', 'orso']
# }

# d={lettera:[p for p in parole if lettera in p]
#    for lettera in set("".join(parole))
#    if sum(1 for p in parole if lettera in p)>=2}
# parole = ["gatto", "tigre", "topo", "orso", "gru"]

# d = {
#     lettera: [p for p in parole if lettera in p]
#     for lettera in set("".join(parole))
#     if sum(1 for p in parole if lettera in p) >= 2
# }
# print (d)

# Esercizio 14.14. Date due liste di interi, creare un dizionario dove le chiavi
# sono i resti possibili della divisione per 3 (0, 1, 2) e i valori sono le liste di
# coppie (x, y) tali che x mod 3 = y mod 3. Ad esempio:

# lista_a = [3,7,11,6]
# lista_b = [9,4,2,12]

# d={r:[(x,y) for x in lista_a for y in lista_b if x%3==y%3==r] for r in range(3)}
# print (d)
# output atteso:
# {
# 0: [(3, 9), (3, 12), (6, 9), (6, 12)],
# 1: [(7, 4)],
# 2: [(11, 2)]
# }

'''ITERATORI'''

# Esercizio 15.1 (Flusso pari). Si scriva una classe per un iteratore che genera
# il flusso
# x, x + δ, x + 2δ, x + 3δ, . . . , y
# con x, δ ed y > x input della classe.

# class Iteratore ():
#     def __init__ (self,x,gamma, y):
#         self.x=x
#         self.c=1
#         self.gamma=gamma
#         if y<x: raise ValueError ("deve essere maggiore")
#         self.y=y
#         self.current=x
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.c>self.y: raise StopIteration
#         valore=self.current
#         valore+=self.c*self.gamma
#         self.c+=1
#         return valore

# itera=Iteratore(2,3,11)
# for i in itera:
#     print (i)

# Esercizio 15.2 (Flusso primi da lista). Si scriva una classe per un iteratore
# che restituisce solamente i numeri primi all’interno di una lista di interi (i.e.,
# la classe memorizza la lista, e l’iteratore ci naviga sopra di conseguenza).

# class iterabile ():
#     def __init__(self,lista):
#         self.lista=lista
#         self.c=0
#     def __iter__(self):
#         return self
#     def is_primo(self,n):
#         if n<2:
#             return True
#         for i in range(2,n-1):
#             if n%i==0:
#                 return False
#         return True
#     def __next__(self):
#         while self.c<len(self.lista):
#             valore=self.lista[self.c]
#             self.c+=1
#             if self.is_primo(valore): return valore
#         raise StopIteration

# l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# lista=iterabile(l)
# for i in lista:
#     print (i)

# Esercizio 15.4 (Flusso doppio). Si scriva una classe per un iteratore che
# genera gli elementi della successione
# ai = 2i/2i − 1

# class iteratore():
#     def __init__ (self):
#         self.i=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         a=(2**self.i)/((2*self.i)-1)
#         self.i+=1
#         return a
# itera=iteratore()
# for i in range (10):
#     print (next(itera))

# Esercizio 15.5 (Discretizzazione funzione). Si consideri una funzione f (x)
# discretizzata sull’intervallo [a, b] sui punti
# x1, x2, . . . , xn
# con xi = a + (i − 1)δx. Si costruisca un iteratore che generi i valori
# f (x1), f (x2), . . . , f (xn).

# def f(x):
#     return x**2
# class funz():
#     def __init__(self,a,b,f):
#         self.a=a
#         self.b=b
#         self.f=f
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.a>self.b: raise StopIteration
#         valore= f(self.a)
#         self.a+=1
#         return valore
# mio=funz(1,10,f)
# for i in mio:
#     print (i)

# Esercizio 15.6 (Calendario itinerante). Realizzare una classe Date che pre-
# senta come attributi una generica data (giorno, mese, anno).
# Inoltre, la classe presenta i seguenti metodi:
# • __init__, costruttore per creare un oggetto della classe;
# • __str__, funzione per stampare la data;
# • __iter__, funzione per creare un iteratore, utilizzato per “muoversi”
# tra i giorni secondo un incremento di un giorno;
# • __next__, funzione per realizzare la logica dell’iteratore. In particola-
# re, l’iteratore deve essere in grado di riconoscere se l’anno di riferimento
# ‘e un anno bisestile ed in caso modificare i giorni dei mesi opportuni.
# L’iteratore deve essere in grado di cambiare mese e/o anno dove ‘e ne-
# 71
# cessario (es. da 30/10/2020 si passa a 1/11/2020, oppure da 31/11/2020
# si passa a 1/1/2021).
# Utilizzare una funzione esterna che determina se l’anno di riferimento sia
# bisestile oppure no; si osservi che un anno viene considerato bisestile nei due
# casi seguenti:
# • l’anno è divisibile per 400;
# • l’anno è divisibile per 4, ma non per 100.
# Il corpo principale del programma dovrà testare il corretto funzionamento
# della classe Date su tutte le casistiche che potrebbero essere di interesse.

# def bisestile(anno):
#     if anno%400==0:
#         return True
#     if anno%4==0 and anno%100!=0:
#         return True
#     return False

# class date():
#     def __init__(self,g,m,a,bisestile):
#         self.g=g
#         self.m=m
#         self.a=a
#         self.bisestile=bisestile
#     def __str__(self):
#         return f"format g/m/a {self.g}/{self.m}/{self.a}"
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.g==31 and self.m in (1,3,5,7,8,10,12):
#             self.g=1
#             if self.m==12:
#                 self.m=1
#                 self.a+=1
#             else: self.m+=1
#         elif self.g==30 and self.m in (4,6,9,11):
#             self.g=1
#             self.m+=1
#         elif self.g>=28 and self.m==2:
#             if bisestile (self.a) and self.g==29 or bisestile(self.a) and self.g==28:
#                 if self.g==28:
#                     self.g+=1
#                 else:
#                     self.g=1
#                     self.m+=1
#             elif self.g==28:
#                 self.g=1
#                 self.m+=1
#         else: self.g+=1
#         return (self.g,self.m,self.a)
# data=date(1,1,2000,bisestile)
# for i in range (100):
#     print (next(data))
        
'''GESTIONE DEGLI ERRORI'''

# Esercizio 16.1. Modificare l’oggetto CSVFile dell’esercizio 13.1 in modo che
# stampi a schermo un messaggio di errore se si cerca di aprire un file non
# esistente.
# Il controllo può essere effettuato:
# 1. nella funzione get_data(), oppure
# 2. nel metodo __init__() (basta leggere la prima riga per verificare se il
# file esiste).

# class CSVFile:
#     def __init__ (self, nome):
#         if not isinstance(nome,str):
#             raise TypeError("non e una stringa")
#         self.nome=nome
#     def get_data(self,start=None,end=None):
#         try:
#             data=open(self.nome,"r")
#             l=[]
#             for i in range(start+1):
#                 linea=data.readline()
#             while start<=end:
#                 linea=linea.strip()
#                 linea=linea.split(",")
#                 lista=[linea]
#                 l+=lista
#                 linea=data.readline()
#                 start+=1
#             data.close()
#             return l
#         except IOError:
#             print("file non esistente")

# file=CSVFile("data.csv")
# print(file.nome)
# print (file.get_data(9,10))

# Esercizio 16.2. Modificare l’oggetto CSVFile della lezione precedente in mo-
# do che alzi un’eccezione se il nome del file non è una stringa (nel metodo
# __init__()).
# Successivamente, modificare la funzione get_data() di CSVFile in modo da
# leggere solo un intervallo di righe del file, aggiungendo gli argomenti opzionali
# start ed end, controllandone la correttezza e sanitizzandoli se necessario:

# Esercizio 16.3. Si osservi che, se l’esercizio precedente è stato svolto cor-
# rettamente, anche NumericalCSVFile eredita quasi automaticamente queste
# migliorie.
# In particolare, mentre il controllo sul nome del file viene effettivamente ere-
# ditato, per il range di righe è necessario inoltrare gli argomenti dal metodo
# della sottoclasse a quello della superclasse, ad esempio mediante:
# class NumericalCSVFile(CSVFile):
#     def get_data(self, *args, **kwargs):
#         csv_data = super().get_data(*args, **kwargs)

# file=NumericalCSVFile("data.csv")
# print(file.nome)
# print (file.get_data())

# Esercizio 16.4. Scrivere un programma che riceva una data di nascita come
# input e visualizzi l’età dell’utente e il numero di giorni, ore, minuti e secondi
# che mancano al prossimo compleanno.
# def bisestile(anno):
#     if anno%400==0:
#         return True
#     if anno%4==0 and anno%100!=0:
#         return True
#     return False
# class date():
#     def __init__(self,g,m,a,bisestile):
#         self.g=g
#         self.m=m
#         self.a=a
#         self.bisestile=bisestile
#     def __str__(self):
#         return f"format g/m/a {self.g}/{self.m}/{self.a}"
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.g==31 and self.m in (1,3,5,7,8,10,12):
#             self.g=1
#             if self.m==12:
#                 self.m=1
#                 self.a+=1
#             else: self.m+=1
#         elif self.g==30 and self.m in (4,6,9,11):
#             self.g=1
#             self.m+=1
#         elif self.g>=28 and self.m==2:
#             if bisestile (self.a) and self.g==29 or bisestile(self.a) and self.g==28:
#                 if self.g==28:
#                     self.g+=1
#                 else:
#                     self.g=1
#                     self.m+=1
#             elif self.g==28:
#                 self.g=1
#                 self.m+=1
#         else: self.g+=1
#         return (self.g,self.m,self.a)
# data=date(1,1,2000,bisestile)
# for i in range (100):
#     print (next(data))

# Esercizio 16.5. Scrivere un programma che chieda all’utente di inserire un
# numero intero. Se l’utente inserisce un valore valido, il programma deve
# stampare il quadrato del numero. Se l’utente inserisce un valore non valido, il
# programma deve visualizzare un messaggio di errore e richiedere nuovamente
# l’input.

# def valore():
#     try:
#         a=int(input("inserire numero intero"))
#         return a
#     except ValueError:
#         print("errore di tipi, reinserire")
#         valore()
# a=valore()


# Esercizio 16.6. Creare un programma che mostri un menù all’utente con tre
# opzioni:
# 1. calcolare la somma di due numeri;
# 2. calcolare la differenza tra due numeri;
# 3. uscire.
# Il programma deve:
# 1. chiedere all’utente di scegliere un’opzione (1, 2 oppure 3);
# 2. eseguire l’operazione corrispondente se l’input è valido;
# 3. gestire input non validi mostrando un messaggio di errore;
# 4. continuare a mostrare il menù fino a quando l’utente sceglie di uscire
# (opzione 3).
class SizeError(Exception):
    pass
def sommadue():
    try:
        a=float(input("inserire numero a"))
        b=float(input("inserire numero b"))
        return a+b
    except ValueError:
        print("reinserire")
        sommadue()
def differenza():
    try:
        a=float(input("inserire numero a"))
        b=float(input("inserire numero b"))
        return a-b
    except ValueError:
        print("reinserire")
        differenza()

def valore():
    try:
        a=int(input("inserire numero intero per scelta"))
        if a>3 or a<1: raise SizeError()
        return a
    except SizeError:
        print("numero tra 1 e 3 plis")
        valore()
    except ValueError:
        print("errore di tipi, reinserire")
        valore()
a=0
while a!=3:
    if a==1: print ("somma di due numeri ",sommadue())
    elif a==2: print("differenza di due numeri",differenza())
    print("1. calcolare la somma di due numeri.")
    print("2. calcolare la differenza tra due numeri.")
    print("3. uscire.")
    a=valore()
