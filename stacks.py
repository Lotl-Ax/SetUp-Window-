'''
procedural code snippets to simulate a stack
* check pre-conditions before push, pop or peek operations
'''

stack = []
print(stack)

max = 10
stack_pointer = -1

def push(item):

    if stack_pointer != max: # check stack pointer is not on the last index

        sp +=1  # increment the stack pointer by 1
        print(sp)
        stack[sp] = item # place the new item where stackpointer currently is
        
        print(stack)

    else:
        print('cry')

    pass

#end def

def pop():

    pass

#end def

def peek():

    pass

#end def

def get_item():

    valid = False
    while not valid:

        try:
            item = int(input("Enter Number > "))
            valid = True
        except ValueError:
            print("Not an integer")
        #end except

    #end while

    return item

#end def

# main
exit = False
while not exit:

    op = input("[p]ush, p[o]p, p[e]eek or e[x]it > ").lower()
    if op not in "poex":
        print("Invalid Op")
    elif op == "x":
        exit = True
    elif op == "p":
        item = get_item()
        result = push(item)
    elif op == "o":
        result = pop
    elif op == "e":
        result = peek
    #end if

#end while

print("End")