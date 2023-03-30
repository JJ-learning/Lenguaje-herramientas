# Juan José Méndez Torrero i42metoj@uco.es

# Creamos un data frame vacio
empleados <- data.frame(nombreUsuario=c(), 
                        valoracion=c(),
                        seccion=c(),
                        ganancias=c(),
                        complementos=c(),
                        empleadpMes=c()
                        )

# Inicializamos similla random
set.seed(123)

# Creamos 10 usuarios aleatorios
for (i in 1:10){
  nombreUsuario = paste("usuario", as.character(i), sep="-")
  valoracion = as.integer(sample(1:5, size=1))
  seccion = sample(c("control de stock", "ventas", "compras", "cuentas"), size=1)
  ganancias = as.integer(sample(1000:3000, size=1))
  complementos = as.integer(sample(500:1000, size=1))
  empleado_mes = sample(c(TRUE, FALSE), size=1)
  
  # Concatenamos por fila dentro del data frame vacio creado
  empleados <- rbind(empleados, c(nombreUsuario, valoracion, seccion, ganancias, complementos, empleado_mes))
}

# Cambiamos el nombre de las columnas del data frame
colnames(empleados) <- c("nombeUsuario", "valoracion", "seccion", "ganancias", "complementos", "empleadoMes")

# Creamos un vector auxiliar
aux_ganancias <- c()

for (i in 1:10){
    
  # Si es empleado mes
  if (empleados$empleadoMes[i]){
    aux_ganancias <- cbind(aux_ganancias, as.integer(empleados$ganancias[i]) + as.integer(empleados$complementos[i]) * 2)
  }
  
  # Si no es empleado mes
  else {
    aux_ganancias <- cbind(aux_ganancias, as.integer(empleados$ganancias[i]) + as.integer(empleados$complementos[i]))
  }
}

# Añadimos el vector creado a la columna de ganancias totales
empleados$gananciasTotales <- c(aux_ganancias)

