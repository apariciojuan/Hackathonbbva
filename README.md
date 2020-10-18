# Hackathon BBVA

Podemos probarlo aqui:   
https://panaceatelc.com/

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




### License

This project uses [MIT license.](https://github.com/apariciojuan/Hackathonbbva/blob/main/LICENSE)
