from app import generar_hash, verificar_clave


def test_generar_hash():
    resultado = generar_hash("hola")
    assert len(resultado) == 64


def test_hash_repetido():
    assert generar_hash("hola") == generar_hash("hola")


def test_clave_correcta(monkeypatch):
    monkeypatch.setenv("CLAVE_APP", "clave123")
    assert verificar_clave("clave123") is True


def test_clave_incorrecta(monkeypatch):
    monkeypatch.setenv("CLAVE_APP", "clave123")
    assert verificar_clave("incorrecta") is False
