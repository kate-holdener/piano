import threading
class EventQueueRunner:
    """
    This class reads events from a queue and passes them t0
    controller.process_event(event) function in a dedicated
    thread. To start processing, use run() function. To stop
    processing use stop() function. All events that were in the
    queue before stop() function was called get processed.
    """
    def __init__(self, queue, controller):
        self.event_queue = queue
        self.controller = controller
        self.terminate = False
        self.queue_drain_thread = threading.Thread(target=self.process_queue)

    def run(self):
        self.queue_drain_thread.start()

    def process_queue(self):
        self.terminate = False
        while not self.terminate:
            self.drain_queue()

    def drain_queue(self):
        while not self.event_queue.empty():
            event = self.event_queue.get()
            self.controller.process_event(event)

    def stop(self):
        self.terminate = True
        self.queue_drain_thread.join()
