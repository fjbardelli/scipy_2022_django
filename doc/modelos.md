# Modelos de datos de la app

## Parte 1 (Modelos de Ejemplos)

### Servicios

- id [int => autonómico]
- nombre [string => 50]
- nro_telefono [string => 15]
- descripcion = [string => text]
- created_at = [date]
- updated_at = [date]
- version = [int]

### Moviles

- id [int => autonómico]
- patente [string => 6]
- servicio [id de Relación]


## Parte 2 (Modelo para el CSV)

### Casos

- id [int => autonómico]
- fecha [date => ]
- llamados [int => default 0 ]
- sospechosos [int => default 0 ]
- descartados [int => default 0 ]
- trasladados [int => default 0 ]
- derivados [int => default 0 ]
