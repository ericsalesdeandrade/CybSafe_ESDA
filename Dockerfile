FROM python:3.8.5
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
COPY src ./code/src/
COPY src/helpers/ ./code/src/helpers/
CMD [ "pytest", "./tests/test_unit_get_pokemon.py" ]