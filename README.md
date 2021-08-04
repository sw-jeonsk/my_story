# My Story

---

## 나의 스토리를 기록하고 싶다.

-   python version : 3.8.10
-   conda activate my-story
-   docker build -t my-story:0.1 .
-   docker-compose up --build -d

-   superuser create
    -   python app/manage.py createsuperuser
-   DB migration file create
    -   python app/manage.py makemigrations
-   DB migrate
    -   python app/manage.py migrate
