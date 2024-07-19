from abc import ABC, abstractmethod
import requests


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class CreateUserCommand(Command):
    def __init__(self, receiver, user):
        self.receiver = receiver
        self.user = user
        self.user_id = None

    def execute(self):
        response = self.receiver.create_user(self.user)
        if response.status_code == 201:
            self.user_id = response.json()['id']
            print(f"User created with ID: {self.user_id}")

    def undo(self):
        if self.user_id:
            self.receiver.delete_user(self.user_id)
            print(f"User with ID: {self.user_id} deleted")

class UpdateUserCommand(Command):
    def __init__(self, receiver, user_id, new_data):
        self.receiver = receiver
        self.user_id = user_id
        self.new_data = new_data
        self.old_data = None

    def execute(self):
        response = self.receiver.get_user(self.user_id)
        if response.status_code == 200:
            self.old_data = response.json()
            self.receiver.update_user(self.user_id, self.new_data)
            print(f"User with ID: {self.user_id} updated")

    def undo(self):
        if self.old_data:
            self.receiver.update_user(self.user_id, self.old_data)
            print(f"User with ID: {self.user_id} restored to old data")

class DeleteUserCommand(Command):
    def __init__(self, receiver, user_id):
        self.receiver = receiver
        self.user_id = user_id
        self.deleted_data = None

    def execute(self):
        response = self.receiver.get_user(self.user_id)
        if response.status_code == 200:
            self.deleted_data = response.json()
            self.receiver.delete_user(self.user_id)
            print(f"User with ID: {self.user_id} deleted")

    def undo(self):
        if self.deleted_data:
            self.receiver.create_user(self.deleted_data)
            print(f"User with ID: {self.user_id} restored")

class UserManagerAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, user):
        return requests.post(f"{self.base_url}/users", json=user)

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def update_user(self, user_id, user_data):
        return requests.put(f"{self.base_url}/users/{user_id}", json=user_data)

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}")


class UserInvoker:
    def __init__(self):
        self._commands = []
        self._undone_commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
            self._undone_commands.append(command)
        self._commands = []

    def undo_last_command(self):
        if self._undone_commands:
            command = self._undone_commands.pop()
            command.undo()

if __name__ == "__main__":
    api = UserManagerAPI("http://localhost:5000")
    invoker = UserInvoker()

    user1 = {"name": "John Doe", "email": "example@gmail.com"}
    user2 = {"name": "Jane Doe", "email": "example1@gmail.com"}

    create_user1 = CreateUserCommand(api, user1)
    create_user2 = CreateUserCommand(api, user2)
    update_user1 = UpdateUserCommand(api, 1, {"name": "John Smith"})
    delete_user2 = DeleteUserCommand(api, 2)
    
    invoker.store_command(create_user1)
    invoker.store_command(create_user2)
    invoker.store_command(update_user1)
    invoker.store_command(delete_user2)

    invoker.execute_commands()
    invoker.undo_last_command()