from enum import Enum


class UserException(Exception):
    def __init__(self, msg):
        super.__init__(msg)


class Warehouse:
    def __init__(self, items: dict):
        self._items = items

    def get_items(self, item, count):
        if item not in self._items:
            raise UserException(f'Нет {item}')
        if self._items[item] < count:
            raise UserException(f'Не достаточное кол-во на складе {item}')
        self._items[item] -= count


class Customer:
    """Класс заказчика"""
    def __init__(self, project):
        self._project = project

    def get_project(self):
        return self._project


class Worker:
    def __init__(self, tooling):
        self.tooling = tooling

    def build(self):
        if self.tooling[0] == 1:
            return True
        else:
            return False


class Foreman:

    def __init__(self, need_to_get_items):
        self._need_to_get_items = need_to_get_items
        self._brigade = []

    def add_worker_in_brigade(self, tooling):
        self._brigade.append(Worker(tooling))
        self._need_to_get_items[tooling] = self._need_to_get_items.setdefault(tooling, 0) + 1

    def get_items_in_wh(self, wh: Warehouse):
        if not isinstance(wh, Warehouse):
            raise UserException('это не склад')
        for k, v in self._need_to_get_items.items():
            wh.get_items(k, v)
        self._need_to_get_items = None
        for worker in self._brigade:
            worker.tooling[0] = 1

    def build(self):
        if self._need_to_get_items:
            return False
        return all([i.build() for i in self._brigade])


class Manager:

    def __init__(self, project):
        self.project = project

    def start_project(self, material: dict):
        return Foreman(material)


