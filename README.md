# Backend

This repository contains the backend application built with [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python 3.8+.


## Create a Virtual Environment

It’s recommended to create a virtual environment to isolate dependencies:

```bash
python -m venv env
env\Scripts\activate  
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application in development mode:

1. Navigate to the `backend/app` directory:

   ```bash
   cd backend/app
   ```

2. Run the application using `uvicorn`:

   ```bash
   uvicorn main:app --reload
   ```

   The server will be running at `http://127.0.0.1:8000/` by default.

## API Documentation

FastAPI provides interactive API documentation using both Swagger UI and Redoc. Once the app is running, you can access the documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

#### Example structure files:
```
backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── investments.py
│   │   │   │   ├── watchlist.py
│   │   │   │   ├── prices.py
│   │   │   └── dependencies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── investment.py
│   │   ├── transaction.py
│   │   ├── watchlist.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── investment.py
│   │   ├── transaction.py
│   │   ├── watchlist.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── investment.py
│   │   ├── transaction.py
│   │   ├── watchlist.py
│   ├── database.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_investment.py
│
├── .env
├── requirements.txt
└── README.md
```

### Frontend is being developed in Dart/Flutter.

#### Example structure files:
```
lib/
│
├── core/
│   ├── error/
│   │   ├── exceptions.dart
│   │   ├── failures.dart
│   ├── network/
│   │   ├── api_client.dart
│   │   ├── network_info.dart
│   ├── util/
│   │   ├── input_converter.dart
│   │   ├── constants.dart
│   ├── theme/
│       ├── app_theme.dart
│
├── features/
│   ├── auth/
│   │   ├── domain/
│   │   │   ├── models/
│   │   │   │   ├── user_model.dart
│   │   │   ├── usecase/
│   │   │   │   ├── user_usecase.dart
│   │   ├── data/
│   │   │   ├── repositories/
│   │   │       ├── auth_repository.dart
│   │   │   ├── data_source/
│   │   │       ├── user_data_source.dart
│   │   ├── presentation/
│   │   │   ├── cubit/
│   │   │   │   ├── auth_cubit.dart
│   │   │   ├── pages/
│   │   │   │   ├── login_page.dart
│   │   │   │   ├── register_page.dart
│   │   │   ├── widgets/
│   │   │       ├── login_form.dart
│
│   ├── investment/
│   │   ├── domain/
│   │   │   ├── models/
│   │   │   │   ├── investment_model.dart
│   │   │   ├── usecase/
│   │   │   │   ├── investment_usecase.dart
│   │   ├── data/
│   │   │   ├── repositories/
│   │   │       ├── investment_repository.dart
│   │   │   ├── data_source/
│   │   │       ├── investment_remote_data_source.dart
│   │   │       ├── investment_local_data_source.dart
│   │   ├── presentation/
│   │   │   ├── cubit/
│   │   │   │   ├── investment_cubit.dart
│   │   │   ├── pages/
│   │   │   │   ├── investments_page.dart
│   │   │   │   ├── investment_detail_page.dart
│   │   │   ├── widgets/
│   │   │       ├── investment_card.dart
│
│   ├── watchlist/
│   │   ├── domain/
│   │   │   ├── models/
│   │   │   │   ├── watchlist_model.dart
│   │   │   ├── usecase/
│   │   │   │   ├── watchlist_usecase.dart
│   │   ├── data/
│   │   │   ├── repositories/
│   │   │       ├── watchlist_repository.dart
│   │   │   ├── data_source/
│   │   │       ├── watchlist_remote_data_source.dart
│   │   │       ├── watchlist_local_data_source.dart
│   │   ├── presentation/
│   │   │   ├── cubit/
│   │   │   │   ├── watchlist_cubit.dart
│   │   │   ├── pages/
│   │   │   │   ├── watchlist_page.dart
│   │   │   ├── widgets/
│   │   │       ├── watchlist_item.dart
│
├── app.dart
├── main.dart
└── routes.dart
```
[Inspiration](https://chatgpt.com/share/66e885c3-27a0-8005-9d90-84dc21ff4572)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
