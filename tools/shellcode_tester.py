# Shellcoder Tools
# Twitter : @r0llafag , @blacknbunny

import urllib2
import ctypes

dosyadi = sys.argv[1]
dosya = open(dosyadi)
textfile = dosya.read()

shellcode = textfile



shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))


shellcode_func  = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))


shellcode_func()
