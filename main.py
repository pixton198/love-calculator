print("The Love Calculator is calculating your score...")
name1 = input() 
name2 = input() 
comb_name = name1+name2
lower_name=comb_name.lower()
t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
first_digit=t+r+u+e
l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
second_digit=l+o+v+e
love_score=int(str(first_digit)+str(second_digit))
if (love_score<10) or (love_score>90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<=love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
   print(f"Your score is {love_score}.")