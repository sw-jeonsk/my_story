# My Story

### Link

-   [Document Blog](https://swenginejsk.notion.site/My-Story-Backend-4203a6a7211243d28db5ef4285806b52)

---

### Purpose

-   나의 스토리를 기록하고 싶다. 나의 일기, 나의 스케쥴 등 관리하고 싶다.

---

### Environment

-   Backend Framework : Django==3.2.4
-   python version : 3.8.10
-   conda activate my_story
-   docker build -t my_story:0.1 .
-   docker-compose up --build -d

---

### Install & Run

-   superuser create
    -   python my_story/manage.py createsuperuser
-   DB migration file create
    -   python my_story/manage.py makemigrations
-   DB migrate
    -   python my_story/manage.py migrate
