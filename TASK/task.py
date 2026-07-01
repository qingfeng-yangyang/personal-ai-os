class Task:
    def __init__(self, task_id, input_text):
        self.task_id = task_id
        self.input = input_text

        self.type = None
        self.level = None
        self.status = "created"
        self.agent = None
        self.version = 1

        self.result = None
        self.quality = None
        self.retry_count = 0

        self.meta = {
            "created_time": None,
            "source": "main"
        }
