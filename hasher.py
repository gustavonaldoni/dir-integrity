import hashlib

class Hasher:
    def hash_text(self, text: bytes, algorithm: str) -> str:
        correct_algorithm = None

        match algorithm:
            case 'sha256':
                correct_algorithm = hashlib.sha256()
            
            case 'sha512':
                correct_algorithm = hashlib.sha512()

            case 'md5':
                correct_algorithm = hashlib.md5()
        
        correct_algorithm.update(text)
        return correct_algorithm.hexdigest()

    def hash_file(self, file_path: str, algorithm: str) -> str:
        with open(file_path, 'rb') as file:
            buffer = file.read()

            return self.hash_text(buffer, algorithm)