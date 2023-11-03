import base64
import json
import zlib

class HealthcareDataTransfer:
    def __init__(self, sender, message_file):
        self.sender = sender
        self.message_file = message_file

    def read_message(self):
        with open(self.message_file, 'r', buffering=5) as file:
            return file.read()

    def write_received_message(self, received_message):
        with open('received_message.txt', 'w', buffering=5) as file:
            file.write(received_message)

    def encode_data(self, data):
        return base64.b64encode(data.encode('utf-8'))

    def decode_data(self, encoded_data):
        return base64.b64decode(encoded_data).decode('utf-8')


    def compress_data(self, data):
        return zlib.compress(data)

    def decompress_data(self, compressed_data):
        return zlib.decompress(compressed_data)

    def add_signature(self, data):
        return f'{data}\n--- Signed by {self.sender} ---'

    def transmit(self):
        message = self.read_message()
        signed_message = self.add_signature(message)
        encoded_data = self.encode_data(signed_message)
        compressed_data = self.compress_data(encoded_data)
        return compressed_data

    def receive(self, compressed_data):
        decompressed_data = self.decompress_data(compressed_data)
        decoded_data = self.decode_data(decompressed_data)
        received_message = self.extract_message(decoded_data)
        self.write_received_message(received_message)
        return received_message

    def extract_message(self, data):
        lines = data.split('\n')
        return '\n'.join(lines[:-2])


if __name__ == '__main__':
    sender = 'Doctor'
    patient_record = {
        'patient_id': 'P12345',
        'name': 'Patient',
        'dob': '21-07-2003',
        'diagnosis': 'Insomnia',
        'medications': ['Medication A', 'Medication B'],
        'doctor': 'Doctor'
    }
    message_file = 'patient_message.txt'

    # Convert patient record to JSON format
    json_record = json.dumps(patient_record)

    # Create an instance of HealthcareDataTransfer
    data_transfer = HealthcareDataTransfer(sender, message_file)

    # Transmit data
    compressed_data = data_transfer.transmit()

    # Receive and decode data
    received_message = data_transfer.receive(compressed_data)

    # Print original and received message
    print('Original Message:')
    print(data_transfer.read_message())
    print('\nReceived Message:')
    print(received_message)
