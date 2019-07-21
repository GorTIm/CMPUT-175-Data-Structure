def read_file(filename):
    file_object=open(filename)
    whole_file=file_object.readlines()
    return whole_file 

def check_status():
    filename=input('Enter the input filename:')
    sudoku_list=read_file(filename)
    
    check_block(sudoku_list)

def check_block(puzzle):
    Row_count=0
    Column_count=0
    while Row_count<=6:
        while Column_count<=6:
            temp_list=[]
            for j in range(0+Column_count,3+Column_count):
                for i in range(0+Row_count,3+Row_count):
                    check(puzzle[i][j],temp_list)
            Column_count+=3
        Row_count+=3

def check(letter,temp_list):
    if letter in temp_list:
        print('The puzzle is not valid!')
    if  letter=='0':
            pass
    else:
        temp_list.append(letter)     

check_status()