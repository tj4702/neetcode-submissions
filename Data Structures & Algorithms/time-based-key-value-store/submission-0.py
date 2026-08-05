class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keys:
            return ''
        
        # print(self.keys[key])

        curr = ''

        self.keys[key].sort(key = lambda item: item[1])

        for value, timestamp_prev in self.keys[key]:
            if timestamp_prev <= timestamp:
                curr = value
        return curr
        
