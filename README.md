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
## Componentes del Agente

### 1. Ontología (OWL/RDF)
- Define las clases: Amenaza, Control, Activo
- Define las relaciones: mitiga, afecta
- Contiene los individuos: Phishing, Malware, Firewall, AutenticacionDobleFactor, etc.
- Sirve como base de conocimiento estructurado

### 2. Motor de razonamiento (rdflib + SPARQL)
- Carga la ontología en un grafo RDF
- Ejecuta consultas SPARQL para inferir relaciones
- Permite extender reglas y consultas más complejas

### 3. Agente (clase en Python)
- **Percepción**: Detecta una amenaza (entrada del usuario o sistema)
- **Razonamiento**: Consulta la ontología para encontrar controles asociados
- **Acción**: Recomienda controles o clasifica el riesgo

Métodos principales:
- `recomendar(amenaza)` → devuelve controles que mitigan la amenaza
- `evaluar_riesgo(amenaza)` → clasifica la amenaza según número de controles disponibles

### 4. Interfaz de interacción
- Script en consola que permite introducir amenazas
- Recibe recomendaciones de controles de seguridad
- Puede extenderse a API REST o chatbot

### 5. Repositorio (GitHub)
- Contiene la ontología `ontologia.owl`
- Incluye ejemplos de consultas SPARQL y código del agente
- Facilita colaboración y control de versiones
