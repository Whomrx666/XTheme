# -*- coding: utf-8 -*-
# XTheme/main/th13.py
# Credit by Mr.X
import os, sys, time, shutil
from support.echo import xtheme, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th13():
    os.system("clear")
    print(xtheme)
    print(f"        {abu}XTHEME {pxh} Evil Geniuses {netral}")
    print(f"\n{putih}({kuning}*{putih}) {abu}'username' and 'team name' will be displayed below the logo")
    username = input(f"\n{putih}enter username   {hijau}>{putih} ")
    while not username.strip() or '"' in username or "'" in username:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!!")
        username = input(f"\n{putih}enter username   {hijau}>{putih} ")
        continue
    time.sleep(0.5)
    team = input(f"\n{putih}enter team name  {hijau}>{putih} ")
    while not team.strip() or '"' in team or "'" in team:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!! ")
        team = input(f"\n{putih}enter team name  {hijau}>{putih}")
        continue
    print(f"\n{putih}[{hijau}!{putih}] changing the Termux theme  ")
    load()
    file = "theme.py"
    fill = """#Created with the XTHEME coded by Mr.X
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[97m                    ^P7                      
                  ~5&@7                      
                !G@@@@7                      
              7B@@@@@@7  ~PYJ7~:             
           .?B@@@@@@@@7  7@@@@@&#P?^         
         :J#@@@@@@@@@@7  7@@@@@@@@@@B?:      
       :Y&@@@@@@@@@@@@7  7@@@@@@@@@@@@&Y:    
      7&@@@@@@@@@@@@&#!  !#&@@@@@@@@@@@@&7   
     Y@@@@@@@@@@&P?~:      :~?P&@@@@@@@@@@5  
    Y@@@@@@@@@&J:              :~~~~~~~~~~~. 
   !@@@@@@@@@@J^~~~~^      ^~~~~~~~~~~~~~~~~:
   B@@@@@@@@@@@@@@@@G      G@@@@@@@@@@@@@@@@B
   @@@@@@@@@@@@@@@@@G      G@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@G      G@@@@@@@@@@@@@@@@@
   B@@@@@@@@@@@@@@@@G      G@@@@@@@@@@@@@@@@B
   !@@@@@@@@@@J^~~~~^      ^~~~~^J@@@@@@@@@@!
    Y@@@@@@@@@&J:              :J&@@@@@@@@@Y 
     Y@@@@@@@@@@&P?~:      :~?P&@@@@@@@@@@Y  
      7&@@@@@@@@@@@@&#!  !#&@@@@@@@@@@@@&7   
       :Y&@@@@@@@@@@@@7  7@@@@@@@@@@@@&Y:    
         :?B@@@@@@@@@@7  7@@@@@@@@@@#J:      
            ^?P#&@@@@@7  7@@@@@@@@B?.        
                :~7JYP~  7@@@@@@B7           
                         7@@@@G!             
                         7@&5~               
                         7P^                  '''
run(logo)
print('''              \033[97m Username : \033[30;47m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''')  """
    with open(file, "w") as y:
        y.write(fill)
    of = "theme.py"
    into = os.path.join(os.environ["HOME"], "..", "usr", "etc", "theme.py")
    und = os.path.join(os.environ["HOME"], "..", "usr", "etc", "motd")
    if os.path.exists(into):
        os.remove(into)
    elif os.path.exists(und):
        os.remove(und)

    while True:
        try:
            shutil.move(of, into)
            message("theme")
            break
        except Exception as e:
            with open(file, "w") as y:
                y.write(fill)
            time.sleep(1)
