name1=input("interr frist name: ").lower()
name2=input("interr second name: ").lower()

name=name1+name2
def calculate_love_score():
    counter1=0
    counter2=0
    for i in "true":
        counter1=counter1+name.count(i)

    for k in "love":
        counter2=counter2+name.count(k)
    love_score = f"{counter1}{counter2}"
    return love_score
print("love score "+calculate_love_score())    
