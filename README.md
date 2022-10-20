#Entrega final: web django

---RODRIGO JAVIER ALONZO

---El sitio pertenece a un estudio integral: marketing, contabilidad, legales, desarrollo de software---

<<<Se crea AppBlog para administrar la información del sitio>>>


- Se crearon 4 modelos de datos:

--- "Professionals" contiene información del personal del estudio

--- "Services" contiene las categorías de servicios prestados

--- "Updatedinformation" contiene novedades publicadas por los profesionales

--- "Taxexpirationdates" contiene los vencimientos de los distintos impuestos

--- "UserAvatar" contiene la imagen de perfil del usuario

--- "AboutMeImage" contiene imagen de la sección "ACERCA DE MI"


<<< Url's: de AppBlog >>>

http://127.0.0.1:8000/AppBlog/inicio/ ---> Página principal

http://127.0.0.1:8000/AppBlog/acercademi/ ---> Sección acerca de mí

http://127.0.0.1:8000/AppBlog/nosotros/ ---> Listado de profesionales del estudio

http://127.0.0.1:8000/AppBlog/nosotros/profdetails/<int:pk> ---> Detalles de un determinado profesional seleccionado

http://127.0.0.1:8000/AppBlog/servicios/ ---> Listado de servicios prestados

http://127.0.0.1:8000/AppBlog/infoactual/ ---> Listado de novedades agregadas por los profesionales

http://127.0.0.1:8000/AppBlog/vencimientos/ ---> Listado de vencimientos fiscales

http://127.0.0.1:8000/AppBlog/formprof/ ---> Formulario de carga de datos de profesionales

http://127.0.0.1:8000/AppBlog/formserv/ ---> Formulario de carga de servicios prestados

http://127.0.0.1:8000/AppBlog/forminfo/ ---> Formulario de carga de novedades

http://127.0.0.1:8000/AppBlog/formtaxes/ ---> Formulario de carga de vencimientos fiscales

http://127.0.0.1:8000/AppBlog/searchprofessional/ ---> Formulario de consulta de profesionales por nombre

http://127.0.0.1:8000/AppBlog/searchprof/ ---> Resultado de búsqueda de profesionales

http://127.0.0.1:8000/AppBlog/deleteprof/<profname> ---> Borrar el profesional seleccionado

http://127.0.0.1:8000/AppBlog/deleteserv/<servname> ---> Borrar el servicio seleccionado

http://127.0.0.1:8000/AppBlog/deleteinfo/<infotitle> ---> Borrar la nota seleccionado

http://127.0.0.1:8000/AppBlog/deletetaxexp/<taxexpname> ---> Borrar el vencimiento seleccionado

http://127.0.0.1:8000/AppBlog/profedit/<profname> ---> Editar datos del profesional seleccionado

http://127.0.0.1:8000/AppBlog/servedit/<servname> ---> Editar datos del servicio seleccionado

http://127.0.0.1:8000/AppBlog/infoedit/<infoname> ---> Editar datos de la nota seleccionada

http://127.0.0.1:8000/AppBlog/taxexpedit/<taxexpname> ---> Editar datos del vencimiento seleccionado

http://127.0.0.1:8000/AppBlog/nosotros/profdetails/<int:pk> ---> Detalles del profesional seleccionado

http://127.0.0.1:8000/AppBlog/nosotros/deleteprofq/<int:pk> ---> Pregunta si confirma borrar el profesional seleccionado

http://127.0.0.1:8000/AppBlog/servicios/deleteservq/<int:pk> ---> Pregunta si confirma borrar el servicio seleccionado

http://127.0.0.1:8000/AppBlog/infoactual/deleteinfoq/<int:pk> ---> Pregunta si confirma borrar la nota seleccionada

http://127.0.0.1:8000/AppBlog/vencimientos/deletetaxexpq/<int:pk> ---> Pregunta si confirma borrar el vencimiento seleccionado

http://127.0.0.1:8000/AppBlog/login/ ---> Iniciar sesión con usuario y contraseña

http://127.0.0.1:8000/AppBlog/register/ ---> Registro de nuevo usuario

http://127.0.0.1:8000/AppBlog/logout/ ---> Cerrar sesión con el usuario conectado

http://127.0.0.1:8000/AppBlog/useredit/ ---> Editar usuario conectado

http://127.0.0.1:8000/AppBlog/infoactual/infodetails/<int:pk> ---> Detalles de la nota seleccionada


<<< CONTACTO ADMINISTRADOR >>>

E-mail: rodrigo.alonzo@hotmail.com

Video explicativo de la página web:

<<<<<<** VERSIÓN ACTUAL 4.2 **>>>>>>
