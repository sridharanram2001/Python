from sys import argv
script,user_name=argv
prompt=(">")
print(f"Hi {user_name} I am {script}")
print(f"Do you like me {user_name}")
likes=input(prompt)
print(f"What kind of computer do you have {user_name}")
type=input(prompt)
print(f"Where do you live {user_name}")
live=input(prompt)
print(f'''So you said {likes} about liking me 
          You have a {type} computer
          You live in {live}  ''')
 