def validar_email(email):
    # Regra 1: Deve conter exatamente um "@"
    if email.count("@") != 1:
        return "E-mail inválido"
    
    # Regra 2: Não pode começar ou terminar com "@"
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    
    # Regra 3: Não pode conter espaços
    if " " in email:
        return "E-mail inválido"
    
    # Regra 4: Deve conter um domínio após o "@", como gmail.com
    usuario, dominio = email.split("@")
    if "." not in dominio:
        return "E-mail inválido"
    
    return "E-mail válido"


# Leitura da entrada
email = input()
print(validar_email(email))