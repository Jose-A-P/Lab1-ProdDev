# Gestion de Experimentacion y Modelos con DVC Automated Machine Learning (AutoML)

### Requisitos
- Python 3.11+ (instalado en PATH)
- pip
- git
- dvc (>=2.0)

Los datasets se descargan del siguiente enlace: [datasets](https://drive.google.com/drive/folders/1Pg-B2LDOITkfRdNqn20T0Hlynrf91YdI?usp=sharing). Estos deben de ser agregados a la carpeta data.

### Instalacion

Estos pasos se deben de ejecutar en la terminal, dentro de la carpeta donde se manejara el archivo.

1. Clonar el repositorio:

Se puede realizar como una descarga de zip desde el siguiente link [Repositorio Lab1 PD](https://github.com/Jose-A-P/Lab1-ProdDev.git)

o utilizando la terminal:
```console
git clone https://github.com/Jose-A-P/Lab1-ProdDev.git
```

2. Crear un entorno virtual en windows y activarlo en la terminal actual:

```console
python -m venv venv
venv\Scripts\activate.bat # CMD
```

3. instalar las dependencias: 

```console
pip install -r requirements.txt
```

Llegado a este paso ya se encuentra clonado e instalado de manera apropiada el repositorio para ser utilizado. Al ejecutar o modificarlo se debe de activar el entorno utilizando:

```console
venv\Scripts\activate.bat # CMD
``` 

Asegurandose siempre de estar en la carpeta designada en la terminal.

### Ejecutar el pipeline

Al encontrarse en la terminal y el entorno virtual del proyecto activado se puede ejecutar lo siguiente:

```console
dvc repro
```

Esto ejecutara por etapas:
1. preprocess: Limpieza y codificacion de los datos.
2. train: entrenamiento de los modelos definidos en `params.yaml`
3. evaluate: calculo y almacenamiento de metricas en `metrics.json` y generacion de `report.csv`

### Como se pueden ver las metricas actuales:

Para mostrar las metricas actuales se puede utilizar:

```console
dvc metrics show
```

### Como se pueden comparar las metricas entre versiones:

Para comparar las metricas entre versiones o commits se puede utilizar:

```console
dvc metrics diff --all
```

Este mostrara las metricas del modelo actual, comparandolo con una version anterior. Si no se encuentra una version anterior o ya se hizo `commit` a la version actual, terminara comparando la version actual con ella misma.

### Como se puede cambiar el dataset:

Se debe de copiar el nuevo archivo de datos en la carpeta `data`. Este debe de ser unicamente en formato CSV. En este parrafo el nuevo dataset tomara el nombre de 'dataset_vN.csv'

Luego de haberlo copiado, en la terminal se debe de ejecutar:

```console
dvd add data/dataset_vN.csv
```
Esto permitira el versionamiento con DVC. Al haberlo ejecutado, se recomienda hacer un commit de estos cambios en github para guardar la nueva version.

Luego, se debe de editar el archivo `params.yaml`, colocando el nombre del dataset a utilizar en la siguiente posicion:

```yaml
data:
  input: data/dataset_vN.csv
```

Colocando el nombre del nuevo dataset en la variable input de `data`.

Al haber cambiado los datos se puede ejecutar:

```console
dvc repro
```

Esto actualizara las metricas y resultados del experimento, utilizando el nuevo dataset. 

Dado que no se ha realizado un commit, se puede utilizar: 

```console
dvc metrics diff
```

Esto permitira corroborar las metricas actuales, con el experimento anterior. Luego de hacer commit este comando no funcionara o se debe de agregar `--all` al final, para que muestre resultados.
