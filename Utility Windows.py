import subprocess, os, sys

def Utility_Windows():
    prog=input("""Quale programma vuoi usare?
            1. Gestione Computer
            2. Gestione Certificati
            3. Gestione Dispositivi
            4. Gestione Disco
            5. Visualizzatore eventi
            6. Gestione Hyper-V
            7. Utenti e gruppi locali
            8. Performance Monitor
            9. Gestione di Stampa
           10. Servizi
           11. Utilità di Pianificazione
           12. Gestione Trusted Platform Module
           13. Windows Firewall con sicurezza avanzata
           14. Registro Windows
           15. System Information
           16. Prompt dei Comandi
           17. Check connessione
           18. systeminfo.exe
           19. Ip locale e configurazione di rete
           20. Exit
           

           (indicare il numero del programma che si vuole eseguire) """)

    prog=str(prog)
    
    if prog=="1":
        os.popen("Compmgmt.msc")

    elif prog=="2":
        os.popen("Certmgr.msc")

    elif prog=="3":
        os.popen("Devmgmt.msc")
        
    elif prog=="4":
        os.popen("Diskmgmt.msc")

    elif prog=="5":
        os.popen("Eventvwr.msc")

    elif prog=="6":
        os.popen("Virtmgmt.msc")

    elif prog=="7":
        os.popen("Lusrmgr.msc")

    elif prog=="8":
        os.popen("Perfmon.msc")

    elif prog=="9":
        os.popen("Printmanagement.msc")

    elif prog=="10":
        os.popen("Scervices.msc")

    elif prog=="11":
        os.popen("Taskschd.msc")

    elif prog=="12":
        os.popen("tpm.msc")

    elif prog=="13":
        os.popen("Wf.msc")

    elif prog=="14":
        os.popen("regedit")

    elif prog=="15":
        os.popen("msinfo32")

    elif prog=="16":
        subprocess.call("C:\\Windows\\System32\\cmd.exe")

    elif prog=="17":
        print(subprocess.getoutput("ping 8.8.8.8"))

    elif prog=="18":
        print(subprocess.getoutput("systeminfo"))

    elif prog=="19":
        print(subprocess.getoutput("ipconfig"))

    elif prog=="20":
        sys.exit()

    else:
        print("Opzione non valida")

    Utility_Windows()

Utility_Windows()
