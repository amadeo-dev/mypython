import random
def combat():
    print('Bienvenue sur ce jeu de combat laisser moi vous presenter les differente attaque')
    print('charge: inflige entre 5 et 10 de degat et vous inflige entre1 et 3 de dégat(+2 mana)')
    print('lance:inflige entre 1 et 5 de dégat(+7mana)')
    print('glace:inflige 3 dégat et a 1/2 chance de glacer l ennemi(-3 mana)')
    print('soins: rend 4 PV(+2 mana)')
    print('potion: as 1/2 chance de vous rendre 10 PV')
    print('aura de glace: glace l ennemie(-3 mana)')
    print('vole vie:enleve 3 PV a l ennemi et vous les donnent')
    print('magie noir:coute 100 mana peut enlever entre -10 et 30 PV')
    print('Le mana (obligatoire pour la dernière attaque) se gagne ou se perd en faisant certaine attaque')
    épée=0
    lance=0
    try:
        with open('E:\\save.txt'): pass
        file = open('E:\\save.txt',"r")
        l = file.readlines()
        shop=int(l[0])
        file.close()
        print('vous avez '+str(shop)+ ' coins')
    except IOError:
        file = open("E:\\save.txt", "x")
        file.close()
        print ('le dossier et cree')
        file = open("E:\\save.txt","w")
        en=10
        file = file.write(''+str(en)+'')
    a2=0
    LP=random.randint(90,100)
    PV=random.randint(90,100)
    i=0
    mana=random.randint(0,10)
    mana2=5
    print('choissisez votre mode de jeu 1=PVIA 2=PVP 3=shop(acheter de l equipement) 4= s equiper pour cette parti(ne faire que si vous avez achetez des chose au shop sinon le programe bugera)')
    mode=int(input('mode de jeu='))
    if mode==3:
        print('acheter une épée(+5 d attaque avec l attaque charge)-100 coins')
        print('acheter lance d argent(+5 d attaque avec lattaque lance)-70 coins')
        arme=int(input('1=choisir l épée(-100 coins) 2= choisir la lance(-70 coins'))
        if arme==1:
            try:
                with open('E:\\shoping.txt'): pass
            except IOError:
                file = open("E:\\shoping.txt", "x")
                file.close()
                print ('le dossier et cree') 

            if shop==100 or shop>100:
                shop=shop-100
                épée=1
                file = open("E:\\shoping.txt","w")
                file = file.write(''+str(épée)+'')
            elif shop<100:
                print('vous manquer de mana')
                return('dez')
        if arme==2:
            if shop==70 or shop>70:
                shop=shop-70
                lance=2
                file = open("E:\\shoping.txt","w")
                file = file.write(''+str(lance)+'')
            elif shop<70:
                print('vous manquer de mana')
                return('dez')
    elif mode==4:
        file = open("E:\\shoping.txt","r")
        selct = file.readline()
        selct = int(selct[0])
        if selct==1:
            épée=selct
        elif selct==2:
            lance=selct
    elif mode==2:
        print('attention le mode PVP presente des bug et le joueur 2 et nommé "l ennemi"')
    print('vous avez au debut tant de PV:')
    print(PV)
    print('et l ennemi a tant de PV')
    print(LP)
    while LP>0 and PV>0:
        print('Votre Mana-->'+str(mana)+'/100')
        print('mana ennemi:'+str(mana2)+'/100')
        print('choisisez une attaque 1=charge 2=lancé 3=glace 4=soin 5=potion 6=aura de glace 7=vole vie 8=magie noir(100 mana requis)')
        a=int(input('numeros de l attaque '))
        
        if a2==3:
            g=random.randint(1,2)
            if g==1:
                print('vous êtes glacé vous ne pouvez bouger')
            elif g==2:
                if a==1:
                    if épée==1:
                        doul=random.randint(5,15)
                    else:
                        doul=random.randint(5,10)
                    LP=LP-doul
                    charge=random.randint(1,3)
                    PV=PV-charge
                    mana=mana+3
                    print('la puissance de la charge vous a fait perdre tant de PV:')
                    print(charge)
                    print('il vous reste:')
                    print(PV)
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('mana ennemi:'+str(mana2)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('-'+str(charge)+'|                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                    
                elif a==2:
                    if lance==2:
                        doul=random.randint(1,10)
                    else:
                        doul=random.randint(1,5)
                    LP=LP-doul
                    mana=mana+7
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('mana ennemi:'+str(mana2)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                elif  a==3:
                    doul=3
                    LP=LP-doul
                    mana=mana-3
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('mana ennemi:'+str(mana2)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                elif a==4:
                    soin=5
                    PV=PV+soins
                    mana=mana+2
                    print('votre nombre de pv est de :')
                    print(PV)
                    print(''+str(mana)+'/100')
                    print('mana ennemi:'+str(mana2)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-')
                    print('+'+str(soins)+'|0                     0|')
                    print('  |_______________________|')
                elif a==5:
                    n=random.randint(0,2)
                    if  n==2:
                        print(' vous vous soigner de 10')
                        PV=PV+10
                        print('il lui vous reste tant de pv')
                        print(PV)
                    elif n==0 or n==1:
                        print('votre potion c est casser')
                        print('il lui vous reste tant de pv')
                        print(PV)
                
                elif a==6:
                    a==3
                    mana=mana-3
                elif a==7:
                    doul=3
                    soins=doul
                    LP=LP-doul
                    mana=mana-1
                    print('PV enlever a l ennemie')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print('PV volé a l ennemie:')
                    print(soins)
                    print('il vous reste')
                    print(PV)
                    print(''+str(mana)+'/100')
                    print('mana ennemi:'+str(mana2)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('+'+str(soins)+'|                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                
                elif a==8:
                    if mana==100 or mana>100:
                        mana=mana-100
                        mn=random.randint(-10,40)
                        LP=LP-mn
                        print('PV enlever a l ennemie')
                        print(mn)
                        print('il lui reste:')
                        print(LP)
                        print('mana ennemi:'+str(mana2)+'/100')
                        print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                        print(  '|                       |-'+str(mana)+'')
                        print('  |0---------------------*|')
                        print('  |_______________________|')
                    elif mana<100:
                        print('vous manquez de mana :-o')
        elif  a==1:
            if épée==1:
                doul=random.randint(5,15)
            else:
                doul=random.randint(5,10)
            LP=LP-doul
            charge=random.randint(1,3)
            PV=PV-charge
            mana=mana+3
            print('la puissance de la charge vous a fait perdre tant de PV:')
            print(charge)
            print('il vous reste:')
            print(PV)
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('mana ennemi:'+str(mana2)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(charge)+'|                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==2:
            if lance==2:
                doul=random.randint(1,10)
            else:
                doul=random.randint(1,5)
            LP=LP-doul
            mana=mana+7
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('mana ennemi:'+str(mana2)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif  a==3:
            doul=3
            LP=LP-doul
            mana=mana-3
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('mana ennemi:'+str(mana2)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==4:
            soins=5
            PV=PV+soins
            mana=mana+2
            print('votre nombre de pv est de :')
            print(PV)
            print(''+str(mana)+'/100')
            print('mana ennemi:'+str(mana2)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('+'+str(soins)+'|0                     0|')
            print('  |_______________________|')
        elif a==5:
            n=random.randint(0,2)
            if  n==2:
                print(' vous vous soigner de 10')
                PV=PV+10
                print('il lui vous reste tant de pv')
                print(PV)
            elif n==0 or n==1:
                print('votre potion c est casser')
                print('il lui vous reste tant de pv')
                print(PV)
        elif a==6:
            a=3
            mana=mana-3
        elif a==7:
            doul=3
            soins=doul
            LP=LP-doul
            PV=PV+soins
            mana=mana-1
            print('PV enlever a l ennemie')
            print(doul)
            print('il lui reste:')
            print(LP)
            print('PV volé a l ennemie:')
            print(soins)
            print('il vous reste')
            print(PV)
            print(''+str(mana)+'/100')
            print('mana ennemi:'+str(mana2)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('+'+str(soins)+'|                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==8:
            if mana==100 or mana>100:
                mana=mana-100
                mn=random.randint(-10,30)
                LP=LP-mn
                print('PV enlever a l ennemie')
                print(mn)
                print('il lui reste:')
                print(LP)
                print('mana ennemi:'+str(mana2)+'/100')
                print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                print(  ' |                       |-'+str(mn)+'')
                print('  |0---------------------*|')
                print('  |_______________________|')
            elif mana<100:
                print('vous manquez de mana :-o')
            
        print('au tour de l ennemi')
        if mode==2:
           a2=int(input('choisisez une attaque 1=charge 2=lancé 3=glace 4=soin 5=potion 6=aura de glace 7=vole vie 8=magie noir(100 mana requis)'))
        elif mode==1 or mode==3 or mode==4:
            a2=random.randint(1,7)
        if mode==1:
            if LP<15:
                soins=5
                LP=LP+soins
                print('l ennemi c est soigner il lui reste tant de PV:')
                print(LP)
                print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                print('  |                       |')
                print('  |0                     0|''+'+str(soins)+'')
                print('  |_______________________|')
        if mana2==100 or mana2>100:
            mana2=mana2-100
            mn2=random.randint(-10,30)
            PV=PV-mn2
            print('PV enlever par l ennemie')
            print(mn2)
            print('il vous reste:')
            print(PV)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print( '-'+str(mn2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a==3 :
            g=random.randint(1,2)
            if g==1 or g==1:
                print('l ennemie est glacé il ne peut bouger')
            elif g==2 :
                doul2=random.randint(1,5)
                PV=PV-doul2
                mana2=mana2+10
                print('vous avez perdu tant de PV:')
                print(doul2)
                print('il vous reste:')
                print(PV)
                print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                print('-'+str(doul2)+'|                       |')
                print('  |*---------------------0|')
                print('  |_______________________|')
        elif a2==1:
            doul2=random.randint(5,10)
            PV=PV-doul2
            charge=random.randint(1,3)
            LP=LP-charge
            print('la puissance de la charge lui a fait perdre tant de PV:')
            print(charge)
            print('il lui reste:')
            print(LP)
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            mana2=mana2+3
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |-'+str(charge)+'')
            print('  |*---------------------0|')
            print('  |_______________________|')
            
        elif a2==2:
            doul2=random.randint(1,5)
            PV=PV-doul2
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            mana2=mana2+10
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a2==3:
            doul2=3
            PV=PV-doul2
            mana2=mana2-3
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a2==4:
            soins=5
            LP=LP+soins
            mana2=mana2+2
            print('l ennemi c est soigner il lui reste tant de PV:')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('  |0                     0|''+'+str(soins)+'')
            print('  |_______________________|')
        elif a2==5:
            n=random.randint(0,2)
            if  n==2:
                print('il se soigner de 10')
                LP=LP+10
                print('il lui reste tant de pv')
                print(LP)
            elif n==0 or n==1:
                print(' ça potion c est casser')
        
        elif a2==6:
            a2=3
            mana2=mana2-3
        elif a2==7:
            doul2=3
            soins2=doul2
            PV=PV-doul2
            LP=LP+soins2
            mana2=mana2-1
            print('PV enlever par l ennemie')
            print(doul2)
            print('il vous reste:')
            print(PV)
            print('PV volé par l ennemie:')
            print(soins2)
            print('il lui reste')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |+'+str(soins2)+'')
            print('  |*---------------------0|')
            print('  |_______________________|')
        
        elif LP<15:
            soins=5
            LP=LP+soins
            print('l ennemi c est soigner il lui reste tant de PV:')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('  |0                     0|''+'+str(soins)+'')
            print('  |_______________________|')
        i=i+1
    if LP<=0:
        print('vous avez gagner bravo')
        win=30
        shop=shop+win
        print('vous avez gagner tant d argent '+str(win)+'')
    elif PV<=0:
        print('vous avez perdu dez')
    file = open('E:\\save.txt',"w")
    file = file.write(''+str(shop)+'')
    print('nombre de tours joué:')
    print(i)
    print('Merci d avoir joué :-).Jeu créé et édité par Martin Fischer')
    print('Version 4.0')
combat()