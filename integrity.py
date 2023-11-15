import os
from hasher import Hasher

class DirIntegrity:
    def generate_integrity_file(self, dir_path: str, result_path: str):
        hasher = Hasher()
        complete_file_paths = []

        for (dirpath, dirnames, filenames) in os.walk(dir_path):
            file_paths = [f'{dirpath}\\{filename}' for filename in filenames]
            complete_file_paths.extend(file_paths)

        with open(result_path, 'w') as result_file:
            for complete_file_path in complete_file_paths:
                complete_file_path = complete_file_path

                digest = hasher.hash_file(complete_file_path, 'sha256')
                text = f'{complete_file_path} : {digest}\n'

                result_file.write(text)

    def check_integrity(self, integrity_path: str, result_path: str):
        hasher = Hasher()

        with open(integrity_path, 'r') as integrity_file:
            buffer = integrity_file.read()

            values = buffer.split('\n')[:-1]
            values = [value.split(' : ') for value in values]

            with open(result_path, 'w') as result_file:
                for complete_file_path, digest in values:
                    new_digest = hasher.hash_file(complete_file_path, 'sha256')

                    text = ''

                    text += f'PATH: {complete_file_path}\n'
                    text += f'OLD: {digest}\n'
                    text += f'NEW: {new_digest}\n'

                    if new_digest == digest:
                        text += f'RESULT: INTACT\n'
                    else:
                        text += f'RESULT: MODIFIED\n'

                    text += '\n'

                    result_file.write(text)
