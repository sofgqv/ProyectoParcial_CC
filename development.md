
# CORRER BASE DE DATOS

## EN CMD:
ssh -i ./.ssh/labsuser.pem ubuntu@54.204.79.149

docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0

docker run -d --rm --name adminer_c -p 8080:8080 adminer

## ENTRAR A adminer
http://54.204.79.149:8080/

# EN AMBIENTE DE DESARROLLO

### API 2
cd ubuntu/proyectoparcial/api-voluntario
docker build -t api-voluntario .

docker login -u sofiagarcia 
docker tag api-voluntario sofiagarcia/api-voluntario
docker push sofiagarcia/api-voluntario
docker logout

docker run -d --rm --name api-voluntario_c -p 8001:8001 api-voluntario

### API 2
cd ubuntu/proyectoparcial/api-donar
docker build -t api-donar .

docker login -u sofiagarcia 
docker tag api-donar sofiagarcia/api-donar
docker push sofiagarcia/api-donar
docker logout

docker run -d --rm --name api-donar_c -p 8002:8002 api-donar

### API 3
cd ubuntu/proyectoparcial/api-adoptar

docker build -t api-adoptar .

docker login -u valdlaw 
docker tag api-adoptar valdlaw/api-adoptar
docker push valdlaw/api-adoptar
docker logout

docker run -d --rm --name api-adoptar_c -p 8003:8003 api-adoptar

## Testing Postman

<IP del ambiente de desarrollo>:8001/servoluntarios
<IP del ambiente de desarrollo>:8001/voluntario/id

<IP del ambiente de desarrollo>:8002/-
<IP del ambiente de desarrollo>:8002/-

<IP del ambiente de desarrollo>:8003/adoptar
<IP del ambiente de desarrollo>:8003/mascota/id

# Correr en ambientes de producción

docker run -d --rm --name api-voluntario_c -p 8001:8001 sofiagarcia/api-voluntario

docker run -d --rm --name api-donar_c -p 8002:8002 sofiagarcia/api-donar

docker run -d --rm --name api-adoptar_c -p 8003:8003 valdlaw/api-adoptar
