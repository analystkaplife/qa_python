import pytest
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

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    # -------------------- Тесты для add_new_book --------------------
    @pytest.mark.parametrize("name", [
        "Война и мир",
        "А" * 40,
        "Книга с очень длинным названием, но ровно 40 символов"  # 40 символов
    ])
    def test_add_new_book_valid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre
        assert collector.books_genre[name] == ""

    @pytest.mark.parametrize("name", [
        "",
        "А" * 41,
        "   "  # пустая строка с пробелами
    ])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_new_book("Дюна")
        assert len(collector.books_genre) == 1

    # -------------------- Тесты для set_book_genre и get_book_genre --------------------
    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_book_genre("Книга") == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Роман")
        assert collector.get_book_genre("Книга") == ""

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Существующая книга")
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in collector.books_genre

    # -------------------- Тесты для get_books_with_specific_genre --------------------
    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Книга 1", "Книга 2"]),
        ("Ужасы", ["Книга 3"]),
        ("Детективы", []),
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_new_book("Книга 3")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Фантастика")
        collector.set_book_genre("Книга 3", "Ужасы")
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        result = collector.get_books_with_specific_genre("Роман")
        assert result == []

    # -------------------- Тесты для get_books_for_children --------------------
    @pytest.mark.parametrize("genre, expected_in_children_list", [
        ("Фантастика", True),
        ("Мультфильмы", True),
        ("Комедии", True),
        ("Ужасы", False),
        ("Детективы", False),
    ])
    def test_get_books_for_children(self, genre, expected_in_children_list):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        children_books = collector.get_books_for_children()
        if expected_in_children_list:
            assert "Книга" in children_books
        else:
            assert "Книга" not in children_books

    def test_get_books_for_children_with_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")
        children_books = collector.get_books_for_children()
        assert "Книга без жанра" not in children_books

    # -------------------- Тесты для add_book_in_favorites --------------------
    def test_add_book_in_favorites_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.favorites

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.favorites.count("Книга") == 1

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Существующая книга")
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.favorites

    # -------------------- Тесты для delete_book_from_favorites --------------------
    def test_delete_book_from_favorites_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.favorites

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Несуществующая книга")
        assert "Книга" in collector.favorites

    # -------------------- Тесты для get_books_genre --------------------
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        result = collector.get_books_genre()
        assert result == collector.books_genre
        assert len(result) == 2

    # -------------------- Тесты для get_list_of_favorites_books --------------------
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Книга 1", "Книга 2"]

    # -------------------- Комплексные тесты --------------------
    def test_full_scenario_add_and_favorite(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        collector.add_book_in_favorites("1984")
        assert collector.get_book_genre("1984") == "Фантастика"
        assert "1984" in collector.favorites
        assert collector.get_books_for_children() == ["1984"]

    def test_full_scenario_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_book_genre("Оно") == "Ужасы"
        assert collector.get_books_for_children() == []
        collector.add_book_in_favorites("Оно")
        assert "Оно" in collector.favorites