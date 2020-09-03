# Read Me
## Requirements

- Python 3.8 >
- pip 
- docker 
- docker-compose
- cat (for Data Setup Option #1)

## Getting Started

Be sure to set up a virtual environment for your installed packages. If you need to add packages to your product, be sure to add them to the requirements.txt so it can be reproduced:
    
    pip install package && pip freeze > requirements.txt

#### Flask Setup:

    pip install -r requirements.txt
    python run.py
    
Flask micro-app will start on [http://localhost:5000](http://localhost:5000)

#### Docker Setup:

    docker-compose up -d 
    
#### Data Setup

    cat init.sql | docker exec -i <postgres_container_id> bash -c 'psql -U postgres'

#### Data Setup alternative
Connect to Postgres DB with [DBeaver](https://dbeaver.io/download/) (or equivalent Database IDE). 
Default Settings are:
     
    username: postgres
    password: password
    database: postgres
    
Run the contents of the init.sql file in the project. 

#### Nominatim

Nominatim docker-app will start on [http://localhost:5003](http://localhost:5003)

Readme of API options can be found here: [Nominatim API](https://nominatim.org/release-docs/latest/api/Search/)

## Recommended other Technical Assignments

- Docker
- SQL

## Technologies Used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) - Flask Micro-Framework
- [Docker](https://www.docker.com) - Docker Virtualization
- [Nominatim](https://wiki.openstreetmap.org/wiki/Nominatim) - Nominatim Geo-Coding and Reverse Geo-Coding
- [Swagger/ OpenAPI](https://swagger.io/specification/) - OpenAPI API documentation 
