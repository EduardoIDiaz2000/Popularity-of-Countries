## Popularidad de países de Sudamérica

### 1. Requerimientos
* Tener instalado Anaconda  
* De preferencia instalar Mamba para una mejor aceleración respecto a Conda  
* Tener un sistema operativo Mac, Linux o Windows (WSL)  
* Usar un editor de texto plano (VS Code)  

### 2. Clonar y instalar el entorno

* Clonar el repositorio:
  git clone git@github.com:EduardoIDiaz2000/Popularity-of-Countries.git
  cd Popularity-of-Countries

### 4. Instalar el entorno con Conda/Mamba 
* Se instalara el entorno virtual desde el archivo environment.yml
`-`En el caso de usar conda (conda env create -f environment.yml)
`-`En el cado de usar mamba (mamba env create -f environment.yml)

### 5. Activar el ambiente virtual
* Con conda se realiza de la siguiente forma: conda activate nombre_del_entorno
* Con mamba es de la misma manera: mamba activate nombre_del_entorno

### 6. Ejecución del script
* Mediante la terminal ejecuta el comando (python main.py)
* Generara un grafico de barras que estara ubicado en la carpeta imgs