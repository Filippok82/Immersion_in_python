class UserException(Exception):
    pass


class UserValueError(UserException):
    def __str__(self):
        return f'Радиус не должен быть нулем или меньше нуля '


class FileNotFoundError(UserException):

    def __str__(self):
        return f'Файла с таким именем студента не существует '
