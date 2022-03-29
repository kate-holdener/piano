class EventQueueRunner:
    def __init__(self, queue, controller):
        self.event_queue = queue
        self.controller = controller
        self.terminate = False

    def run(self):
        self.terminate = False
        while not self.terminate:
            self.process()

    def process(self):
        event = self.event_queue.get()
        self.controller.process_event(event)
       
    def stop(self):
        self.terminate = True
