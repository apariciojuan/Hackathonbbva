# Hackathon BBVA

### APIs

* Creamos un usuario nuevo.

Recive:

POST: 

   > 'nombre' type Char   
   > 'apellido' type Char   
   > 'dni' type Char    
   > 'photo' type bytes    


api/v1/usuario/




* Operaciones sobre usuario.

Recive:

GET, UPDATE, REMOVE

UPDATE 

   > 'nombre' type Char    
   > 'apellido' type Char   
   > 'dni' type Char  

   > {identificador} es el numero personal identificatorio del cliente

api/v1/usuario/{identificador}/



* cheque biometrico

Recive:

POST: 

> 'image' type bytes  
> 'numero_usuario'type Char  

Return:

> {"result": 'ok'} or {"result": 'ko'}


api/v1/chequeo/facial/


## se complementa con una mini app que esta en este [repo](https://github.com/apariciojuan/Biolock---Hackathon-BBVA-2020-Fronted) 


### License

This project uses [MIT license.](https://github.com/apariciojuan/Hackathonbbva/blob/main/LICENSE)
