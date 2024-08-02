import re

def decrypt_message(message, key_count):
    decrypted_message = ''.join(chr(ord(c) - key_count) for c in message)
    return decrypted_message

def extract_information(decrypted_message):
    pattern = r'@(?P<name>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<attack_type>[AD])![^@\-!:>]*->(?P<soldier_count>\d+)'
    match = re.search(pattern, decrypted_message)
    if match:
        return match.group('name'), int(match.group('population')), match.group('attack_type'), int(match.group('soldier_count'))
    return None

def star_enigma(n, messages):
    attacked_planets = []
    destroyed_planets = []

    for message in messages:
        key_count = sum(message.lower().count(ch) for ch in 'star')
        decrypted_message = decrypt_message(message, key_count)
        info = extract_information(decrypted_message)
        if info:
            name, population, attack_type, soldier_count = info
            if attack_type == 'A':
                attacked_planets.append(name)
            elif attack_type == 'D':
                destroyed_planets.append(name)

    attacked_planets.sort()
    destroyed_planets.sort()

    print(f"Attacked planets: {len(attacked_planets)}")
    for planet in attacked_planets:
        print(f"-> {planet}")

    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planet in destroyed_planets:
        print(f"-> {planet}")

n = int(input())
messages = [input() for _ in range(n)]
star_enigma(n, messages)
