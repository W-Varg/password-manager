from crypto import derive_key, encrypt_password, decrypt_password
from database import init_db, save_password, get_passwords, delete_password
import os
import getpass

def main():
    init_db()
    master_password = getpass.getpass("Ingrese su contraseña maestra: ")
    
    while True:
        print("\n--- Gestor de Contraseñas ---")
        print("1. Agregar nueva contraseña")
        print("2. Ver todas las contraseñas")
        print("3. Recuperar contraseña")
        print("4. Eliminar contraseña")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            service = input("Servicio: ")
            username = input("Usuario: ")
            password = getpass.getpass("Contraseña: ")
            salt = os.urandom(16)
            key = derive_key(master_password, salt)
            encrypted = encrypt_password(key, password)
            save_password(service, username, encrypted, salt.hex())
            print("Contraseña guardada exitosamente.")
            
        elif choice == "2":
            passwords = get_passwords()
            for pwd in passwords:
                print(f"{pwd[0]}. {pwd[1]} - {pwd[2]}")
                
        elif choice == "3":
            password_id = input("ID de la contraseña a recuperar: ")
            passwords = get_passwords()
            for pwd in passwords:
                if str(pwd[0]) == password_id:
                    salt = bytes.fromhex(pwd[4])
                    key = derive_key(master_password, salt)
                    decrypted = decrypt_password(key, pwd[3])
                    print(f"Contraseña: {decrypted}")
                    break
                    
        elif choice == "4":
            password_id = input("ID de la contraseña a eliminar: ")
            delete_password(password_id)
            print("Contraseña eliminada.")
            
        elif choice == "5":
            break

if __name__ == "__main__":
    main()