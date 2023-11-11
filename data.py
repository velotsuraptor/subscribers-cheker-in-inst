from history_of_subscribers import *
import records

def set_name():
    from datetime import date
    today = date.today()
    dd = today.strftime("%d_%m_%Y_")
    # You are free to replace the string 'account' with any name you want but don't forget to put singular ' at the
    # beginning and the end of the string, so you don't break the code.
    name = 'subs' + dd + 'account'
    return name


def define_subscriber(l1):
    new_list = []
    st1 = ''
    # Replace the next line variable's value with your languages equivalent please so everything worked!
    edited_p = 'Основна світлина'
    '''I'm sorry but I'm Ukrainian and ny Instagram is in Ukrainian and that's why this code won't work with 
       your data. I highly recommend you replace the 'Основна світлина' in this code with your language's 
       equivalent so your code could work. There no other things you will need to do manually except copying 
       the subscribers. Would be thankful to anyone who will explain me the way me I can automate it!'''
    for item in l1:
        if len(item) > 17:
            new_list.append(item)
        for i in new_list:
            if edited_p not in i:
                new_list.remove(i)
    for i in new_list:
        st1 += i + ' '
    st1 = st1.replace(edited_p, '')
    return set(st1.split())


def rewrite_records():
    try:
        with open('records.py', 'r') as f:
            file_data = f.read()
        with open('records.py', 'w') as f:
            if len(records.all_saved) == 0:
                f.write(str(file_data[:-1] + "'" + set_name() + "'"+ "]"))
                return 0
            else:
                f.write(file_data)
            if file_data.strip() and file_data[-2] != '[':
                f.write(',')
            f.write("'" + set_name() + "'")
            f.write(']')
            return 0

    except FileNotFoundError:
        print("Error: File not found.")
        return 2
    except IOError:
        print("Error: Unable to read or write the file.")
        return 3


def append_data_to_file(subs):
    with open('history_of_subscribers.py', 'a+') as f:
        file_content = f'{set_name()} = {subs}\n'
        f.write(file_content)

