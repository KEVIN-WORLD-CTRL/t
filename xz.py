import os, platform
 
try:
        import requests
        
        os.system("git pull")
        
except:
        os.system('pip2 install requests')
import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from xk import sf
        sf()
elif bit == "32bit":
        from xk import sf
        sf()
        
