# Reading the "The Fender" Hacker's password file and pulling the compromised_users list for whom the password is hacked
import csv
compromised_users=[]
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

#Writing the collected information into compromised_users.txt file
with open("compromised_users.txt","w") as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

#Sending message to Boss using encoded messages in JSON format
import json
with open("boss_message.json","w") as boss_message:
  boss_message_dict = {"recipient":"The Boss","message":"Mission Success"}
  json.dump(boss_message_dict,boss_message)

#Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely and leave a message in the name of another hacker "Slash Null"
slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""

with open("new_passwords.csv","w") as new_password_csv:
  new_password_csv.write(slash_null_sig)


#Congrats! We fooled the Hacker












  
