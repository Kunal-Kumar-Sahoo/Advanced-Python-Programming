class FileError(Exception):
    def __init__(self, filename, operation, message):
        self.filename = filename
        self.operation = operation
        self.message = message
        super().__init__(self.message)

class FileReadError(FileError):
    def __init__(self, filename, message='Error reading file'):
        super().__init__(filename, 'read', message)

class FileWriteError(FileError):
    def __init__(self, filename, message='Error writing file'):
        super().__init__(filename, 'write', message)

class FileTransferError(FileError):
    def __init__(self, filename, destination, message='Error transferring file'):
        self.destination = destination
        super().__init__(filename, 'transfer', message)

class WhatsAppMessageTransfer:
    def __init__(self, source_account, dest_account):
        self.source_account = source_account
        self.dest_account = dest_account

    def read_chat_messages(self):
        try:
            filename = f'{self.source_account}_chat.txt'
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileReadError(filename, 'Chat file not found')
        except Exception as e:
            raise FileReadError(filename, str(e))

    def transfer_messages(self):
        try:
            messages = self.read_chat_messages()
            dest_filename = f'{self.dest_account}_chat.txt'
            with open(dest_filename, 'w') as file:
                file.write(messages)
        except FileReadError as e:
            raise FileTransferError(e.filename, self.dest_account, e.message)
        except FileWriteError as e:
            raise FileTransferError(e.filename, self.dest_account, e.message)

# Example usage
if __name__ == '__main__':
    source_account = 'user1'
    dest_account = 'user2'

    try:
        transfer = WhatsAppMessageTransfer(source_account, dest_account)
        transfer.transfer_messages()
        print(f'WhatsApp messages from {source_account} transferred to {dest_account}')
    except FileTransferError as e:
        print(f'Error transferring messages: {e.message}')
