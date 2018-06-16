import zipfile
import os.path
from optparse import OptionParser
parser = OptionParser("""

  ___________ _____     _____                _    _             
 |___  /_   _|  __ \   / ____|              | |  (_)            
    / /  | | | |__) | | |     _ __ __ _  ___| | ___ _ __   __ _ 
   / /   | | |  ___/  | |    | '__/ _` |/ __| |/ / | '_ \ / _` |
  / /__ _| |_| |      | |____| | | (_| | (__|   <| | | | | (_| |
 /_____|_____|_|       \_____|_|  \__,_|\___|_|\_\_|_| |_|\__, |
                                                           __/ |
                                                          |___/
coded by Hazem Hesham
FB = https://www.facebook.com/Human.script.01

{-h or --help } for more info                                                          


    """)
parser.add_option('-f','--zipfile',dest='zf',type='string',help='location zipfile')
parser.add_option('-p','--passwordlist',dest='pl',type='string',help='location password list')
(options,args) = parser.parse_args()
if options.zf == None or oprions.pl == None :
    print (parser.usage)
    exit()
else:
    zip_file = options.zf
    password_list = options.pl
    if os.path.isfile(zip_file) == True and os.path.isfile(password_list) == True:
        print("----------------------------------------------------------")
        open_password_list = open(password_list,"r")
        for p in open_password_list.readlines():
            try:
                password = password.rstrip("\n")
                zf = zipfile.ZipFile(zip_file,'r')
                zf.extractall(pwd=password.encode("utf-8"))
            except RunTimeError :
                print ("this is password [{0}] = False ".fromat(p))
            else:
                print ("this is password [{0}] = True".format(p))
                exit()
    else:
        print ("some thing not found")
                 
        
