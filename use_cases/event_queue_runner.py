class EventQueueRunner:
    def __init__(self, queue, controller):
        self.event_queue = queue
        self.controller = controller
        self.terminate = False

    def run(self):
        self.terminate = False
        while not self.terminate:
            self.drain_queue()

    def drain_queue(self):
        while not self.event_queue.empty():
           event = self.event_queue.get()
           self.controller.process_event(event)
       
    def stop(self):
        self.terminate = True
