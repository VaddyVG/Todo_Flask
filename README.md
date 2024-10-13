# Todo Flask App

Простое приложение на Flask и SQLAlchemy

## Возможности

- Добавление задачи в спсиок дел
- Отметить задачу, как выполненную ('Complete') или невыполненную ('Incomplete')
- Удаление задачи из списка

## Установка

1. Клонируйте репозиторий
```bash
git clone https://github.com/VaddyVG/Todo_Flask.git
```

2. Перейдите в репозиторий
```bash
cd Todo_Flask
```

3. Установите и активируйте виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Установите Flask и SQLAlchemy
```bash
pip install Flask
pip install Flask-SQLAlchemy
```

5. Установите переменные в терминале
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

6. Запустите приложение
```bash
flask run
```
