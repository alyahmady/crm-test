Notes:

- Emails will be redirected to `./logs/email` directory
- To monitor celery, you can use `flower` service, which is running on port `5566`
- As I started late (I'm really sorry for it) and I didn't have enough time,
I decided to not style the templates with CSS and Bootstrap, and just use plain HTML.

---

TODO for Production:

1- In the case of implementing CI/CD, may we need to ignore migration files from being tracked in git.

2- We may need to separate Celery instances from `backend` Docker Compose service.

3- Add certbot Docker Compose service and a crontab on Server OS to generate/renew SSL certificates.
If so, we need to reconfigure Nginx config files (templates) in `./deploy/config/nginx/templates`.
(https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx)


---

# CRM test project

This project is for Car Rental system, which is a test project for `dorost.nl`.

Make sure that you have **Docker and Docker Compose** installed, before you build the project with Docker.
[Download](https://docs.docker.com/compose/install/)

----

## Configurations

You need to check and set configurations of the project, for Docker deployments and builds.

* First, make a copy of the example configurations:

    **Windows**
    ```bash
    copy .\deploy\environments\backend.env.example .\deploy\environments\backend.env
    ```

    **Linux**
    ```bash
    cp ./deploy/environments/backend.env.example ./deploy/environments/backend.env
    ```

* Take a look at the file in this address, with a text editor and change as you wish

    **Windows**
    ```bash
    notepad.exe .\deploy\environments\backend.env
    ```

    **Linux**
    ```bash
    nano ./deploy/environments/backend.env
    ```

  * **It's better the re-set all password fields for more security.** If you did so, please take a look at other `env` files within `environments` directory, to set passwords of other related services, as well. **Please consider that username, password, and port configs of Redis and Postgres must be synced within all of these three files:**
    * `backend.env`
    * `redis.env`
    * `postgres.env`


* In Admin page of your project, after building with Docker, you can start with the email and password that you set for `DJANGO_SUPERUSER_EMAIL` and `DJANGO_SUPERUSER_PASS` environment variables, within `.env` file.
* This SuperUser is authorized for admin panel.
* If you want to authorize this SuperUser for all APIs and MVC pages, please change value of `HAS_SUPERUSER_GOD_MODE` to `true`.

----


## Automatic Build (Docker)

**Production**
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

**Local**
```bash
docker-compose -f docker-compose.local.yml up -d --build
```

**You project now is running on your _localhost_ on _80_ port.**

Pages

  * Home -> [localhost:80](localhost:80)
  * Admin Panel (SuperUser) -> [localhost:80/admin/](http://localhost:80/admin/)
  * Car List -> [localhost:80/car/list/](http://localhost:80/car/list/)
  * Rental List (Admin or Staff only) -> [localhost:80/rental/list/](http://localhost:80/rental/list/)
  * Rental Create (Staff only) -> [localhost:80/rental/create/](http://localhost:80/rental/create/)
  * Login -> [localhost:80/user/login/](http://localhost:80/user/login/)
  * SignUp -> [localhost:80/user/signup/](http://localhost:80/user/signup/)

APIs

  * Swagger -> [localhost:80/api/v1/schema/swagger-ui/](http://localhost:80/api/v1/schema/swagger-ui/)

  * Login (POST) -> [localhost:80/api/v1/user/token/](http://localhost:80/api/v1/user/token/)
  * Refresh Token (POST) -> [localhost:80/api/v1/user/token/refresh/](http://localhost:80/api/v1/user/token/refresh/)

  * Car Create (POST) -> [localhost:80/api/v1/car/](http://localhost:80/api/v1/car/)
  * Car List (GET) -> [localhost:80/api/v1/car/](http://localhost:80/api/v1/car/)
  * Car Update (PUT) -> [localhost:80/api/v1/car/<car_id>](http://localhost:80/api/v1/car/<car_id>)
  * Car Partial Update (PATCH) -> [localhost:80/api/v1/car/<car_id>](http://localhost:80/api/v1/car/<car_id>)
  * Car Retrieve (GET) -> [localhost:80/api/v1/car/<car_id>](http://localhost:80/api/v1/car/<car_id>)
  * Car Delete (DELETE) -> [localhost:80/api/v1/car/<car_id>](http://localhost:80/api/v1/car/<car_id>)

-----

## Local build (without Docker)

1- Please check you have **Python 3**, **PostgreSQL** and **Redis** installed.
 * [Python](https://www.python.org/downloads/)
 * [PostgresSQL](https://www.postgresql.org/download/)
 * [Redis](https://redis.io/docs/getting-started/installation/)


2- Then you need a virtual environment for the project, and have it activated.

**Windows**
```bash
cd <PROJECT_DIR>
python -m venv .venv
.venv\Scripts\activate
```

**Linux**
```bash
cd <PROJECT_DIR>
python3 -m venv .venv
source .venv/bin/activate
```

3- After that you should install project dependencies.

```bash
pip install requirements/local.txt
```

4- Then you need to check and set configurations of the project. Instructions are at the bottom of the page.

  * You need to create your database and user on your local PostgreSQL server, before you set configurations with `POSTGRES_` prefix. To do so, you can run these queries on your PostgreSQL.

      ```bash
      CREATE DATABASE <POSTGRES_DB>;
      CREATE USER <POSTGRES_USER> WITH PASSWORD '<POSTGRES_PASSWORD>';
      ALTER ROLE <POSTGRES_USER> SET client_encoding TO 'utf8';
      ALTER ROLE <POSTGRES_USER> SET default_transaction_isolation TO 'read committed';
      ALTER ROLE <POSTGRES_USER> SET timezone TO 'UTC';
      GRANT ALL PRIVILEGES ON DATABASE <POSTGRES_DB> TO <POSTGRES_USER>;
      ```

5- To call APIs or test project, you need to have `celery` process, running on your system

**Windows**
```bash
celery -A crmtest.celery worker --loglevel=debug --pool=solo
celery -A crmtest.celery beat --loglevel=debug
```

**Linux**
```bash
celery -A crmtest.celery worker --loglevel=debug
celery -A crmtest.celery beat --loglevel=debug
```

6- Before finishing the build process, if you want to make sure of test cases, you can run this command.

```bash
python manage.py test
```

* Please consider that, You may have failures experience in tests, for Celery async tasks, on Windows. To make sure of test cases, it's better to run `test` command on a linux instance.

7- To initialize Database and static files, run these commands:

```bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata user_app/user_groups.json
python manage.py initialize
```

  * For not experiencing pages without static files (through local deployment mode only), you need to set `DEBUG` config as `True` within `crmtest/settings/base.py` explicitly.

8- Run this commands, to start the project development server:

**Linux**
```bash
python manage.py runserver 0.0.0.0:8000
```

* If you want to run project on a more secure and stable server, instead of `runserver` command, follow as below:

```bash
gunicorn --workers=10 --bind=0.0.0.0:8000 crmtest.asgi:application -k uvicorn.workers.UvicornWorker --timeout 1000
```

* You can provide an absolute path of `./deploy/config/gunicorn_config.py` file, to `--config` argument of `gunicorn` command, to use a custom configuration file.

```bash
gunicon --config /home/aly/crmtest/deploy/config/gunicorn.conf.py crmtest.asgi:application
```

**You project now is running on your _localhost_ on _8000_ port.**

Pages

  * Home -> [localhost:8000](localhost:8000)
  * Admin Panel (SuperUser) -> [localhost:8000/admin/](http://localhost:8000/admin/)
  * Car List -> [localhost:8000/car/list/](http://localhost:8000/car/list/)
  * Rental List (Admin or Staff only) -> [localhost:8000/rental/list/](http://localhost:8000/rental/list/)
  * Rental Create (Staff only) -> [localhost:8000/rental/create/](http://localhost:8000/rental/create/)
  * Login -> [localhost:8000/user/login/](http://localhost:8000/user/login/)
  * SignUp -> [localhost:8000/user/signup/](http://localhost:8000/user/signup/)

APIs

  * Swagger -> [localhost:8000/api/v1/schema/swagger-ui/](http://localhost:8000/api/v1/schema/swagger-ui/)

  * Login (POST) -> [localhost:8000/api/v1/user/token/](http://localhost:8000/api/v1/user/token/)
  * Refresh Token (POST) -> [localhost:8000/api/v1/user/token/refresh/](http://localhost:8000/api/v1/user/token/refresh/)

  * Car Create (POST) -> [localhost:8000/api/v1/car/](http://localhost:8000/api/v1/car/)
  * Car List (GET) -> [localhost:8000/api/v1/car/](http://localhost:8000/api/v1/car/)
  * Car Update (PUT) -> [localhost:8000/api/v1/car/<car_id>](http://localhost:8000/api/v1/car/<car_id>)
  * Car Partial Update (PATCH) -> [localhost:8000/api/v1/car/<car_id>](http://localhost:8000/api/v1/car/<car_id>)
  * Car Retrieve (GET) -> [localhost:8000/api/v1/car/<car_id>](http://localhost:8000/api/v1/car/<car_id>)
  * Car Delete (DELETE) -> [localhost:8000/api/v1/car/<car_id>](http://localhost:8000/api/v1/car/<car_id>)
