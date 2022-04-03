from queue import Queue
from use_cases.event_queue_runner import EventQueueRunner

class Controller:
    def __init__(self):
        self.event_count = 0

    # pylint: disable=unused-argument
    def process_event(self, event):
        self.event_count+=1

def init_components(queue_size):
    event_queue = Queue(queue_size)
    test_controller = Controller()
    event_queue_runner = EventQueueRunner(event_queue, test_controller)
    return (event_queue, test_controller, event_queue_runner)

def test_one_event():
    # assemble the test components
    (event_queue, test_controller, event_queue_runner) = init_components(1)

    # act on the test components
    event_queue.put('hi')
    event_queue_runner.drain_queue()

    # assert the expected state
    assert test_controller.event_count == 1
    assert event_queue.empty()

def test_run_thread():
    # assemble the test components
    (event_queue, test_controller, event_queue_runner) = init_components(1)

    # act on the test components
    event_queue.put('hi')
    event_queue_runner.run()
    event_queue_runner.stop()

    # assert the expected state
    assert test_controller.event_count == 1
    assert event_queue.empty()

def test_thread_multi_event():
    # assemble the test components
    (event_queue, test_controller, event_queue_runner) = init_components(1)

    # act on the test components
    event_queue.put('hi')
    event_queue_runner.run()
    event_queue.put('hello')
    event_queue.put('dog')
    event_queue_runner.stop()

    # assert the expected state
    assert event_queue.empty()
    assert test_controller.event_count == 3
