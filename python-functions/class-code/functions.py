def print_name(name, *args):
    print(name)
    print(args[2])


print_name("Yusuf",100,200,300)


my_list = [1,2,3]

print(sum(my_list))




def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_numbers(1,2,3)


def search_filter(**kwargs):
    print(kwargs)


search_filter(price=50, brand="dell")





print(max([1,2,3]))



def normal_double(num):
    return num*2

double_function = lambda num : num*2


print(double_function(3))
print(normal_double(3))



my_ages = [21,20,15,35,12]

filter_function = lambda num : num >18

def normal_filter_function(num):
    return num >18

print(list(filter(lambda num : num >18 ,my_ages)))

print(list(map(lambda num : num*2,my_ages)))