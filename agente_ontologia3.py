from rdflib import Graph, Namespace, RDF, RDFS

# Cargar la ontología
g = Graph()
g.parse("ontologia3.rdf", format="xml")

# Namespace de tu ontología
ns = Namespace("http://www.semanticweb.org/carlos/ontologies/2026/4/untitled-ontology-7#")

class AgenteCiberseguridad:
    def __init__(self, grafo):
        self.grafo = grafo

    def recomendar(self, amenaza):
        consulta = f"""
        PREFIX ns: <http://www.semanticweb.org/carlos/ontologies/2026/4/untitled-ontology-7#>
        SELECT ?control WHERE {{
            ?control ns:mitiga <{ns[amenaza]}> .
        }}
        """
        return [str(r[0]).split("#")[-1] for r in self.grafo.query(consulta)]

    def evaluar_riesgo(self, amenaza):
        controles = self.recomendar(amenaza)
        cantidad = len(controles)
        if cantidad == 0:
            return "ALTO - Sin controles definidos"
        elif cantidad == 1:
            return "MEDIO - Un control disponible"
        else:
            return "BAJO - Multiples controles disponibles"

# Programa principal
if __name__ == "__main__":
    agente = AgenteCiberseguridad(g)

    print("=" * 50)
    print("   AGENTE DE CIBERSEGURIDAD - CAVFL019")
    print("=" * 50)

    amenazas = ["Phishing_Corporativo", "Phishing_Banco"]

    for amenaza in amenazas:
        controles = agente.recomendar(amenaza)
        riesgo = agente.evaluar_riesgo(amenaza)
        print(f"\nAmenaza: {amenaza}")
        print(f"Controles: {controles if controles else 'Ninguno registrado'}")
        print(f"Nivel de riesgo: {riesgo}")

    print("\n" + "=" * 50)
    print("Analisis completado")