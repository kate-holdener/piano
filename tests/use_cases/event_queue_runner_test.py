from queue import Queue
from use_cases.event_queue_runner import EventQueueRunner

class Controller:
    def __init__(self):
        self.event_count = 0
    def process_event(self, event):
        self.event_count+=1

def test_one_event():
    event_queue = Queue(1)
    test_controller = Controller()
    event_queue_runner = EventQueueRunner(event_queue, test_controller)
    event_queue.put('hi')
    event_queue_runner.drain_queue()
    assert test_controller.event_count == 1
    assert event_queue.empty()

