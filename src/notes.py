"""Notes module — core CRUD logic."""
from datetime import datetime


class Note:
    """Represents a single note."""

    def __init__(self, note_id: int, title: str, content: str):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert note to a dictionary (JSON-friendly)."""
        return {
            "id": self.note_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
        }


class NotesStore:
    """In-memory storage for notes."""

    def __init__(self):
        self.notes = []
        self.next_id = 1

    def create(self, title: str, content: str) -> dict:
        """Create a new note and return it as a dict."""
        note = Note(self.next_id, title, content)
        self.notes.append(note)
        self.next_id += 1
        return note.to_dict()

    def get_all(self) -> list:
        """Return all notes as a list of dicts."""
        return [note.to_dict() for note in self.notes]

    def get_by_id(self, note_id: int) -> dict | None:
        """Find and return a single note by ID, or None if not found."""
        for note in self.notes:
            if note.note_id == note_id:
                return note.to_dict()
        return None


# Quick test — runs only when you execute this file directly
if __name__ == "__main__":
    store = NotesStore()
    store.create("First note", "Learning Python + AWS")
    store.create("Shopping", "Milk, bread, eggs")

    print("All notes:")
    for note in store.get_all():
        print(note)

    print("\nNote with ID 1:")
    print(store.get_by_id(1))