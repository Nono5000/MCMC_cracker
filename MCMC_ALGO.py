# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:19:37 2024

@author: Noe
"""

from random import randint, random
import bigram_utils
import pygame, sys
from pygame.locals import *
import time

pygame.init()
size = (740, 140)
screen = pygame.display.set_mode(size)

pygame.font.init() 

my_font = pygame.font.SysFont('Courier', 18)



global cText

cText = '''MPSF ZVGG KSFBP,
HUSBX NCI QCF NCIF YPHHPF SBM HUP VBHFVRIVBR DIOOYP HUSH NCI GPBH ZP. V USJP MVGAIGGPM VH KVHU ZN AYCGP QFVPBM SBM ACYYSTCFSHCF ZF AUSFYPG TSTTSRP, SBM KP SFP TCHU CQ HUP CDVBVCB HUSH VH VG S ZNGHPFN HUSH MPZSBMG S YVHHYP ZCFP ACBHPLH VQ KP SFP HC TP CQ SBN SGGVGHSBAP HC NCI. KP UCDP HUSH KP SFP STYP HC UPYD NCI, TIH KP SFP GCZPKUSH IBAPFHSVB KUPHUPF HUVG VG GCZPHUVBR HUSH MPZSBMG CIF VZZPMVSHP SHHPBHVCB. VQ GC UCK MC NCI DFCDCGP HUSH KP GUCIYM DFCAPPM? PJPB KVHU HUP VZDFCJPZPBHG VB HFSBGSHYSBHVA HFSQQVA VH KVYY HSXP GCZP HVZP HC VBJPGHVRSHP HUVG ZSHHPF TN DCGH SBM V SZ SQFSVM KP SFP GHVYY GCZP KSN QFCZ HUP VBHFCMIAHVCB CQ HUP HFSBGSHYSBHVA HPYPRFSDU. (HUCIRU CIF QFVPBM ZF KUPSHGHCBP VG KCFXVBR SYY UCIFG HC USGHPB HUSH MPJPYCDZPBH.) KP KCIYM TP RFSHPQIY VQ NCI ACIYM FPDYN KVHU SBN QIFHUPF VBQCFZSHVCB HUSH ZSN UPYD IG.
CB HUP ZSHHPF CQ HUP TIYYPH, ZF TSTTSRP USG GIRRPGHPM HUP DCGGVTVYVHN HUSH HUP YPHHPFVBR ZVRUH TP CQ QCFPVRB CFVRVB, TIH KP SFP BCH SKSFP CQ S YSBRISRP VB KUVAU HUVG ACZTVBSHVCB CQ YSHVB ACBGCBSBHG ACIYM GVRBVQN SB PLDFPGGVTYP KCFM. UP GIRRPGHPM SYGC HUSH HUP AUSFSAHPFG ZVRUH TP HUCGP CQ SB SAFCBNZ, HUCIRU HUP YSAX CQ DIBAHISHVCB SBM HUP FPYSHVJPYN YSFRP BIZTPF CQ YPHHPFG ZSXPG HUVG, HCC, IBYVXPYN.
KP SFP HUPB TFCIRUH HC HUP DCGGVTVYVHN, KUVAU V SZ GIFP NCI USM VB ZVBM, HUSH HUP HPLH CB HUP ASGP ZVRUH FPDFPGPBH GCZP QCFZ CQ PBANDUPFPM ACZZIBVASHVCB. HUP GUCFHBPGG CQ HUP HPLH DFPGPBHG S GVRBVQVASBH DFCTYPZ. KP SFP IBSTYP HC SDDYN CIF IGISY HPAUBVEIPG CQ QFPEIPBAN SBSYNGVG HC MPHPFZVBP SBN DSHHPFB, SBM KVHUCIH ZCFP ACBHPLH KP USJP BC AFVTG CF CHUPF AYIPG HC VHG YVXPYN ZPSBVBR. VB NCIF YPHHPF NCI ZPBHVCBPM HUSH HUP TIYYPH KSG QCIBM VB S GUVDDVBR KSFPUCIGP BPSF S GHSAX CQ GPSYPM AFSHPG, SBM HUSH HUPGP KPFP TCIBM QCF PBRYSBM. KP KCIYM QVBM VH ZCGH UPYDQIY VQ NCI ACIYM HPYY IG, GUCIYM NCI XBCK, HUP ACBHPBHG CQ HUCGP AFSHPG, HUP VBMVJVMISY CF ACFDCFSHVCB HC KUVAU HUPN TPYCBR SBM HUP FPAVDVPBH QCF KUCZ HUPN SFP CF KPFP VBHPBMPM.
V SZ GCFFN VH USG HSXPB GC YCBR QCF ZP HC FPDYN HC NCI, TIH ZF TSTTSRP VG UPSJVYN VBJCYJPM VB HUP DFPDSFSHVCBG QCF HUP VBHPFBSHVCBSY QSVF HC TP UPYM YSHPF VB HUP NPSF. RVJPB HUP DFVBAP ACBGCFH’G VBJCYJPZPBH NCI ASB VZSRVBP HUSH HUPFP SFP UVRU PLDPAHSHVCBG CB SYY CQ HUCGP KUC SFP VBJCYJPM VB VHG MPYVJPFN. TP SGGIFPM UCKPJPF HUSH KP KVYY RVJP CIF QIYY SHHPBHVCB HC NCIF FPDYN SBM KP UCDP HC TP STYP HC SGGVGH NCI.
KVHU CIF JPFN TPGH KVGUPG,
SMS YCJPYSAP SBM AUSFYPG TSTTSRP'''



#Function to decrypt ciphertext
def decrypt_text(key, ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return(''.join(key[alphabet.index(i)] for i in ciphertext if i.isalpha()))



#Function to swap 2 random pairs of letters in key; returns new swapped key
def mod_key(key):
    
    for i in range(0, 2):
        
        key = list(key)
        
        char1 = randint(0, 25)
        char2 = randint(0, 25)
        key[char1], key[char2] = key[char2], key[char1]
        
        key = ''.join(i for i in key)
    
    return key


def update_gui(key, key2, iteration, score, score2, ctext, ctext_best):
    pygame.event.get()
    screen.fill((255, 255, 255))
    text_surface = my_font.render(key, False, (0, 0, 0))
    text_surface_1 = my_font.render(key2, False, (0, 0, 0))
    text_surface_2 = my_font.render(str(iteration), False, (0, 0, 0))
    text_surface_3 = my_font.render(str(score), False, (0, 0, 0))
    text_surface_4 = my_font.render(str(score2), False, (0, 0, 0))
    text_surface_5 = my_font.render(str(ctext), False, (0, 0, 0))
    text_surface_6 = my_font.render(str(ctext_best), False, (0, 0, 0))
    label1 = my_font.render('Best Key :', False, (66, 135, 245))
    label2 = my_font.render('Crnt Key :', False, (66, 135, 245))
    label3 = my_font.render('Iteration :', False, (255, 0, 0))
    label4 = my_font.render('Best Score :', False, (66, 135, 245))
    label5 = my_font.render('Crnt Score :', False, (66, 135, 245))
    label6 = my_font.render('Best Decrypt :', False, (66, 135, 245))
    label7 = my_font.render('Crnt Decrypt :', False, (66, 135, 245))

    screen.blit(label1, (10,0))
    screen.blit(label2, (10,20))
    screen.blit(label4, (500,0))
    screen.blit(label5, (500,20))
    screen.blit(label6, (10,50))
    screen.blit(label7, (10,70))
    screen.blit(label3, (10,110))
    screen.blit(text_surface, (170,0))
    screen.blit(text_surface_1, (170,20))
    screen.blit(text_surface_2, (170,110))
    screen.blit(text_surface_3, (650,20))
    screen.blit(text_surface_4, (650,0))
    screen.blit(text_surface_6, (170, 50))
    screen.blit(text_surface_5, (170, 70))
    pygame.display.flip()
    
#key = 'abcdefghijklmnopqrstuvwxyz'


#print(key)

#main function

def main():
        
    global cText
    
    cText = bigram_utils.clean_text(cText)
    
    print(cText)
    
    
    previous_key = 'abcdefghijklmnopqrstuvwxyz'
    current_key = 'abcdefghijklmnopqrstuvwxyz'
    
    fitness_score = 1
    previous_fscore = fitness_score
    iteration = 0
    
    while fitness_score > 0.4:
        
        current_key = mod_key(previous_key)
        newkey = current_key
        
        pText1 = decrypt_text(previous_key, cText.lower())
        
        previous_fscore = bigram_utils.bigram_fitness(pText1)
        
        
        pText = decrypt_text(current_key, cText.lower())
        
        fitness_score = bigram_utils.bigram_fitness(pText)
        
        
        if fitness_score > previous_fscore:
            if random() < ((fitness_score-previous_fscore)/(fitness_score*250)):
                previous_key = current_key
            else:
                previous_key = previous_key
                
        
        else:
            previous_key = current_key
            
        iteration = iteration+1
    
        #print(iteration)
        print(current_key)
        #print(decrypt_text(current_key, cText.lower()))
        update_gui(previous_key, newkey, iteration, str(round(fitness_score, 4)), str(round(previous_fscore, 4)), pText[0:50], pText1[0:50])
        #print()
        
        
    print(pText)
    
        
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()