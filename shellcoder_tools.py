# Shellcoder Tools
# Twitter : @smashedkernel , @blacknbunny

import os.path,time
import sys,os

os.system("cls")
konum = os.getcwd()
tool1 = "tools/shellcode_badchars.py"
tool2 = "tools/shellcode_crypter.py"
tool3 = "tools/shellcode2asm.py"
tool4 = "tols/shellcode_tester.py"
ft = open("tools/about.txt")
hakkinda = ft.read()
fak = open("tools/gui.txt")
gui = fak.read()

amnk = open("tools/asmhlp.txt")
asmhlp = amnk.read()


if os.path.isfile(tool1):
    
    print('[!] Dosya Bulundu : {0}'.format(tool1))
else:
     print('[-] Dosyalar Eksik Tekrar indirmeyi Deneyin !')
     
if os.path.isfile(tool2):
    
     print('[!] Dosya Bulundu : {0}'.format(tool2))
else:
     print('[-] Dosyalar Eksik Tekrar indirmeyi Deneyin !')
     
if os.path.isfile(tool3):
     
     print('[!] Dosya Bulundu : {0}'.format(tool3))
else:
     print('[-] Dosyalar Eksik Tekrar indirmeyi Deneyin !')
     
if os.path.isfile(tool4):
     
     print('[!] Dosya Bulundu : {0}'.format(tool4))

        
time.sleep(1)
os.system("cls")
        
print(gui)

secim = input("Tool >> ")

if (secim == "1"):
      os.system("cls")
      print(asmhlp)
      retbit = input("Return Bit >> ")
      arch = input("Architecture >> ")
      asmflavor = input("Assembly Flavor >> ")
      shcd = input("Shellcode txt File >> ")
      wtf = open(shcd)
      sikkod = wtf.read()
      os.system("python tools/shellcode2asm.py " + retbit + " " + arch + " " + asmflavor + " " + sikkod)
elif (secim == "2"):
   os.system("cls")
   
   option = input("Enter Option (encrypt/decrypt) : ")
   key = input("Enter Secret Key (Default : hexrain) : ")
   shellcode = input("Enter Shellcode : ")
   os.system("python tools/shellcode_crypter.py --shellcode " + shellcode + " --key " + key + " --option " + option)


elif (secim == "3"):
   os.system("cls")
   selkod = input("Shellcode txt File : ")
   tamami = konum + "\\" + selkod
   os.system("python tools/shellcode_badchars.py " + tamami)

elif (secim == "4"):
   os.system("cls")
   skodd = input("Shellcode txt File : ")
   tumu = konum + "\\" + skodd
   os.system("python tools/shellcode_tester.py " + tumu)

elif (secim == "6"):
   os.system("cls")
   print(hakkinda)

elif (secim == "5"):
   os.system("cls")
   os.system("pip install -r tools/requirements.txt")
   
else:
   print("[!] Lutfen Bir Secenek girin..")