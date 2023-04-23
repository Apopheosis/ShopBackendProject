FROM python:3.9.0-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN pip install asyncpg && pip install psycopg2-binary && pip install pydantic[email] && pip install python-multipart && pip install sqlalchemy_utils
RUN pip install alembic && pip install uvicorn
COPY pg_init_scripts/init.sql/ /docker-entrypoint-initdb.d/

RUN rm -rf migrations
RUN alembic init migrations
COPY migrations/env.py migrations/env.py

EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]

