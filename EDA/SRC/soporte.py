# tratamiento de datos
import pandas as pd
import numpy as np

# visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns


def grafico_barras(series, top_n=10, title='', xlabel='Cantidad', ylabel='', palette='viridis'):
    """
    creamos un gráfico de barras horizontales para los valores más frecuentes en una serie.
    tenemos en cuenta:
    - series: Serie de pandas (ej. df['CompanyName'])
    - top_n: número de categorías a mostrar
    - title: título del gráfico
    - xlabel: etiqueta del eje x
    - ylabel: etiqueta del eje y
    - palette: paleta de colores de seaborn
    """
    top_counts = series.value_counts().head(top_n)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_counts.values, y=top_counts.index, palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def graficar_ingresos(df, columna_categoria, top_n=10, titulo=None):
    """
    Grafica los ingresos totales por una categoría específica.
    tenemos en cuenta:
    - df: DataFrame original (debe tener columnas 'event_type', 'price' y la columna de categoría)
    - columna_categoria: columna a usar para agrupar ('PrimaryCategory', 'SecondaryCategory', 'brand')
    - top_n: cuántas categorías mostrar en el gráfico
    - titulo: título para cada gráfico
    """


    df_ventas = df[df['event_type'] == 'purchase'].copy()
    ingresos_categoria = (
        df_ventas.groupby(columna_categoria)['price']
        .sum()
        .sort_values(ascending=False)
        .reset_index(name='ingreso_total')
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(data=ingresos_categoria.head(top_n),
                x='ingreso_total',
                y=columna_categoria)
    if not titulo:
        titulo = f'Top {top_n} {columna_categoria} con mayor ingreso total'
    plt.title(titulo)
    plt.xlabel('Ingreso total ($)')
    plt.ylabel(columna_categoria)
    plt.tight_layout()
    plt.show()


def graficar_productos_recomprados(df, top_n=10):
    """
    Grafica los productos más recomprados por los mismos usuarios.

    Parámetros:
    - df: DataFrame con columnas 'event_type', 'user_id', 'product_id', 'ProductName'
    - top_n: cantidad de productos a mostrar en el grafico

    Retorna:
    - DataFrame con los productos recomprados
    """
   
    df_compras = df[df['event_type'] == 'purchase'].copy()

    # cuenta compras por usuario y producto
    compras_usuario_producto = (
        df_compras.groupby(['user_id', 'product_id'])
        .size()
        .reset_index(name='recompras')
    )

    # mas compras del mismo producto por el mismo usuario
    recompras = compras_usuario_producto[compras_usuario_producto['recompras'] > 1]

    productos_mas_recomprados = (
        recompras.groupby('product_id')
        .size()
        .reset_index(name='usuarios_recompra')
        .sort_values(by='usuarios_recompra', ascending=False)
    )

    #agregamos nombre y marca
    detalles = df[['product_id', 'ProductName', 'BrandName']].drop_duplicates()
    resultado = productos_mas_recomprados.merge(detalles, on='product_id', how='left')

    top_resultado = resultado.head(top_n)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_resultado,
                x='usuarios_recompra',
                y='ProductName',
                palette='viridis')
    plt.title(f'Top {top_n} productos más recomprados por los mismos usuarios')
    plt.xlabel('Cantidad de usuarios que recompraron')
    plt.ylabel('Producto')
    plt.tight_layout()

    return top_resultado

def analizar_estacionalidad(df):
    """
    Analiza la estacionalidad de las compras según día de la semana y hora.
    """
    df_compras = df[df['event_type'] == 'purchase'].copy()
    df_compras['event_time'] = pd.to_datetime(df_compras['event_time'])

    df_compras['dia_semana'] = df_compras['event_time'].dt.day_name()
    df_compras['mes'] = df_compras['event_time'].dt.month_name()
    df_compras['hora'] = df_compras['event_time'].dt.hour

    #orden dias
    orden_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    #dia
    plt.figure(figsize=(8,5))
    sns.countplot(data=df_compras, x='dia_semana', order=orden_dias,palette='viridis')
    plt.title('Compras por día de la semana')
    plt.xlabel('Día')
    plt.ylabel('Cantidad de compras')
    plt.xticks(rotation=45)
    plt.tight_layout()

    #hora
    plt.figure(figsize=(10,5))
    sns.countplot(data=df_compras, x='hora', palette='cubehelix')
    plt.title('Compras por hora del día')
    plt.xlabel('Hora')
    plt.ylabel('Cantidad de compras')
    plt.tight_layout()
  