import subprocess, os, sys

list_utilities = ["Compmgmt.msc", "Certmgr.msc", "Devmgmt.msc","Diskmgmt.msc", "Eventvwr.msc", "Virtmgmt.ms",
     "Lusrmgr.msc", "Perfmon.msc", "Printmanagement.msc", "Scervices.msc", "Taskschd.msc", "tpm.msc",
     "Wf.msc", "regedit", "msinfo32", "start", "ping 8.8.8.8", "systeminfo", "ipconfig"]

print("Benvenetuto in Utility Windows\n")
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

prog=int(prog)-1

try:
    if prog<16:
        os.popen(list_utilities[prog])
    else:
        subprocess.run(list_utilies[prog], output=sys.stdout)
        
except IndexError:
    print("Opzione non valida\n")
    subprocess.run('"Utility Windows.exe"', output=sys.stdout)
    
sys.exit()
