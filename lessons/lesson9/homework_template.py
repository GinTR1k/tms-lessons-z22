class Authenticator:
    def __init__(self):
        self.login: str | None = None  # или self.login: Optional[str] = None
        # Дальше создать переменные
        ...

        ...  # Читаем из файла и перезаписываем переменные

    def _is_auth_file_exist(self) -> bool:
        """Что делает метод? Зачем?"""
        is_file_exist = ...  # проверить файл, что он существует - гугл

        if is_file_exist:
            return True

        return False

    def _read_auth_file(self):
        """Что делает метод? Зачем?"""
        with ... as f:
            self.login = f.readline()
            # дальше обновить переменные
            ...

    def _update_auth_file(self):
        """Что делает метод? Зачем?"""
        with ... as f:
            f.write(self.login)
            # дальше записать в файл переменные
            ...

    def registrate(self):
        """Что делает метод? Зачем?"""
        if ...:  # Как можно сделать проверку, что файла не существует, не вызывая ни одного метода здесь?
            ...  # Обновить счетчик неудачных попыток
            raise ...  # Файл существует

        ...  # Сохранить данные в файл

    def authorize(self):
        """Что делает метод? Зачем?"""
        if ...:  # Как можно сделать проверку, что файла не существует, не вызывая ни одного метода здесь?
            ...  # Обновить счетчик неудачных попыток
            raise ...  # Файла не существует

        ...  # Обнулить счетчик неудачных попыток
        ...  # Сохранить данные в файл
