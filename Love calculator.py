print("*** Welcome to Love Calculator ***")
name1=input("what is your name ? ")
name2=input("What is their name ? ")

name1=name1.lower()
name2=name2.lower()
true =0
true=true+name1.count("t")
true=true+name1.count("r")
true=true+name1.count("u")
true=true+name1.count("e")

true=true+name2.count("t")
true=true+name2.count("r")
true=true+name2.count("u")
true=true+name2.count("e")



love =0
love=love+name1.count("l")
love=love+name1.count("o")
love=love+name1.count("v")
love=love+name1.count("e")

love=love+name2.count("l")
love=love+name2.count("o")
love=love+name2.count("v")
love=love+name2.count("e")

lovescore=true*10+love


if lovescore<10 or lovescore>90:
    print(f"Your score is {lovescore} and you are togather llike coke and mentos.")

elif lovescore>=40 and lovescore<=50 :
    print(f"Your score is {lovescore} and you are alright together.")
else:
    print(f"Your lovescore is {lovescore}")