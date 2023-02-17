<!-- Bienvenido al convertidor de imagenes PNG, JPG y JPEG a WEBP -->
<!-- By Emanuel Nuñez -->


<!-- 1. Lo primero que se debe hacer es corroborar que Python 3 está instalado, correr en cualquier cmd: -->
python3
<!-- Esto nos va a decir si Python está instalado. De estarlo, nos indicará la versión del mismo, de lo contrario, comenzará a instalarse -->

<!-- 2. Una vez instalado Python, debemos instalar un "Virtual Enviroment" para evitar dañar alguna carpeta/archivo con python.
Para esto, se debe utilizar el cmd en la carpeta que utilicemos, para instalar este espacio de trabajo, en este caso será "Venv" -->
python3 -m venv venv

<!-- 3. Verificar que Venv está instalado con: -->
ls (Powershell - Git Bash) / dir (Cmd Prompt)

<!-- 4. Para ingresar al venv desde el "cmd" o "Command Prompt" -->
.\venv\Scripts\activate.bat
<!-- Para ingresar al venv desde el "Powershell" o "Git Bash" -->
.\venv\Scripts\activate.psl

<!-- 5. Debería aparecer delante de la linea principal de comandos de la terminal, lo siguiente: -->
(venv)

<!-- 6. Instalar la librería Pillow con pip -->
pip install Pillow 

<!-- 7. Proceder a utilizar el archivo convert-webp.py -->
python convert-webp.py

<!-- 8. Para salir del venv, escribir: -->
deactivate