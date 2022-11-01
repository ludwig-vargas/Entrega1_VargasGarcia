# Entrega1_VargasGarcia
Proyecto inventario entrega 1

1. Generar el archivo venv e instalar Django en la misma.
.\venv\Scripts\activate
pip install django

2. Generamos las migraciones para crear la base de datos en cd my_inventory
python manage.py migrate

3. Nos dirigimos al navegarod y escribimos localhost:800

4. En el index seleccionamos cualquiera de las tres etiquetas que son Productos, Clientes o Empleados
-En este caso sera en Productos
-Lo redireccionara a product_list.html que su direccion en el proyecto es la siguiente:
Entrega1-Vargas\my_inventory\product\templates\product\product_list.html

5. Seleccionamos el boton para crear un nuevo elemento
-Lo redireccionara a product_form.html donde aparecera el formulario dependiendo del archivo forms.py
Entrega1-Vargas\my_inventory\product\templates\product\product_form.html
-La creacion del nuevo elemento se da en la carpeta de views.py
Entrega1-Vargas\my_inventory\product\views.py
-En el archivo de urls.py se mustran las urls de la lista como del formulario para crear un nuevo elemento
\Entrega1-Vargas\my_inventory\product\urls.py

6. Cuando se seleccione en guardar volvera a la pantalla de product_list.html
-Aparecera el nuevo elemento
-En esta pantalla esta un ciclo que muestra el resultado de todos los elementos creados

7. Para realizar la busqueda en index solo se tendra que poner el nombre o el codigo y aparecera en seguida
-Esta funcionalidad se da en el archivo views.py de home
\Entrega1-Vargas\my_inventory\home\views.py
-Al igual que en index.html para mostrar el resultado
-La busqueda funciona para los tres modelos

# Extras
-En los tres modelos el code es un primary key que esta limitado a 3 numeros
-En los archivos de forms.py de los tres bienen limitados como minimo 3 y maximo 3 numeros
-Realiza busquedas de los tres modelos
-En existencia para crear un nuevo producto es un numero que indica cuantos de ese produto existen en el inventario

