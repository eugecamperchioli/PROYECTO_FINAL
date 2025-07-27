# 🧪 Análisis Exploratorio de Datos (EDA) de Productos Cosméticos y Ventas Online

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) combinando dos fuentes de información:

1. **Dataset de productos químicos reportados** (información sobre ingredientes, fechas de reporte, marcas y categorías).
2. **Dataset de eventos de compra online** (ventas de productos cosméticos, usuarios, precios y sesiones de compra).

El objetivo es comprender mejor el comportamiento de ventas, la presencia de químicos potencialmente descontinuados y cómo interactúan los usuarios con ciertos tipos de productos.


## 📁 Archivos del proyecto

### `cscpopendata.csv`
[Dataset descargado desde Kaggle:](https://www.kaggle.com/datasets/krrai77/chemicals-in-cosmetics)  
Contiene información de productos cosméticos y los ingredientes químicos asociados.

1. CDPHId: identificador interno del producto
2. ProductName: nombre del producto           
3. CSFId:  número de identificación del color, aroma o sabor asignado por CDPH, tenemos 33.973 nulos               
4. CSF: nombre textual de ese color, aroma o sabor. tenemos 34.398 nulos 
5. CompanyId: ID de la compañia
6. CompanyName: nombre de la compañia
7. BrandName: nombre de la marca
8. PrimaryCategoryId: identificador de la categoria primaria
9. PrimaryCategory: nombre de la categoria primaria
10. SubCategoryId: identificador de la subcategoria
11. SubCategory: nombre de la subcategoria
12. CasId: Ingrediente químico (interno del producto)         
13. CasNumber: Número CAS global de la sustancia, tenemos 6.476 nulos     
14. ChemicalId: ID del nombre quimico
15. ChemicalName: Instancia química específica del producto
16. InitialDateReported: fecha en que el perfil del producto (no del ingrediente) fue creado por primera vez y enviado por el fabricante
17. MostRecentDateReported: fecha en que el perfil del producto fue modificado por última vez antes de su presentación al CDPH
18. DiscontinuedDate: Fecha en que CDPH marcó el producto como ya no disponible en el mercado. Si está vacía (NaN), el producto aún se considera activo, tenemos 101.715 nulos
19. ChemicalCreatedAt: Fecha en que se reportó por primera vez ese ingrediente químico en el producto específico     
20. ChemicalUpdatedAt: Última fecha en que se modificó el registro del ingrediente químico para ese producto  
21. ChemicalDateRemoved: Fecha en que este ingrediente fue eliminado del producto (reformulación), tenemos 111.650 nulos
22. ChemicalCount: Número de químicos actualmente REPORTADOS en el producto, excluyendo aquellos que fueron eliminados  

### `sales_dataset.csv`
[Dataset descargado desde Kaggle:](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop?select=2020-Jan.csv)  
Registra las transacciones de compra realizadas por usuarios en una tienda online de cosméticos.
1. event_time: Fecha y hora del evento (UTC)
2. event_type: Tipo de evento (filtramos solo "purchase" en este caso)
3. product_id: ID del producto comprado
4. category_id: ID de la categoría del producto
5. category_code: Código o nombre de la categoría del producto
6. brand: Marca del producto en minúsculas
7. price: Precio del producto
8. user_id: ID único del usuario
9. user_session: ID temporal de la sesión del usuario 

## 🎯 Objetivos del análisis

- Identificar los productos que contienen ingredientes químicos discontinuados.
- Analizar las ventas por categoría, marca y momento del día.
- Explorar la relación entre ingredientes y comportamiento de compra.
- Detectar tendencias estacionales o por hora/día de la semana.
- Visualizar las marcas más vendidas y su composición química.

## 📊 Metodología

1. **Carga y limpieza** de ambos datasets.
2. **Unión** de datasets mediante `product_id` y marcas limpias (`brand_clean`).
3. Análisis de:
   - Distribución de químicos por categoría
   - Evolución de descontinuaciones por año
   - Comportamiento de compra por hora/día
   - Comparación de precios por categoría
4. **Visualizaciones** con gráficos de barras, líneas, y mapas de calor.


## 📈 Analisis Realizado
- Analisis preliminar
- Limpieza de datos: tratamiento de valores nulos, outliers y codificacion. 
- Analisis univariado: distribucion de variables numericas y categoricas.
- Analisis bivariado: tasa de conversión segun variables claves. 
- Analisis temporal: suscripciones a lo largo del tiempo.
- Segmentaciones: impacto de la economia en el compartamiento del cliente.

## 🧰 Tecnologías usadas
- Python 
- Pandas
- Numpy
- Seaborn
- Matplotlib
- Jypter Notebook
- Dashboard / Excel

## 📂 Estructura del Proyecto
Proyecto/
├── EDA/
│   ├── DATA/
│   │   ├── RAW/                        # ***Datos originales sin procesar***
│   │   │   ├── 2020-Jan.csv
│   │   │   └── cscpopendata.csv
│   │   ├── OUTPUT/                     # ***Datos limpios y combinados***
│   │   │   ├── cscpopendata_limpio.csv
│   │   │   └── datos_unificados.csv
│   │
│   ├── NOTEBOOK/                       # ***Notebooks de análisis***
│   │   ├── 01-analisis_preliminar.ipynb
│   │   ├── 02-limpieza.ipynb
│   │   └── 03-EDA.ipynb
│   │
│   └── SRC/                            # ***Código auxiliar / scripts***
│       └── soporte.py
│
├── DASHBOARD/
│   └── excel_dashboard_proyectofinal2.xlsx   # ***Dashboard final en Excel***


## ✅ Conclusiones
- el top 5 de empresas con mas productos quimicos reportados es liderado por LOREAL y seguido por SEPHORA, COTY, REVLON Y BARE.
- el top 5 de categorias mas frecuentes es liderado por MAQUILLAJE y seguido por CUIDADO DE UÑAS, CUIDADO DE LA PIEL, PRODUCTOS RELACIONADOS CON EL SOL Y CON EL BAÑO.
- el top 5 de subcategorias mas frecuentes es liderado por LABIALES y seguido por SOMBRAS DE OJOS, BASES, ESMALTES, LIP GLOSS Y DELINEADORES DE OJOS.
- el producto quimico mas eliminado es el Dioxido de Titanio, hay mucha distancia en relacion a los demas productos eliminados. en segundo lugar con una cantidad mucho menor es la cocamida dietanolamina
- la proporcion de productos eliminados es muy baja, solo un 2.4% en la base que estamos estudiando
- las dos empresas que lideran la eliminacion de procutos son FANTASIA INSDUSTRIES E IMPERIAL DAX HAIR CARE.
- El modelo de regresion obtuvo un error absoluto medio (MAE) de 166 días, significa que en promedio se equivoca por unos 5–6 meses al predecir la vida útil de un producto. El coeficiente de determinación (R²) fue 0.14, lo que indica que el modelo explica aproximadamente el 14% de la variabilidad en los tiempos de eliminación. esto lo utilizamos para estimar cuántos días vive un producto químico antes de ser eliminado del mercado, en función de sus características.
- podemos deducir que las marcas en general son mas conservadoras que innovadoras al no realizar muchas cambios en sus formulaciones.
- las marcas con mayor volumen de compra son CND, ENTITY Y MATRIX.
- el titanium dioxide es el ingrediente mas frecuente en los productos mas vendidos.
- el precio promedio de la marca mas vendida es de 15$, mientras que orly es la marca con precio promedio mas bajo 12$ y joico es la marca con precio promedio mas alto 40$.
- las marcas que mayor ingreso total generan son las mismas con mayor volumen de compra CND, MATRIX y ENTITY. 
- la categoria que mayor ingreso genera es la de PRODUCTOS PARA LAS UÑAS.
- Los 10 productos que son mayormente recomprados por los usuarios son: PURE PINK SCULTING POWDER, PURE WHITE SCULPTING POWDER, CREATIVE PLAY BASE COAT, CREATIVE PLAY NAIL LACQUER, BRISA PAINT LIQUID GEL, PERFECT COLOR SCULPTING POWDER, VINYLUX WEEKLU POLISH, SHELLAC COLOR COAT, BRISA SCULPTING GEL CREATIVE PLAY POLISH.
- los martes, miercoles y jueves los consumidores tienden a comprar mas, pero no hay mucha diferencia con los demas dias. 
- el horario mas fuerte para la compra es las 12hs, seguido por las 19 y 20hs


## 📌 Próximos pasos
- consultar si existe un impulso por parte de la pagina web para ciertos productos. 
- cruzar la informacion con los demas meses para verificar la tendencia. 
- verificar stock de la web a fin de confirmar si tiene alguna implicancia en el mix vendido. 


## 📎 Notas
- Las fechas están en formato UTC.
- Los precios no incluyen impuestos o descuentos.
- Los nombres de marcas pueden variar ligeramente entre datasets y fueron limpiados para análisis.