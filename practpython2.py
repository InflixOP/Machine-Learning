# is_old=False
# if is_old:
#     print("you are old")
# else:
#     print("not old") 

# Ternary operator
'''
is_friend=False
can_message="message allowed" if is_friend else "not allowed"
print(can_message)
'''
#Short Circuiting

'''
is_friend=True
is_user=True

if is_friend and is_user:
    print("Best friends forever")
'''

#for loop
'''
for i in 'anubhav':
    print(i)

for i in [1,2,3,4]:
    for j in 'anu':
        print(i, j)
dict1={
    'name': 'Anubhav',
    'age':20,
    'prof': 'agaga'
}
for key,value in dict1.items():
    print(key,value)

for i in range(1,101):
    print(i)
    
for i,char in enumerate(list(range(100))):
    print(i+1,char)

'''
#functions

'''
def say_hello():
    print('hello')
say_hello() 

def say(name,emoji):
    print(f'hello {name} {emoji}')
say('Anubhav',':)'


def super(*args,**kwargs):
    total=0
    for i in kwargs.values():
        total+=i
    print(args)
    return sum(args),total

print(super(1,3,5,6,a=2,b=5))
'''
