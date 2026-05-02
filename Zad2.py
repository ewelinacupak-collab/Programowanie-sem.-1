def funkcja(name: str, email: str, **kwargs):
    if not isinstance(name, str):
        raise ValueError("imie musi być stringi'em")

    if not name.strip():
        raise ValueError("imie nie może być puste")

    if not isinstance(email, str):
        raise ValueError("email musi być stringi'em")

    if not email.strip():
        raise ValueError("email nie może być pusty")

    if len(kwargs) < 3:
        raise ValueError("Musisz podać co najmniej 3 dodatkowe informacje")


    profile = {
        "name": name,
        "email": email
    }
    profile.update(kwargs)

    return profile

print(funkcja("Przemek", "ewelina@gmail", wiek = 20, adres = "Rzeszów", ulubiony_kolor = "czerwony"))
