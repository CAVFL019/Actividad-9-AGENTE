from rdflib import Graph, Namespace, RDF

# Cargar la ontología
g = Graph()
g.parse("ontologia.owl", format="xml")

# Definir namespace
CYBER = Namespace("http://www.CAVFL019.org/ciberseguridad#")

class AgenteSeguridad:
    def __init__(self, grafo):
        self.grafo = grafo

    def recomendar(self, amenaza):
        """Devuelve controles que mitigan la amenaza dada."""
        amenaza_uri = CYBER[amenaza]
        query = f"""
        PREFIX cyber: <http://www.CAVFL019.org/ciberseguridad#>
        SELECT ?control WHERE {{
            ?control cyber:mitiga <{amenaza_uri}> .
        }}
        """
        resultados = self.grafo.query(query)
        controles = [str(row.control).split("#")[-1] for row in resultados]
        return controles

    def evaluar_riesgo(self, amenaza):
        """Clasifica el riesgo según número de controles disponibles."""
        controles = self.recomendar(amenaza)
        cantidad = len(controles)
        if cantidad == 0:
            return "ALTO - Sin controles definidos"
        elif cantidad == 1:
            return "MEDIO - Un control disponible"
        else:
            return "BAJO - Múltiples controles disponibles"

# Programa principal
if __name__ == "__main__":
    agente = AgenteSeguridad(g)
    print("=== Agente de Ciberseguridad ===\n")
    amenazas = ["Phishing", "Malware", "Ransomware"]
    for amenaza in amenazas:
        print(f"Amenaza: {amenaza}")
        controles = agente.recomendar(amenaza)
        riesgo = agente.evaluar_riesgo(amenaza)
        print(f"  Controles: {controles if controles else 'Ninguno'}")
        print(f"  Nivel de riesgo: {riesgo}\n")
