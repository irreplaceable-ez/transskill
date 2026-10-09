"""Empty episodic-memory extension point; no histories are bundled."""
class EmptyPracticum:
    def retrieve(self, query):
        return []
