def format_name(f , n):
    print(f.title())
    print(n.title())
format_name("AAlu",  "BHAlu")


#or



def format_name(f , n):
    f_name = f.title()
    n_name = n.title()
    print(f"{f_name} {n_name}")
format_name("AAluaa",  "BHAluaa")


#or

def format_name(f , n):
    f_name = f.title()
    n_name = n.title()
    return f"{f_name} {n_name}"
print(format_name("AAluaa",  "BHAluaa"))





def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)