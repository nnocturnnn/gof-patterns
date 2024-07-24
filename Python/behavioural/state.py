class State:
    def handle(self, context):
        pass


class NewOrderState(State):
    def handle(self, context):
        print("Order is in the 'New' state.")
        context.set_state(SentOrderState())


class SentOrderState(State):
    def handle(self, context):
        print("Order is in the 'Sent' state.")
        context.set_state(DeliveredOrderState())


class DeliveredOrderState(State):
    def handle(self, context):
        print("Order is in the 'Delivered' state.")


class OrderContext:
    def __init__(self):
        self.state = NewOrderState()

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


order = OrderContext()
order.request()
order.request()
order.request()
