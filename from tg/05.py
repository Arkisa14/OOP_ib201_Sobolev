class Document:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self._content = content
        self.__audit_log: list[str] = []
    
    def read(self) -> str:
        return self._content
    
    def history(self) -> tuple[str, ...]:
        return tuple(self.__audit_log)
    
    def _log(self, event: str) -> None:
        self.__audit_log.append(event)
    
    def _purge_history(self) -> None:
        self.__audit_log.clear()

class EditorDocument(Document):
    def edit(self, new_content: str) -> None:
        event = f'edit: {self._content} -> {new_content}'
        self._log(event)
        self._content = new_content

class AdminDocument(EditorDocument):
    def purge_history(self) -> None:
        self._purge_history()