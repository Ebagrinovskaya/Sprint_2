from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # По умолчанию рейтинг у добавленной книги 1
    def test_add_new_book_default_rating_1(self):
        name = 'Маугли'
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (len(collector.get_books_rating()) == 1) and collector.get_book_rating(name) == 1

    # Нельзя добавить одну книгу дважды
    def test_add_new_book_1_book_twice_error(self):
        name = 'Анна Каренина'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, 5)
        collector.add_new_book(name)
        assert (len(collector.get_books_rating()) == 1) and collector.get_book_rating(name) == 5

    # Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_book_not_in_collection_error(self):
        collector = BooksCollector()
        name = 'Молчание ягнят'
        collector.set_book_rating(name, 5)
        assert (len(collector.get_books_rating()) == 0) and collector.get_book_rating(name) == None

    # Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_less_than_1_error(self):
        name = 'Хребты безумия'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, 0)
        assert collector.get_book_rating(name) == 1

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_more_than_10_error(self):
        name = 'Сияние'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, 11)
        assert collector.get_book_rating(name) == 1

    # У недобавленной книги нет рейтинга
    def test_get_book_rating_book_not_in_collection(self):
        name = 'Мешок с костями'
        collector = BooksCollector()
        assert collector.get_book_rating(name) == None

    # Проверка получения списка книг с рейтингом 8, когда их в списке 2
    def test_get_books_with_specific_rating_show_rating_8_result_not_empty(self):
        name1 = 'Темный карнавал'
        name2 = 'Канун всех святых'
        name3 = 'Черная месса'
        name4 = 'Дракула'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.set_book_rating(name1, 8)
        collector.add_new_book(name2)
        collector.set_book_rating(name2, 3)
        collector.add_new_book(name3)
        collector.set_book_rating(name3, 8)
        collector.add_new_book(name4)
        collector.set_book_rating(name4, 9)
        result = collector.get_books_with_specific_rating(8)
        assert (len(result) == 2) and (name1 in result) and (name3 in result)

    # Проверка получения списка книг с рейтингом 6, когда их в списке нет
    def test_get_books_with_specific_rating_show_rating_6_result_empty(self):
        name1 = 'Спящие красавицы'
        name2 = 'Призраки дома на холме'
        name3 = 'Хрупкие вещи'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.set_book_rating(name1, 3)
        collector.add_new_book(name2)
        collector.set_book_rating(name2, 7)
        collector.add_new_book(name3)
        collector.set_book_rating(name3, 5)
        result = collector.get_books_with_specific_rating(6)
        assert (len(result) == 0)

    # Проверка получения списка добавленных книг
    def test_get_books_rating_add_3_books(self):
        name1 = 'Спящие красавицы'
        name2 = 'Призраки дома на холме'
        name3 = 'Хрупкие вещи'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.set_book_rating(name1, 3)
        collector.add_new_book(name2)
        collector.set_book_rating(name2, 7)
        collector.add_new_book(name3)
        collector.set_book_rating(name3, 5)
        result = collector.get_books_rating()
        assert (len(result) == 3) and (result[name1] == 3) and (result[name2] == 7) and (result[name3] == 5)

    # Добавление книги в избранное
    def test_add_book_in_favorites_add_one_book(self):
        name = 'Кристина'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 1) and (name in favs)

    # Добавление нескольких книг в избранное
    def test_add_book_in_favorites_add_two_book(self):
        name1 = 'Кристина'
        name2 = 'Туман'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name1)
        collector.add_book_in_favorites(name2)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 2) and (name1 in favs) and (name2 in favs)

    # Нельзя добавить книгу в избранное, если нет в словаре books_rating
    def test_add_book_in_favorite_book_not_in_collection_error(self):
        name = 'Мертвая зона'
        collector = BooksCollector()
        collector.add_book_in_favorites(name)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 0)

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self):
        name = 'Мизери'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 0)

    # Проверка удаления книги из избранного, когда добавлено 2 книги
    def test_delete_book_from_favorites_delete_one_of_two_books(self):
        name1 = 'Коллекционер'
        name2 = 'Преступление и наказание'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name1)
        collector.add_book_in_favorites(name2)
        collector.delete_book_from_favorites(name1)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 1) and (name2 in favs)

    # Проверка получения списка добавленных в избранное книг
    def test_get_list_of_favorites_books_2_books(self):
        name1 = 'Коллекционер'
        name2 = 'Преступление и наказание'
        collector = BooksCollector()
        collector.add_new_book(name1)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name1)
        collector.add_book_in_favorites(name2)
        favs = collector.get_list_of_favorites_books()
        assert (len(favs) == 2) and (name1 in favs) and (name2 in favs)
