def calc_alpha(my_str):
    
    vowels = "A, E, I, O, U, Y"
    consonants = "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z"

    vowels_cout = 0
    consonants_count = 0
    simbole_count = 0

    for char in my_str:
        if char.upper() in vowels:
            vowels_cout += 1
        elif char.upper() in consonants:
            consonants_count += 1 
        else:
            simbole_count += 1
    return {
        "vowels" : vowels_cout,
        "consonants": consonants_count,
        "simbole": simbole_count
        }


print(calc_alpha("Hello! I'm study "))