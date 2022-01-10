class Employee:
    def __init__(self):
        print('Employee Id Created')

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()

    return obj
    print('function end...') 

print('Calling Create_obj() function...')
obj = Create_obj()
