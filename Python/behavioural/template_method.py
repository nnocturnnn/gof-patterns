from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def process_payment(self, amount):
        self.validate_data(amount)
        self.execute_payment(amount)
        self.log_payment(amount)

    @abstractmethod
    def validate_data(self, amount):
        pass

    @abstractmethod
    def execute_payment(self, amount):
        pass

    @abstractmethod
    def log_payment(self, amount):
        pass


class PayPalProcessor(PaymentProcessor):
    def validate_data(self, amount):
        print(f"Валидация данных для PayPal: сумма {amount}")

    def execute_payment(self, amount):
        print(f"Выполнение платежа через PayPal: сумма {amount}")

    def log_payment(self, amount):
        print(f"Логирование платежа через PayPal: сумма {amount}")


class StripeProcessor(PaymentProcessor):
    def validate_data(self, amount):
        print(f"Валидация данных для Stripe: сумма {amount}")

    def execute_payment(self, amount):
        print(f"Выполнение платежа через Stripe: сумма {amount}")

    def log_payment(self, amount):
        print(f"Логирование платежа через Stripe: сумма {amount}")


class SquareProcessor(PaymentProcessor):
    def validate_data(self, amount):
        print(f"Валидация данных для Square: сумма {amount}")

    def execute_payment(self, amount):
        print(f"Выполнение платежа через Square: сумма {amount}")

    def log_payment(self, amount):
        print(f"Логирование платежа через Square: сумма {amount}")


def main():
    amount = 100

    paypal_processor = PayPalProcessor()
    stripe_processor = StripeProcessor()
    square_processor = SquareProcessor()

    print("Обработка платежа через PayPal:")
    paypal_processor.process_payment(amount)

    print("\nОбработка платежа через Stripe:")
    stripe_processor.process_payment(amount)

    print("\nОбработка платежа через Square:")
    square_processor.process_payment(amount)


if __name__ == "__main__":
    main()
