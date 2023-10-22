from enum import Enum


class Human:
    """Базовый класс для людей в модели"""
    busy = 0

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Warehouse:
    """Это склад"""
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.tooling = {}
            cls.instance.materials = {}
        return cls.instance

    def add_materials(self, materials):
        for key in materials.keys():
            if key not in self.materials.keys():
                self.materials[key]=materials[key]
            else:
                self.materials[key] = self.materials[key] + materials[key]

    def add_tooling(self, tooling):
        for key in tooling.keys():
            if key not in self.materials.keys():
                self.tooling[key]=tooling[key]
            else:
                self.tooling[key] = self.tooling[key] + tooling[key]

    def issue_materials(self, key, kol):
        if key in self.materials.keys():
            if self.materials[key] >= kol:
                self.materials[key] = self.materials[key] - kol
            else:
                raise Exception(f'не хватает{key}, доступно {self.materials[key]}')
        else:
            raise Exception(f'нет такого материала на складе')

    def issue_tooling(self, key, kol):
        if key in self.tooling.keys():
            if self.tooling[key] >= kol:
                self.tooling[key] = self.tooling[key] - kol
            else:
                raise Exception(f'не хватает{key}, доступно {self.tooling[key]}')
        else:
            raise Exception(f'нет такого инструмента на складе')


class Customer(Human):
    """Класс заказчика"""
    def __init__(self, name, lastname, project):
        super().__init__(name, lastname)
        self.project = project


class Worker(Human):
    tooling = None

    def build(self):
        if self.tooling[0] == 1:
            return True
        else:
            return False


class Foreman(Human):
    ongoing_project = None
    need_to_get_materials = {}
    need_to_get_tooling = {}
    brigade = []

    def add_to_brigade(self, worker, tooling):
        if isinstance(worker, Worker):
            if self.ongoing_project and not worker.busy:
                self.brigade.append(worker)
                worker.tooling = [0, tooling]
                worker.busy = 1
                if tooling in self.need_to_get_tooling.keys():
                    self.need_to_get_tooling[tooling] = self.need_to_get_tooling[tooling] + 1
                else:
                    self.need_to_get_tooling[tooling] = 1
            else:
                raise Exception('Нет проекта или работник уже занят')
        else:
            raise Exception('Не передан рабочий')

    def get_mat_tol(self, wh):
        if isinstance(wh, Warehouse):
            for k, v in self.need_to_get_materials.items():
                wh.issue_materials(k, v)
            self.need_to_get_materials = None
            for k, v in self.need_to_get_tooling.items():
                wh.issue_tooling(k, v)
                for worker in self.brigade:
                    if worker.tooling[1] == k and worker.tooling[0] == 0:
                        worker.tooling[0] = 1
            self.need_to_get_tooling = None

    def build(self):
        if not self.need_to_get_tooling and not self.need_to_get_materials:
            if all([i.build() for i in self.brigade]):
                for worker in self.brigade:
                    worker.busy = 0
                self.busy = 0
                self.brigade = []
                return True
            return False
        return False

class Manager(Human):
    foreman_project = None

    def accept_customer(self, *, customer, foreman):
        if isinstance(customer, Customer) and isinstance(foreman, Foreman):
            if customer.busy == foreman.busy == self.busy == 0:
                customer.busy = foreman.busy = self.busy = 1
                foreman.ongoing_project = customer.project
                self.foreman_project = {foreman.lastname: {}}
            else:
                raise Exception(f"кто то занят другим делом")
        else:
            raise Exception("Требуется передача других параметров")

    def counting_material(self, foreman, materials):
        self.foreman_project[foreman.lastname] = materials

    def get_materials(self, foreman):
        if isinstance(foreman, Foreman):
            if foreman.lastname in self.foreman_project.keys():
                foreman.need_to_get_materials = self.foreman_project[foreman.lastname]
                self.foreman_project = None
                self.busy = 0


class Posts(Enum):
    """Должности в организации"""
    manager = Manager
    foreman = Foreman
    worker = Worker


class Create_people:
    def __new__(cls, *, post=None, name, lastname, project=None):
        if post:
            return Posts[post].value(name, lastname)
        elif project:
            return Customer(name, lastname, project)
        else:
            raise Exception("Что за хуйня?")
