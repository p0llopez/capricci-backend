[Production](https://capricci-backend.onrender.com/api/docs)

# Capricci Backend

It's a python project that uses Django and django-ninja to create a REST API.

## 🚀 Table of Contents

- [Commands](#-commands)
- [Improvements](#-improvements)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                       | Action                                           |
|:------------------------------| :----------------------------------------------- |
| `poetry install`              | Install dependencies                             |
| `python manage.py migrate`    | Apply migrations to the database |
| `python manage.py runserver`  | Run the development server |
| `python manage.py test tests` | Run the tests |
| `pre-commit run --all-files`  | Run pre-commit checks |



## 📝 Improvements

Here are some improvements that can be made:

- [ ] **Cursor Pagination**: Use cursor pagination instead of offset pagination.
- [x] **JWT**: Implement JWT for authentication.
- [ ] **Improve Pipelines GitHub Actions**: Use github actions to autodeploy, build, lint, tests, etc.
- [ ] **Improve Tests**: Add more tests to improve coverage, and improve the quality of the tests (fixtures, factories, etc.).
- [ ] **Improve Endpoint responses**: Add more information to the responses, like the total number of items, etc.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

## 📄 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Ninja](https://django-ninja.dev/)
- [Django Ninja Extra](https://eadwincode.github.io/django-ninja-extra/)
- [Django Ninja JWT](https://eadwincode.github.io/django-ninja-jwt/getting_started/)

[⬆ Back to Top](#-capricci-backend)

[//]: # (Links)
