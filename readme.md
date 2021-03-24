NOTA: Para esta versión del proyecto se utilizó la versión 3.8 de Python.

1. Clonar este repositorio en el directorio de proyectos:
```
git clone https://github.com/HiramHernandez/inventory.git
```
2. Crear el entorno virtual para aislar las depencias del proyecto:

```
virtualenv RUTA_DEL_ENTORNO_VIRTUAL/NOMBRE_ENTORNO
```


2.1 Para ejecutar el entorno virtual es necesario ejecutar el archivo **activate.bat** que se encuentra en:

en Windows:

	```
	RUTA_DEL_ENTORNO_VIRTUAL/Scripts/activate.bat
	```

en linux:

	```
	RUTA_DEL_ENTORNO_VIRTUAL/bin/activate
	```

3. Instalar las dependencias en raíz del proyecto:

	```
	pip install -r requirements.txt
	```

### Configuración
Crear archivo settings.json, en raiz del proyecto.


	```json
	{ 	"DEBUG": "",
		"SQLALCHEMY_TRACK_MODIFICATIONS": "",
		"SQLALCHEMY_DATABASE_URI": "" 
	}
	```
