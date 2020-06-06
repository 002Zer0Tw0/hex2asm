

import sys,os.path,os


seks = sys.argv[1]
ft = open(seks)
shellcode = ft.read()
badchar =  "x00"
badchar1 = "x0a"
badchar2 = "x09"
badchar3 = "xff"
badchar4 = "xcc"
badchar5 = "x08"





if  (badchar in shellcode):
    print("[!] Founded Badchar Check Your Code Please : " + badchar)

	
elif (badchar1 in shellcode):
	print("[!] Founded Badchar Check Your Code Please : " + badchar1)


elif (badchar3 in shellcode):
	print("[!] Founded Badchar Check Your Code Please : " + badchar3)


elif (badchar4 in shellcode):
	print("[!] Founded Badchar Check Your Code Please : " + badchar4)


elif (badchar5 in shellcode):
	print("[!] Founded Badchar Check Your Code Please : " + badchar5)

else:
	print("[+] No Badchars no Founded , Great Shellcode... ")

	

