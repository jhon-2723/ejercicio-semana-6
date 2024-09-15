import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = string.punctuation

    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiales)
    ]
    caracteres_restantes = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    contraseña += random.choices(caracteres_restantes, k=longitud - 4)

    random.shuffle(contraseña)

    return ''.join(contraseña)

longitud = 12  
contraseña_segura = generar_contraseña(longitud)
print("Contraseña segura generada:", contraseña_segura)
