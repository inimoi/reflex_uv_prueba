import sys
import os

# Añadir el root del proyecto al path para poder importar reflex_uv
sys.path.append(os.getcwd())

try:
    from reflex_uv.api.auth import Register
    from pydantic import ValidationError
except ImportError as e:
    print(f"Error: No se pudo importar el modelo Register. Asegúrate de ejecutar este script desde la raíz del proyecto.")
    print(f"Detalle: {e}")
    sys.exit(1)

def test_validation():
    print("--- Iniciando validación de reglas de registro ---")
    
    test_cases = [
        {
            "name": "Password sin número",
            "data": {"email": "test@example.com", "password": "SoloLetras", "name": "UsuarioValido"},
            "should_pass": False,
            "error_hint": "un número"
        },
        {
            "name": "Password sin mayúscula",
            "data": {"email": "test@example.com", "password": "solo1letras", "name": "UsuarioValido"},
            "should_pass": False,
            "error_hint": "mayúscula"
        },
        {
            "name": "Nombre corto (< 5)",
            "data": {"email": "test@example.com", "password": "Password123", "name": "User"},
            "should_pass": False,
            "error_hint": "5 characters"
        },
        {
            "name": "Password corto (< 8)",
            "data": {"email": "test@example.com", "password": "Pas1", "name": "UsuarioValido"},
            "should_pass": False,
            "error_hint": "8 characters"
        },
        {
            "name": "Caso Válido",
            "data": {"email": "valido@example.com", "password": "Password123", "name": "UsuarioValido"},
            "should_pass": True,
            "error_hint": ""
        }
    ]

    total = len(test_cases)
    passed = 0

    for case in test_cases:
        try:
            Register(**case["data"])
            if case["should_pass"]:
                print(f"✅ {case['name']}: Pasó (Correcto)")
                passed += 1
            else:
                print(f"❌ {case['name']}: Debería haber fallado pero pasó")
        except ValidationError as e:
            msg = str(e)
            if not case["should_pass"]:
                if case["error_hint"].lower() in msg.lower():
                    print(f"✅ {case['name']}: Falló correctamente con error: {case['error_hint']}")
                    passed += 1
                else:
                    print(f"❌ {case['name']}: Falló pero con un error inesperado: {msg}")
            else:
                print(f"❌ {case['name']}: Debería haber pasado pero falló: {msg}")

    print(f"\nResultado final: {passed}/{total} tests pasados.")

if __name__ == "__main__":
    test_validation()
