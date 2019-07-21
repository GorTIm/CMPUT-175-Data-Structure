# reads the contents of the file and returns a list of lines
def read_numbers(filename):
    
    file_object = open (filename)
    whole_file=file_object.readlines()
    return whole_file

# takes a number in a free format and returns the standard form xxx-xxx-xxxx
def standarize(phone_number):
    temp_list = []
    temp_newList = []
    times = 0
    for letters in phone_number:
            if letters == '-':
                pass
            else:
                temp_list.append(letters)    
           
    while times != 10:
            letters = temp_list[times]
       
            try:
                temp = int (letters)
               
            except:
                temp = key_map [letters]
               
            temp_newList.append(str(temp))
            if times == 2 or times == 5:
                temp_newList.append('-')
            times += 1
    return ''.join(temp_newList)
               
   
   
           

# takes a phone number in the standard form and returns the sum of its digits
def sum_of_digits(phone_number):
    sum_of_num = 0
    for x in phone_number:
        if x == '-':
            pass
        else:
            sum_of_num = sum_of_num + int(x)
    return sum_of_num  
   
# takes a list of phone numbers and returns the highest sum of digits
def find_highest_sum(phone_list):
    highest = 0
    for line in phone_list:
        temp = sum_of_digits(line)
        if temp >= highest:
            highest = temp
           
    return highest

key_map = {'A':'2', 'B':'2', 'C':'2',
           'D':'3', 'E':'3', 'F':'3',
           'G':'4', 'H':'4', 'I':'4',
           'J':'5', 'K':'5', 'L':'5',
           'M':'6', 'N':'6', 'O':'6',
           'P':'7', 'Q':'7', 'R':'7', 'S':'7',
           'T':'8', 'U':'8', 'V':'8',
           'W':'9', 'X':'9', 'Y':'9', 'Z':'9',
           }

# main program

phone_list = read_numbers("phones.txt")


phone_list = [ standarize(x) for x in phone_list ]
 
highest_sum = find_highest_sum(phone_list)

for number in phone_list:
    if sum_of_digits(number) == highest_sum:
        print(number, '*')
    else:
        print(number)