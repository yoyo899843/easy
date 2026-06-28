#!/usr/bin/env python3
from random import randint

print("===== Welcome to digital recognition game =====")
print("Can you help me recognize some digits?")

digits = [
"""
  ###   
 #   #  
#     # 
#     # 
#     # 
 #   #  
  ###
""",
"""
   #   
  ##   
 # #   
   #   
   #   
   #   
 #####
""",
"""
 #####  
#     # 
      # 
 #####  
#       
#       
#######
""",
"""
 #####  
#     # 
      # 
 #####  
      # 
#     # 
 #####
""",
"""
#       
#    #  
#    #  
#    #  
####### 
     #  
     #
""",
"""
####### 
#       
#       
######  
      # 
#     # 
 #####
""",
"""
 #####  
#     # 
#       
######  
#     # 
#     # 
 #####
""",
"""
####### 
#    #  
    #   
   #    
  #     
  #     
  #
""",
"""
 #####  
#     # 
#     # 
 #####  
#     # 
#     # 
 #####
""",
"""
 #####  
#     # 
#     # 
 ###### 
      # 
#     # 
 #####
"""
]

for i in range(1, 100 + 1):
    print("----- wave {}/100 -----".format(i))
    x = randint(0, 9)
    print(digits[x])
    ans = input('What is this digit? ')
    if int(ans) == x:
        print("You are right.")
    else:
        print("No, Your eye is malfunctioned.")
        exit()

with open('./flag') as f:
    print(f.read())
