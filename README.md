# Cómo generar el índice y las páginas de los proyectos
#### Requerimientos
1. Tener Python instalado.
2. Tener las bibliotecas [Pandas](https://pypi.org/project/pandas/) y [Airium](https://pypi.org/project/airium/0.1.4/) instaladas.  
`pip install airium`    
`pip install pandas`

#### Uso
En el proyecto existen dos scripts: 
* **createIndex.py**: usado para generar el índice de la Muestra Virtual.
* **createProjects.py**: usado para generar una página con información detallada por proyecto.    


Los scripts requieren de dos archivos de Excel para obtener la información y generar el contenido. Estos archivos son *info muestravirtual final 2-12-2021.xlsx* y *proyectos registrados final 2-11-2021.xlsx*. A la hora de correr el programa es importante que tanto el script de Python como los archivos de Excel estén en el mismo directorio.
Usa los siguientes comandos para generar las páginas HTML que deseas:    
`python createIndex.py` - para generar la página del índice.  
`python createProjects.py` - para generar las páginas de los proyectos

Si se requiere hacer cambios a las páginas del HTML, te recomiendo checar los ejemplos que vienen en la documentación de Airium para familiarizarte con su sintaxis.





