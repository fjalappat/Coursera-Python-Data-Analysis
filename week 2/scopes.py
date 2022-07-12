count = 0
def show_count():
    print(count)

def set_count(c):
    count = c
    print(count)

def set_global_count(c):
    global count 
    count = c
    print(count)


if __name__ == '__main__':
    show_count()
    set_count(argv)
    