#!/usr/bin/python3

import subprocess, os, sys, webbrowser

os.chdir("/home/Giuliano/Scrivania/Uni")

def open_file(file):
    subprocess.call(['xdg-open', file])


def Algoritmi():
    sel=input("""Seleziona cosa vuoi fare:\n1. Esercizi\n2. Studio\n""")

    if sel=="1":
        lang=input("Scegli il linguaggio:\n1. Python \n2. C\n""")
        
        if lang==1:
            file=input("Inserisci nome file")
            f=open(file+".py", "x")
            f.close()
            open_file(file + ".py")
        
        elif lang==2:
            file=input("Inserisci nome file")
            f=open(file+".c", "x")
            f.close()
            open_file(file + ".c")

    if sel=="2":
        os.chdir("Ingegneria degli algoritmi/Slides")
        files=sorted(os.listdir())

        for x in files:
            print(x)
        
        file=input("Scegli la slide da aprire (indica il numero) ")
        print()
        try:
            open_file(files[int(file)-1])
        except Exception as e:
            if e is IndexError:
                print("Indice troppo alto o negativo")
            elif e is ValueError:
                print("Porco Dio metti un numero")

def AnalisiII():
    sel=input()"""Seleziona cosa vuoi fare:\n1. Appunti\n2. Dispense Tauraso\n3.Giornale delle lezioni\n4. Videolezioni Tauraso\n""")
    os.chdir("Analisi II")

    if sel=="1":
        open("Appunti.tex")
    
    elif sel==2:
        os.chdir("Dispense")
        files=os.listdir()
        for x,y in zip(files, range(len(files))):
            print(str(y)+".",x)
        
        file=input("Scegli la slide da aprire (indica il numero) ")
        print()
        try:
            open_file(os.listdir()[int(file)-1])
        except Exception as e:
            if e is IndexError:
                print("Indice troppo alto o negativo")
            elif e is ValueError:
                print("Porco Dio metti un numero")
            AnalisiII()
    
    elif sel==3:
        print("Sei proprio sicuro di trovarci qualcosa di utile?")
        open_file("Giornale-delle-lezioni-2019-2020")

    elif sel==4:
        webbrowser.open("https://www.mat.uniroma2.it/~tauraso/analisi2video.html")

def Calcolatori():
    sel=input("""Seleziona cosa vuoi fare:\n1.  Programmazione C\n2.  Programmazione Assembly\n3.  Studio\n""")

    if sel=="1":
        os.chdir("Calcolatori Elettronici/Esercizi/A.A.1920/C")
        file=input("Inserisci nome file")
        f=open(file+".c", "x")
        f.close()
        open_file(file + ".c")

    elif sel=="2":
        os.chdir("Calcolatori Elettronici/Esercizi/A.A.1920/Assembly")
        file=input("Inserisci nome file")
        f=open(file+".s", "x")
        f.close()
        open_file(file + ".s")

    elif sel=="3":
        os.chdir("Calcolatori Elettronici/Slides")
        files=os.listdir()

        for x,y in zip(files, range(len(files))):
            print(str(y)+".",x)
        
        file=input("Scegli la slide da aprire (indica il numero) ")
        print()
        try:
            open_file(os.listdir()[int(file)-1])
        except Exception as e:
            if e is IndexError:
                print("Indice troppo alto o negativo")
            elif e is ValueError:
                print("Porco Dio metti un numero")
            Calcolatori()

def Geometria(cap, options=None):
    os.chdir("Geometria")

    assert type(cap) is str and cap.isdigit()
    
    if 1<=int(cap)<8:
        open_file(f"Capitolo {cap}.pdf")

    elif int(cap)==8:
        open_file("Esercizi Svolti.pdf")
    elif int(cap)==9:
        open_file("Appunti.tex")

def Usage():
    print("""
    Utility commands [args]:
    Commands:
    -g  --geometry [capitolo]
    -ce --calcolatori
    -ia --algoritmi""")

if __name__ == "__main__":
    if len(sys.argv)==1 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
       Usage()

    elif sys.argv[1]=="-g" or sys.argv[1]=="--geometry":
        try:
            Geometria(sys.argv[2])
        except IndexError:
            print("Capitolo non specificato")
            return None

    elif sys.argv[1]=="-ce" or sys.argv[1]=="--calcolari":
        Calcolatori()
        
    elif sys.argv[1]=="-ia" or sys.argv[1]=="--algoritmi":
        Algoritmi()

    elif sys.argv[1]=="-anII" or sys.argv[1]=="--anailisiII":
        Analisi2
