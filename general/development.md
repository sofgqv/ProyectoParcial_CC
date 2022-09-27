
# CORRER BASE DE DATOS

## EN CMD:
ssh -i ./.ssh/labsuser.pem ubuntu@3.230.38.83

docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0

docker run -d --rm --name adminer_c -p 8080:8080 adminer

## Entrar a adminer
http://3.230.38.83:8080/
# EN AMBIENTE DE DESARROLLO

docker login -u valdlaw

## API 1
cd proyectoparcial/api-voluntario

docker build -t api-voluntario .

docker tag api-voluntario valdlaw/api-voluntario

docker push valdlaw/api-voluntario

docker run -d --rm --name api-voluntario_c -p 8001:8001 api-voluntario

## API 2

cd proyectoparcial/api-donar

docker build -t api-donar .

docker tag api-donar valdlaw/api-donar

docker push valdlaw/api-donar

docker run -d --rm --name api-donar_c -p 8002:8002 api-donar}

## API 3

cd proyectoparcial/api-adoptar

docker build -t api-adoptar .

docker tag api-adoptar valdlaw/api-adoptar

docker push valdlaw/api-adoptar

docker run -d --rm --name api-adoptar_c -p 8003:8003 api-adopta


## API 4
cd proyectoparcial/api-admin

docker build -t api-admin .

docker login -u sofiagarcia 

docker tag api-admin sofiagarcia/api-admin

docker push sofiagarcia/api-admin

docker run -d --rm --name api-admin_c -p 8004:8004 api-admin


docker logout

## Testing Postman (colocar el ID, luego lo de abajo)

:8001/servoluntarios

:8001/voluntario/id


:8002/donar

:8002/donaciones


:8003/adoptarestado/a_id

:8003/adoptar

:8003/mascota/id

:8003/mascotas

:8003/mascotasadd

:8004/admin

# Correr en ambientes de producción

docker run -d --rm --name api-voluntario_c -p 8001:8001 sofiagarcia/api-voluntario

docker run -d --rm --name api-donar_c -p 8002:8002 sofiagarcia/api-donar

docker run -d --rm --name api-adoptar_c -p 8003:8003 valdlaw/api-adoptar

docker run -d --rm --name api-admin_c -p 8004:8004 sofiagarcia/api-admin

# Balanceador de carga

lb-prod-632583897.us-east-1.elb.amazonaws.com:8001/servoluntarios

lb-prod-632583897.us-east-1.elb.amazonaws.com:8001/voluntario/id


lb-prod-632583897.us-east-1.elb.amazonaws.com:8002/donar

lb-prod-632583897.us-east-1.elb.amazonaws.com:8002/donaciones


lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/adoptarestado/a_id

lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/adoptar

lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/mascota/id

lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/mascotas

lb-prod-632583897.us-east-1.elb.amazonaws.com:8003/mascotasadd


lb-prod-632583897.us-east-1.elb.amazonaws.com:8004/admin