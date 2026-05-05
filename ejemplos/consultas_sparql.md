# Consultas SPARQL - Ontología de Ciberseguridad

## Namespace
```
http://www.CAVFL019.org/ciberseguridad#
```

## Consulta 1: Controles que mitigan Phishing
```sparql
SELECT ?control WHERE {
    <http://www.CAVFL019.org/ciberseguridad#Phishing>
    ^<http://www.CAVFL019.org/ciberseguridad#mitiga> ?control .
}
```

## Consulta 2: Listar todas las amenazas
```sparql
SELECT ?amenaza WHERE {
    ?amenaza rdf:type <http://www.CAVFL019.org/ciberseguridad#Amenaza> .
}
```

## Consulta 3: Listar todos los controles
```sparql
SELECT ?control WHERE {
    ?control rdf:type <http://www.CAVFL019.org/ciberseguridad#Control> .
}
```

## Consulta 4: Ver todas las relaciones mitiga
```sparql
SELECT ?control ?amenaza WHERE {
    ?control <http://www.CAVFL019.org/ciberseguridad#mitiga> ?amenaza .
}
```

## Consulta 5: Listar todos los activos
```sparql
SELECT ?activo WHERE {
    ?activo rdf:type <http://www.CAVFL019.org/ciberseguridad#Activo> .
}
```
