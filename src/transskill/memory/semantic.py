"""Empty semantic-memory extension point; no knowledge is bundled."""
class EmptySemanticMemory:
    def retrieve(self, query):
        return []
