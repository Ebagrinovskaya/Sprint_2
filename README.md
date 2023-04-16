# qa_python
Sprint_2

Автотесты для проверки класса BooksCollector

Проверяет добавление двух книг
test_add_new_book_add_two_books

По умолчанию рейтинг у добавленной книги 1
test_add_new_book_default_rating_1

Нельзя добавить одну книгу дважды
test_add_new_book_1_book_twice_error

Нельзя выставить рейтинг книге, которой нет в списке
test_set_book_rating_book_not_in_collection_error

Нельзя выставить рейтинг меньше 1
test_set_book_rating_less_than_1_error

Нельзя выставить рейтинг больше 10
test_set_book_rating_more_than_10_error

У недобавленной книги нет рейтинга
test_get_book_rating_book_not_in_collection

Проверка получения списка книг с рейтингом 8, когда их в списке 2
test_get_books_with_specific_rating_show_rating_8_result_not_empty

Проверка получения списка книг с рейтингом 6, когда их в списке нет
test_get_books_with_specific_rating_show_rating_6_result_empty

Проверка получения списка добавленных книг
test_get_books_rating_add_3_books

Добавление книги в избранное
test_add_book_in_favorites_add_one_book

Добавление нескольких книг в избранное
test_add_book_in_favorites_add_two_book

Нельзя добавить книгу в избранное, если нет в словаре books_rating
test_add_book_in_favorite_book_not_in_collection_error

Проверка удаления книги из избранного
test_delete_book_from_favorites_delete_one_book

Проверка удаления книги из избранного, когда добавлено 2 книги
test_delete_book_from_favorites_delete_one_of_two_books

Проверка получения списка добавленных в избранное книг
test_get_list_of_favorites_books_2_books
