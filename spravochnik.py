# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

class Rec:
    def __init__(self):
        self.name = ''
        self.tel = ''
        self.addr = ''

    def enter(self):
        self.name = input('Введите имя: ')
        self.tel = input('Введите телефон: ')
        self.addr = input('Введите адрес: ')

    def __str__(self):
        return self.name + ' tel ' + self.tel + ' addr ' + self.addr

recs = []

while (True):
    print('Записи')
    if (len(recs) == 0):
        print('  пусто')

    for i, r in enumerate(recs):
        print('  ' + str(i) + '. ' + str(r))

    print('1. Добавить')
    print('2. Удалить')
    print('3. Редактировать')
    print('4. Сохранить')
    print('5. Загрузить')
    print('6. Экспорт в JSON')
    print('7. Экспорт в XML')
    print('8. Экспорт в CSV')
    print('0. Выход')

    n = int(input('Выберите: '))

    if (n == 0):
        break
    if (n == 1): #Добавить
        r = Rec()
        r.enter()
        recs.append(r)
    if (n == 2): #Удалить
        i = int(input('Введите индекс: '))
        del recs[i]

    if (n == 3): #Редактировать
        r = recs[i]
        r.enter()

    if (n == 4): #Сохранить
        f = open('db.txt', 'wt')
        f.write(str(len(recs)) + '\n')

        for r in recs:
            f.write(r.name + '\n')
            f.write(r.tel + '\n')
            f.write(r.addr + '\n')
        f.close()

    if (n == 5): #Загрузить
        f = open('db.txt', 'rt')
        recs = []
        cnt = int(f.readline())
        for i in range(cnt):
            r = Rec()
            r.name = f.readline().strip()
            r.tel = f.readline().strip()
            r.addr = f.readline().strip()

            recs.append(r)
        f.close()

    if (n == 6): #Экспорт в JSON
        f = open('db.json', 'wt')
        f.write('[\n')
        for i, r in enumerate(recs):
            z = ","
            if (i == len(recs)-1):
                z = ""

            f.write('{ "name": "%s", "tel": "%s", "addr": "%s" }%s \n' %
                     (r.name, r.tel, r.addr, z))
        f.write(']\n')
        f.close()
    if (n == 7): #Экспорт в XML
        f = open('db.xml', 'wt')
        f.write('<db>\n')
        for r in recs:
            f.write(' <rec>\n')
            f.write(' <name>%s</name><tel>%s</tel><addr>%s</addr>\n' % (r.name, r.tel, r.addr))
            f.write('</res>\n')
        f.write('</db>\n')
        f.close()
    if (n == 8): #Экспорт в CSV
        f = open('db.csv', 'wt')
        f.write('name;tel;addr\n')
        for r in recs:
            f.write( '%s;%s;%s\n' % (r.name, r.tel, r.addr))
        f.close()