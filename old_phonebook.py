# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import time
import re
def show_menu():
    print('\n***Телефонная книжка***\n'
          '1. Отоброзить весь справочник\n'
          '2. Найти абонента по фамилии\n'
          '3. Найти абонента по номеру\n'
          '4. Добавить абонента в справочник\n'
          '5. Изменить номер телефона\n'
          '6. Удалить абонента\n'
          #'7. Сохранить справочник\n'
          '7. Закончить работу\n')
    
    while True:
        try :
            choice = int(input('Выберите необходимое действие: ' ))
            if choice < 1 or choice > 7:
                #choice = int(input('Выберите необходимое действие: ', ))
                work_with_phonebook()
            break
        except:
            print('Ошибка ввода')    
    return choice

#1. Отоброзить весь справочник (по алфавиту)
def read_show(filename):
    print('\n***Распечатан весь телефонный справочник***')
    with open(filename, 'r', encoding='utf-8') as data:
        names = data.readlines()
        phonebook = sorted(names)

    print(*phonebook)

#1.1 прочитать справочник    
def read_txt(filename): #читает и присваивает ключи
    phone_book = []
    fields = ['Фамилия','Имя','Телефон']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

#2. Найти абонента по фамилии  
def find_by_lastname(filename, last_name):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if last_name in line:
                phone_book.append(line)

    return phone_book

#3. Найти абонента по номеру  
def find_by_number(filename, number):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if number in line:
                phone_book.append(line)

    return phone_book

#4. записать нового абонента
def write_txt(filename , phone_book):
    with open(filename,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}')


#4.1 Добавить нового абонента
def add_user(user_lastname, user_number, user_firstname=''):
    with open('temp.txt', 'w' ,encoding='utf-8') as data:
        data.write(user_lastname +' ' + user_firstname + ' '+ user_number +' \n' )
    new_data = read_txt('temp.txt')
    return new_data

#5 Изменить номер телефона абонента
def change_number(filename, phone_book, last_name, new_number):
    temp = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if last_name in line:
                temp.append(line)
                old_user = line

    phone_book = temp[-1].split()
    with open('del.txt', 'w', encoding='utf-8') as data:
        data.write(old_user)
    with open('del.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
 
    del phone_book[-1] #удаляем по индексу последнию запись в списке(номер телефона)
    phone_book.append(new_number)#добавляем новый номер в список абонента
    user_lastname = str(*phone_book[0:1])
    user_number = str(*phone_book[2:3])
    user_firstname = str(*phone_book[1:2])
    new_data = add_user(user_lastname, user_number, user_firstname)#добавляет как нового абонента в temp

    return new_data


def read_del_user(filename, old_user):#читаем временный фаил для удаления абонента
    with open(old_user, 'r', encoding='utf-8') as file:
        user = file.readlines()

    return user #возвращаем list абонента для дальнейшего удаления

def del_user(filename, old_user):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    pattern = re.compile(re.escape(old_user))
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)


#Программа телефонный справочник! СТАРТ
def work_with_phonebook():
	
    choice = show_menu() #меню

    filename = 'old_phonebook.txt'

    phone_book = read_txt('old_phonebook.txt')

    while (choice != 8):
        if choice == 1: #'1. Отоброзить весь справочник'
            read_show(filename)
            input('Для продолжения нажмите [Enter] . . .')        
        elif choice == 2: #'2. Найти абонента по фамилии'
            last_name = input('Ввидите Фамилию: ').upper()
            print('Совпадения: ', *find_by_lastname(filename, last_name), sep='\n')
            input('Для продолжения нажмите [Enter] . . .')

        elif choice == 3: #'3. Найти абонента по номеру'
            number = input('Ввидите номер: ')
            print('Совпадения: ', *find_by_number(filename, number), sep='\n')
            input('Для продолжения нажмите [Enter] . . .')

        elif choice == 4: #'4. Добавить абонента в справочник'
            print('\n***Добавить нового абонента в телефонную книгу***\n')
            user_lastname = input('Видите *Фамилию:').upper()
            user_firstname = input('Видите Имя:').upper()
            user_number = input('Видите номер *Телефона:')
            new_data = add_user(user_lastname, user_number, user_firstname)
            #print(type(new_data), new_data)
            print('Абонент добавлен!')
            write_txt(filename ,phone_book + new_data) #добавить в словарь новый словарь и записать в книгу
            time.sleep(3)          

        elif choice == 5: #'5. Изменить номер абонента\n'
            last_name = input('Ввидите фамилию: ').upper()
            new_number = input('Ввидите новый номер: ')
                 
            new_data = change_number(filename, phone_book, last_name, new_number)#возвращает запись в temp.txt(как нового абонента)
            write_txt(filename, phone_book + new_data)#записывает как нового абонента из temp в phonebook
            old_user = str('del.txt')
            user = str(*read_del_user(filename, old_user))#возвращается строка для удаления
            del_user(filename, user)#запускаем удаление старой записи
            print('Номер абонента изменен')
            time.sleep(3) 

        elif choice == 6: #'6. Удалить абонента\n'
            print('\n ***Удаления Абонента***\n'
                  'Ввидите Фамилию и Имя для удаления, например: Попов Алексей\n')
            last_name = input('Ввидите фамилию и Имя для удаления: ').upper()
            if len(last_name) == 0:
                print('***Ошибка***')
                time.sleep(2) 
                work_with_phonebook()
            print('Вы хотите удалить абонента', *find_by_lastname(filename, last_name), 
                  '\n 1. - Да', '\n 2. - Нет')
            #yes_no = input('Выберите необходимое действие: ' )

            while True:
                try:
                    yes_no = int(input('Выберите необходимое действие: ' ))
                    if yes_no > 0 or yes_no < 3:
                        if yes_no == 1:
                            del_user(filename, last_name)
                            print('Номер абонента удален!')
                            time.sleep(3) 
                        elif yes_no == 2:
                            print('***Отмена***')
                            time.sleep(2)                        
                            work_with_phonebook()
                    else:
                        print('***Ошибка***')
                        work_with_phonebook()
                        time.sleep(3)
                    #print('***Ошибка***')
                    time.sleep(3)    
                    work_with_phonebook()                     
                    break
                except:
                    print('Ошибка ввода')

        # elif choice == 7: #'7. Сохранить справочник\n'
        #     print('7')

        elif choice == 7: #'7. Закончить работу'
            print('Програма закрыта')
            break
                                

        choice = show_menu()   
 

work_with_phonebook()
               