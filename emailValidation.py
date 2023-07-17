email = input("Enter Email: ")
k,j,d=0,0,0
#email should be atleast of 6 charachter
if len(email)>=6:
#email should start with aplhabet only
    if email[0].isalpha():
#email should contain only one @ symbol
        if ("@"in email) and (email.count("@")==1):
            if (email[-3]=="." )^(email[-4]=="."):  #"^"xor used not or symbol.
              for i in email:
                  if i==i.isspace():
                      k=1
                  elif i.isalpha():
                      if i==i.upper():
                          j=1
                  elif i.isdigit():
                      continue
                  elif i=="_" or i=="." or i=="@":
                      continue
                  else:
                      d=1          
                      
              if k==1 or j==1 or d==1:
                   print("Wrong Email with condition no. 5")
              else:
                  print("Right Email")
              
            else:
                 print("Wrong Email with condition no. 4")
                
        else:
             print("Wrong Email with condition no. 3")
    else:
         print("Wrong Email with condition no. 2")
        
else:
    print("Wrong Email with condition no. 1")
