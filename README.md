# Hackathonbbva


APIs

* Creamos un usuario nuevo.

Recive:

POST: 
    'nombre' type Char, 
    'apellido' type Char, 
    'dni' type Char,
    'photo' type image


api/v1/usuario/




* Operaciones sobre usuario.

Recive:

GET, UPDATE, REMOVE

UPDATE 
    'nombre' type Char,  
    'apellido' type Char, 
    'dni' type Char



api/v1/usuario/{identificador}/



* cheque biometrico

Recive:

POST: 
    'image' type image,
    'numero_usuario'type Char


api/v1/chequeo/facial/




## License

This project uses MIT license.