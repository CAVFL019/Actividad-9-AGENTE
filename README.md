# Actividad 9 - Agente de Ciberseguridad con Ontología OWL

## Descripción
Ontología de ciberseguridad desarrollada en OWL/RDF con un agente inteligente 
en Python que razona sobre amenazas y recomienda controles de seguridad.

## Namespace
http://www.CAVFL019.org/ciberseguridad#

## Estructura
- `ontologia.owl` — Ontología en formato OWL/RDF
- `agente_python.py` — Agente inteligente con rdflib y SPARQL
- `ejemplos/consultas_sparql.md` — Consultas SPARQL de ejemplo
- `docs/guia_publicacion.md` — Guía de uso y publicación

## Clases
- **Amenaza**: Phishing, Malware, Ransomware
- **Control**: Firewall, Antivirus, AutenticacionDobleFactor
- **Activo**: BaseDeDatos, ServidorWeb

## Relaciones
- **mitiga**: Un control mitiga una amenaza
- **afecta**: Una amenaza afecta un activo

## Ejemplo de consulta SPARQL
```sparql
SELECT ?control WHERE {
    <http://www.CAVFL019.org/ciberseguridad#Phishing>
    ^<http://www.CAVFL019.org/ciberseguridad#mitiga> ?control .
}
```

## Requisitos
- Python 3.x
- `pip install rdflib`

## Cómo ejecutar
```bash
python agente_python.py
```
