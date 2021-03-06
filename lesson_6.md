### Графы
Многие задачи, например, задача обхода точек по кратчайшему маршруту, могут быть решены с помощью одного из мощнейших инструментов — с помощью графов.
Графами можно представить любую структуру или систему, от транспортной сети до сети передачи данных и от взаимодействия белков в ядре клетки до связей между людьми в Интернете. Вершины могут обозначать любые объекты: пользователей сайта, компьютеры корпоративной сети, населенные пункты на карте. Ребра отображают связи между этими объектами: каких пользователей тот или иной человек добавил в друзья, какие компьютеры объединяются прямым подключением, между какими городами проложены дороги. 

Ваши графы могут стать еще полезнее, если добавить в них дополнительные данные вроде весов или расстояний.

Графы бывают ориентированные и неориентированные. Ориентированные - у ребер есть направление. Куда можно двигаться.
Цикл в графе - маршрут из вершины в нее же саму. Дерево - граф в котором не циклов.

Разберемся с алгоритмами обхода графа.
Поиск в глубину, поиск в ширину. 
Мы находимся в определенной верщине и хотим найти вершину с определенным свойством.

Поиск в глубину: 
1) У нас есть вершина. Просматриваем одну из смежых вершин. И потом у новой просматриваем еще одну. Если она закончилась, то у первой новой просматриваем дальше

### Паттерны проектирования
Паттерн проектирования — это часто встречающееся решение определённой проблемы при проектировании архитектуры программ.

В отличие от готовых функций или библиотек, паттерн нельзя просто взять и скопировать в программу. Паттерн представляет собой не какой-то конкретный код, а общую концепцию решения той или иной проблемы, которую нужно будет ещё подстроить под нужды вашей программы.

Паттерны часто путают с алгоритмами, ведь оба понятия описывают типовые решения каких-то известных проблем. Но если алгоритм — это чёткий набор действий, то паттерн — это высокоуровневое описание решения, реализация которого может отличаться в двух разных программах.

Если привести аналогии, то алгоритм — это кулинарный рецепт с чёткими шагами, а паттерн — инженерный чертёж, на котором нарисовано решение, но не конкретные шаги его реализации.
Порождающие, поведенческие, структурные
Порождающие паттерны беспокоятся о гибком создании объектов без внесения в программу лишних зависимостей.

Структурные паттерны показывают различные способы построения связей между объектами.

Поведенческие паттерны заботятся об эффективной коммуникации между объектами.



#### Зачем знать паттерны

Вы можете вполне успешно работать, не зная ни одного паттерна. Более того, вы могли уже не раз реализовать какой-то из паттернов, даже не подозревая об этом.

Но осознанное владение инструментом как раз и отличает профессионала от любителя. Вы можете забить гвоздь молотком, а можете и дрелью, если сильно постараетесь. Но профессионал знает, что главная фишка дрели совсем не в этом. Итак, зачем же знать паттерны?

Проверенные решения. Вы тратите меньше времени, используя готовые решения, вместо повторного изобретения велосипеда. До некоторых решений вы смогли бы додуматься и сами, но многие могут быть для вас открытием.

Стандартизация кода. Вы делаете меньше просчётов при проектировании, используя типовые унифицированные решения, так как все скрытые проблемы в них уже давно найдены.

Общий программистский словарь. Вы произносите название паттерна, вместо того, чтобы час объяснять другим программистам, какой крутой дизайн вы придумали и какие классы для этого нужны.



- Синглтон
Одиночка — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа. Пример обьект доступа к базе данных.

``` python
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            # cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)
```
- Адаптер (в папке паттерны) 
- Декоратор (в папке паттерны) 
- Фабрика (в папке паттерны) 

Чтобы углубиться в эту тему и лучше понять - книга паттерны банды четырех + https://refactoring.guru/

