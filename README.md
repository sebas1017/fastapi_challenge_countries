# API-REST COUNTRIES
![alt text](https://github.com/sebas1017/fastapi_tangelo_challenge/blob/main/images_demo/docker.jpeg?raw=true)

![alt text](https://github.com/sebas1017/fastapi_tangelo_challenge/blob/main/images_demo/postgresql.jpeg?raw=true)


![alt text](https://github.com/sebas1017/fastapi_tangelo_challenge/blob/main/images_demo/heroku.png?raw=true)

![alt text](https://github.com/sebas1017/fastapi_tangelo_challenge/blob/main/images_demo/fastapi.png?raw=true)



url aplicacion :  https://fastapi-api-challenge-tangelo.herokuapp.com/
Este servidor responde a solicitudes tipo GET de acuerdo a las especificaciones solo tenemos un endpoint el cual a su vez consume una API REST externa para
la extraccion  y clasifcacion de datos asociados a paises , de acuerdo a esto para poder ejecutar el proyecto debemos hacer lo siguiente
# INSTALACION [HEROKU-SERVIDOR][CON DOCKER]
debe tener una cuenta creada en heroku y descargar el cliente de heroku luego:
    heroku login
    heroku container:login
    heroku create fastapi-api-challenge-tangelo  #o el nombre que desee
    heroku container:push web -a  fastapi-api-challenge-tangelo
    heroku container:release web -a  fastapi-api-challenge-tangelo  #esto despliega




# INSTALACION [LINUX][CON DOCKER][LOCALMENTE]
1: tener instalado docker

clonar el proyecto y en la carpeta al nivel del Dockerfile ejecutar el siguiente comando
> docker build -t fastapi-api-challenge-tangelo .

el punto indica que creara una imagen de docker apartir del Dockerfile que se encuentra
en la ruta actual donde ejecuta el comando , una vez realizado esto la imagen estara creada
y podra crear un contenedor de la api con el siguiente comando

> docker run -p 8000:8000 fastapi-api-challenge-tangelo

este comando ejecutara un container de la api , expuesto en el puerto 8000 de la maquina propia
y por lo tanto ya podra dirigirse a la ruta http://localhost:8000 y al invocar este url en la raiz debe esperar a que cargue la api y podra ver los resultados del procesamiento de datos y si entra al contenedor podra ver que en los archivos , se creo automaticamente data.json y la base de datos postgresql siempre esta en funcionamiento en heroku, si desea conectarse a ella
revisar el archivo .env donde se encuentran las credenciales


# INSTALACION [LINUX][SIN DOCKER][LOCALMENTE]
requisitos:
1: tener instalado python 3
2: tener instalada la libreria para creacion de entornos virtuales en python3 en caso de no tenerla ejecutar sudo apt-get install python3-venv
clonar el proyecto en su repositorio local y desplazarse hasta ese directorio , posteriormente crear un entorno virtual para instalar las dependencias 

> python3 -m venv venv

luego debera activar el entorno virtual anteriormente creado

> . venv/bin/activate  o bien usando el comando   source venv/bin/activate


una vez activado el entorno virtual debera instalar las dependencias por lo que en la raiz del proyecto ejecutar el siguiente comando

> pip install -r requirements.txt o bien  el comando   pip3 install -r requirements.txt


una vez instaladas las dependencias correr el script main.py  

> python main.py  or python3 main.py

una vez ejecutado podra ir al url  http://127.0.0.1:8000/      y obtendra la respuesta en formato JSON de acuerdo a las especificaciones


al hacer la solicitud de tipo GET en este endpoint , en su directorio local se generara un archivo data.json que tendra la informacion vista desde el navegador
pero en un archivo JSON

si desea tambien puede realizar la solicitud GET desde la linea de comandos 
> curl http://127.0.0.1:8000/


# TESTS [LINUX][SIN DOCKER][LOCALMENTE]

una vez instalada las dependencias y el entorno virtual si realizo la instalacion
sin docker ejecutar en la raiz del proyecto el siguiente comando

> coverage run -m pytest tests


# TESTS [LINUX][CON DOCKER][LOCALMENTE]

si tiene el container corriendo (si siguio la guia para instalarlo localmente con docker)
entonces podra entrar al contenedor con el siguiente comando

para ver los containers activos corriendo
> docker ps 

de este resultado tome el id del container y ejecute 
> docker exec -ti id_container bash

una vez aqui podra ejecutar el comando de tests 

> coverage run -m pytest tests
