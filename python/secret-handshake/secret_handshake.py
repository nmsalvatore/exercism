movements = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(binary_str):
    secret_handshake = []
    
    reverse_binary_str = binary_str[::-1]
    for index, movement in enumerate(movements):
        bit = int(reverse_binary_str[index])
        if bit & 1:
            secret_handshake.append(movement)
    
    msb = int(binary_str[0])
    if msb & 1:
        secret_handshake.reverse()
        
    return secret_handshake
