This is application demo for

1) Flask
2) FastAPI
3) SQLAlchemy
4) PWA

FastAPI will be served as the main entrance for the application and URL as below:

http://127.0.0.1:8000/api/
http://127.0.0.1:8000/web/

http://127.0.0.1:8000/ will redirect to http://127.0.0.1:8000/web/

Run this demo using Uvicorn

uvicorn main:app --reload