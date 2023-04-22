FROM python:3.8-slim-buster

# WORKDIR /src


COPY basic_viewer/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY network_glance network_glance
COPY basic_viewer basic_viewer
COPY pyproject.toml pyproject.toml
COPY README.md README.md
# COPY . .

RUN pip3 install --upgrade build
RUN pip3 install .

CMD ["python3", "basic_viewer/api.py"]
