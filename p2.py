n1=input("enter your firist name ")
n2=input("enter your firist name ")
def format_name(f_name, l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs."
    fn=f_name.title()
    ln=l_name.title()
    return f"{fn} {ln}"
print(format_name(n1, n2))

