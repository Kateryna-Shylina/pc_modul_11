from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    
    def __str__(self):
        return str(self.__value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        required = True
 

class Phone(Field):
    def __init__(self, value):    
        super().__init__(value)
        required = False
            
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Wrong phone number")
        else: 
            self.__value = value
               

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        required = False

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value != "":
            try:
                birthday_day = datetime.strptime(value, '%d.%m.%Y')
                self.__value = value
            except:
                raise ValueError("Wrong date format")


class Record:
    def __init__(self, name, birthday = ""):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
        
    def edit_phone(self, old_phone, new_phone):   
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.remove_phone(old_phone)                
                break
        else:
            raise ValueError
        
    def remove_phone(self, phone_number):
        index = -1
        for phone in self.phones:
            index += 1
            if phone.value == phone_number:
                break
        else:
            raise ValueError

        self.phones.pop(index)

    def days_to_birthday(self):
        if self.birthday.value == "":
            return None
        
        current_day = datetime.now().date()
        birthday_day = datetime.strptime(self.birthday.value, '%d.%m.%Y')
        birthday_day = datetime(year=current_day.year, month=birthday_day.month, day=birthday_day.day, hour=0).date()
        if birthday_day >= current_day:
            days = birthday_day - current_day
        else:
            birthday_day = datetime(year=current_day.year+1, month=birthday_day.month, day=birthday_day.day, hour=0).date()
            days = birthday_day - current_day
        
        return days

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for key, record in self.data.items():
            if key == name:
                return record
        
    def delete(self, name):
        for key, record in self.data.items():
            if key == name:
                del self.data[name]
                break

    def iterator(self, n):
        values = list(self.data.values())
        for i in range(0, len(values), n):
            yield '\n'.join(map(str, values[i:i+n]))

    """
    def iterator(self, n):
        counter = 0
        while counter < len(self.data):
            i = 0
            for value in self.data.values():
                if i >= counter and i < counter + n:
                    result += str(value) + '\n'
                i += 1
            yield result
            counter += n   
    """

if __name__ == '__main__':
    book = AddressBook()
    kate_record = Record("Kate", "13.01.1988")
    kate_record.add_phone("1234567890")
    book.add_record(kate_record)
    
    print(kate_record.days_to_birthday())

    record1 = Record("Kate1")
    record1.add_phone("1234567890")
    book.add_record(record1)

    record2 = Record("Kate2")
    record2.add_phone("1234567890")
    book.add_record(record2)

    record3 = Record("Kate3")
    record3.add_phone("1234567890")
    book.add_record(record3)

    record4 = Record("Kate4")
    record4.add_phone("1234567890")
    book.add_record(record4)

    record5 = Record("Kate5")
    record5.add_phone("1234567890")
    book.add_record(record5)

    record6 = Record("Kate6")
    record6.add_phone("1234567890")
    book.add_record(record6)


    iter = book.iterator(4)
    for i in iter:
        print(i)