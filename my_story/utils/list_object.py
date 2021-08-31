class ListObject:
    def __init__(self, status_code=None, detail=None, items=None) -> None:
        self.status_code = status_code
        self.detail = detail
        self.items = items
