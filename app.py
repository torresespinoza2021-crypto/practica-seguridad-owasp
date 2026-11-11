app
import hashlib
import hmac
import os


def generar_hash(texto):
    """Genera un resumen SHA-256 de un texto."""
    return hashlib.sha256(
        texto.encode("utf-8")
    ).hexdigest()


def verificar_clave(clave):
    """Compara una clave de forma segura."""
    clave_correcta = os.getenv("CLAVE_APP", "")

    if not clave_correcta:
        return False

    return hmac.compare_digest(
        clave,
        clave_correcta
    )


if __name__ == "__main__":
    print("Sistema de seguridad OWASP")
    print("Hash generado:", generar_hash("prueba"))
