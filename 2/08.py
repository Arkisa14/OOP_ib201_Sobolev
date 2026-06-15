class Person:
    def __init__(self, first_name: str, middle_name: str, last_name: str, phones: dict):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phones = phones
    
    def get_phone(self):
        return self.phones.get('private')
    
    def get_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    def get_work_phone(self):
        return self.phones.get('work')
    
    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.middle_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name: str, company_type: str, phones: dict, *employees):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = employees
    
    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for employee in self.employees:
            phone = employee.get_work_phone()
            if phone is not None:
                return phone
        return None
    
    def get_name(self):
        return self.name
    
    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}'

def send_sms(*recipients):
    for recipient in recipients:
        phone = recipient.get_phone()
        if phone is not None:
            print(f'Отправлено СМС на номер {phone} с текстом: {recipient.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {recipient.get_name()}')

