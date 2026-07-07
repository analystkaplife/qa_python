# qa_python
# Тесты для BooksCollector

## Список тест-кейсов

### 1. Добавление книг (`add_new_book`)
- (test_add_new_book_add_two_books) Добавление двух книг — размер словаря увеличивается на 2
- (test_add_new_book_valid_name) Добавление книги с валидным названием (обычное, 40 символов)
- (test_add_new_book_invalid_name) Добавление книги с невалидным названием (пустое, >40 символов)
- (test_add_new_book_duplicate) Добавление дубликата книги — новая запись не создаётся

### 2. Установка и получение жанра (`set_book_genre` / `get_book_genre`)
- (test_set_book_genre_valid_genre) Установка валидного жанра (Фантастика, Ужасы, Детективы, Мультфильмы, Комедии)
- (test_set_book_genre_invalid_genre) Установка невалидного жанра — игнорируется
- (test_set_book_genre_nonexistent_book) Установка жанра для несуществующей книги — игнорируется

### 3. Поиск книг по жанру (`get_books_with_specific_genre`)
- (test_get_books_with_specific_genre) Поиск книг с жанром Фантастика, Ужасы, Детективы
- (test_get_books_with_specific_genre_invalid_genre) Поиск книг с несуществующим жанром — возвращается пустой список

### 4. Получение списка книг для детей (`get_books_for_children`)
- (test_get_books_for_children) Книги жанров Фантастика, Мультфильмы, Комедии попадают в детский список; Ужасы и Детективы — НЕ попадают
- (test_get_books_for_children_with_no_genre) Книги без жанра НЕ попадают в детский список

### 5. Добавление в избранное (`add_book_in_favorites`)
- (test_add_book_in_favorites_valid_book) Добавление существующей книги в избранное
- (test_add_book_in_favorites_duplicate) Добавление дубликата в избранное — игнорируется
- (test_add_book_in_favorites_nonexistent_book) Добавление несуществующей книги — игнорируется

### 6. Удаление из избранного (`delete_book_from_favorites`)
- (test_delete_book_from_favorites_valid_book) Удаление книги из избранного
- (test_delete_book_from_favorites_nonexistent_book) Попытка удалить несуществующую книгу — без ошибки

### 7. Получение всех книг (`get_books_genre`)
- (test_get_books_genre) Получение словаря всех книг с жанрами

### 8. Получение списка избранного (`get_list_of_favorites_books`)
- (test_get_list_of_favorites_books_empty) Получение пустого списка избранного
- (test_get_list_of_favorites_books_with_books) Получение списка избранного с книгами




---

**Итого:** 23 тест-кейса (с учётом параметризации)  
**Покрытие методов:** 100%  
**Фреймворк:** pytest