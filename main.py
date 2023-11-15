from integrity import DirIntegrity

def main():
    dir_path = r'C:\Users\Gustavo\Desktop\segurancaPUCCopia'
    integrity_path = r'C:\Users\Gustavo\Desktop\integrity.int'
    result_path = r'C:\Users\Gustavo\Desktop\result.int'

    dir_int = DirIntegrity()

    # dir_int.generate_integrity_file(dir_path, integrity_path)
    dir_int.check_integrity(integrity_path, result_path)

if __name__ == '__main__':
    main()