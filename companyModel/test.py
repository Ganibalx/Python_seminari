from models import *
#создаем людей
customer = Create_people(name='Петр', lastname='Иванов', project='Строим дом')
manager = Create_people(post='manager', name='Илья', lastname='Сидоров')
foreman = Create_people(post='foreman', name='Виталя', lastname='Филимонов')
worker1 = Create_people(post='worker', name='Никита', lastname='Носков')
worker2 = Create_people(post='worker', name='Денис', lastname='Прошкин')
worker3 = Create_people(post='worker', name='Андрей', lastname='Лузин')
#заполняем склад
wh = Warehouse()
wh.add_materials({'кирпич': 10, 'шифер': 20, 'линолеум': 5})
wh.add_tooling({'молоток': 5, 'дрель': 2, 'трактор': 1, 'гвоздик': 20})
#последовательность строительства
manager.accept_customer(customer=customer, foreman=foreman)
manager.counting_material(foreman, {'кирпич': 3, 'шифер': 5, 'линолеум': 1})
manager.get_materials(foreman)
foreman.add_to_brigade(worker1, 'молоток')
foreman.add_to_brigade(worker2, 'трактор')
foreman.add_to_brigade(worker3, 'гвоздик')
foreman.get_mat_tol(wh)
print(f'дом построен? {foreman.build()}')