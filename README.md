# 🔐 Password Manager

Un gestor de contraseñas seguro desarrollado en Python que utiliza criptografía moderna para proteger tus credenciales.

## 📋 Descripción

Este gestor de contraseñas permite almacenar de forma segura credenciales de diferentes servicios utilizando:
- **Cifrado AES-128** con Fernet
- **Derivación de claves** segura con PBKDF2 + SHA256
- **Salt único** para cada contraseña almacenada
- **100,000 iteraciones** para resistir ataques de fuerza bruta
- **Base de datos SQLite** local

## ✨ Funcionalidades

- ✅ **Crear** nuevas contraseñas para servicios
- ✅ **Guardar** contraseñas cifradas de forma segura
- ✅ **Listar** todos los servicios y usuarios guardados
- ✅ **Recuperar** contraseñas específicas mediante descifrado
- ✅ **Eliminar** contraseñas cuando ya no las necesites
- 🔐 **Autenticación** con contraseña maestra
- 🛡️ **Cifrado de extremo a extremo** sin almacenar la clave maestra

## 🔧 Dependencias

```bash
cryptography==38.0.0
```

## 📦 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/W-Varg/password-manager.git
   cd password-manager
   ```

2. **Crear entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # venv\Scripts\activate   # En Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Uso

1. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

2. **Configurar contraseña maestra:**
   - En el primer uso, ingresa una contraseña maestra segura
   - Esta contraseña se utilizará para cifrar/descifrar todas las demás

3. **Menú principal:**
   ```
   --- Gestor de Contraseñas ---
   1. Agregar nueva contraseña
   2. Ver todas las contraseñas
   3. Recuperar contraseña
   4. Eliminar contraseña
   5. Salir
   ```

### Ejemplo de uso:

```bash
$ python main.py
Ingrese su contraseña maestra: ********

--- Gestor de Contraseñas ---
1. Agregar nueva contraseña
2. Ver todas las contraseñas
3. Recuperar contraseña
4. Eliminar contraseña
5. Salir

Seleccione una opción: 1
Servicio: Gmail
Usuario: mi.email@gmail.com
Contraseña: ********
Contraseña guardada exitosamente.
```

## 📁 Estructura del Proyecto

```
password-manager/
├── main.py           # Interfaz principal y lógica de usuario
├── crypto.py         # Funciones de criptografía
├── database.py       # Operaciones con base de datos SQLite
├── requirements.txt  # Dependencias del proyecto
├── README.md         # Este archivo
└── passwords.db      # Base de datos SQLite (se crea automáticamente)
```

## 🔒 Características de Seguridad

- **No almacenamiento de contraseña maestra**: La clave maestra nunca se guarda en disco
- **Salt único por contraseña**: Cada contraseña tiene su propio salt aleatorio
- **Key derivation robusta**: PBKDF2 con 100,000 iteraciones
- **Cifrado simétrico fuerte**: Fernet (AES 128 + HMAC)
- **Base de datos local**: Los datos no salen de tu máquina

## 🛠️ Requisitos del Sistema

- **Python 3.7+**
- **Sistema operativo**: Windows, macOS, o Linux
- **Espacio**: ~10MB para la aplicación y dependencias

## 📋 Módulos

### `crypto.py`
- `derive_key()`: Deriva una clave criptográfica desde la contraseña maestra
- `encrypt_password()`: Cifra una contraseña usando Fernet
- `decrypt_password()`: Descifra una contraseña

### `database.py`
- `init_db()`: Inicializa la base de datos SQLite
- `save_password()`: Guarda una nueva contraseña cifrada
- `get_passwords()`: Recupera todas las contraseñas almacenadas
- `delete_password()`: Elimina una contraseña por ID

### `main.py`
- Interfaz de usuario por consola
- Flujo principal de la aplicación
- Manejo de entrada del usuario

## ⚠️ Advertencias Importantes

1. **Respaldo de la contraseña maestra**: Si olvidas tu contraseña maestra, NO podrás recuperar tus datos
2. **Respaldo de `passwords.db`**: Considera hacer copias de seguridad periódicas
3. **Entorno seguro**: Ejecuta la aplicación en un entorno confiable
4. **Contraseñas fuertes**: Usa una contraseña maestra robusta y única

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y commitea (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto. Consulta el archivo LICENSE para más detalles.

## 👨‍💻 Autor

**W-Varg** - [GitHub](https://github.com/W-Varg)

---

⭐ Si este proyecto te fue útil, ¡considera darle una estrella!
