# My Story

### 나의 스토리를 기록하고 싶다. 나의 일기, 나의 스케쥴 등 관리하고 싶다.

-   python version : 3.8.10
-   conda activate my_story
-   docker build -t my_story:0.1 .
-   docker-compose up --build -d

-   superuser create
    -   python my_story/manage.py createsuperuser
-   DB migration file create
    -   python my_story/manage.py makemigrations
-   DB migrate
    -   python my_story/manage.py migrate
