# Módulo de optimización

## HVAC_Model

En este módulo de python se genera el modelo de regresión Random Forest bajo los siguientes parámetros

criterio = 'mse' (error cuadrático medio)

profundidad máxima = None

características = 'auto' ('int', 'float', 'sqrt', 'log2')

hojas máximas = None ('int')

número de árboles = 10

númeor de trabajos paralelos = 2 

estado aleatorio= None

Haciendo lectura de los datasets tratados:

[predictors](input/predictors.xlsx)

[targets](input/target.xlsx)

##ModuloOptimizacion

En este módulo de python se define el siguiente problema de optimización:

Funciones objetivo
Min( Costo = Costo_forest.predict(configuración) )
Min( Consumo = Confort_forest.predict(configuración) )
Max( Confort = Confort_forest.predict(configuración) )
Max( COP = COP_forest.predict(configuración) )

Variables de decisión
Ce1 = Capacidad enfriador 1
Ce2 = Capacidad enfriador 2
Cc1 = Capacidad bombas de calor 1
Cc2 = Capacidad bombas de calor 2

Restricciones
Si Ce1 > 0 y Ce2 >0 Entonces Cc1 = 0 y Cc2 = 0
Si Cc1 > 0 y Cc2 >0 Entonces Ce1 = 0 y Ce2 = 0
Ce1, Ce2, Cc1, Cc2 Pertenecen a [0,100]
