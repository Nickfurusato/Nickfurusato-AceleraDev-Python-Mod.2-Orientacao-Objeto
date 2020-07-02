from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):  # utilizando o metodo
    def __init__(self, code, name, salary, department):
        self.__department = department
        self.code = code
        self.name = name
        self.salary = salary

    def get_department(self):
        return self.__department.name

    def set_department(self, dept_name):
        self.__department.name = dept_name

# aplicando o abstractmethod nas instâncias de bonus e get_hours

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, total_sales):
        self.__sales += total_sales

    def calc_bonus(self):
        return self.__sales * 0.15
