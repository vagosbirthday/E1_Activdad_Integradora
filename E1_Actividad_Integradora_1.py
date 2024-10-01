def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"Error al abrir el archivo: {nombre_archivo}")
        return ""

def buscar_patron(texto, patron):
    posicion = texto.find(patron)
    return posicion != -1, posicion

def buscar_palindromo_mas_largo(texto):
    n = len(texto)
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    inicio = 0
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if texto[i] == texto[i + 1]:
            dp[i][i + 1] = True
            inicio = i
            max_len = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if texto[i] == texto[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    inicio = i
                    max_len = k
    return inicio + 1, inicio + max_len

def substring_comun_mas_largo(texto1, texto2):
    m, n = len(texto1), len(texto2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    fin = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if texto1[i - 1] == texto2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    fin = i
    return fin - max_len + 1, fin

def main():
    archivos_transmision = ["transmission1.txt", "transmission2.txt"]
    archivos_mcode = ["mcode1.txt", "mcode2.txt", "mcode3.txt"]

    for archivo_transmision in archivos_transmision:
        contenido_transmision = leer_archivo(archivo_transmision)
        for archivo_mcode in archivos_mcode:
            contenido_mcode = leer_archivo(archivo_mcode)
            encontrado, posicion = buscar_patron(contenido_transmision, contenido_mcode)
            if encontrado:
                print(f"true {posicion + 1}")
            else:
                print("false")

    for archivo_transmision in archivos_transmision:
        contenido_transmision = leer_archivo(archivo_transmision)
        inicio, fin = buscar_palindromo_mas_largo(contenido_transmision)
        print(f"{inicio} {fin}")

    contenido_transmision1 = leer_archivo(archivos_transmision[0])
    contenido_transmision2 = leer_archivo(archivos_transmision[1])
    inicio, fin = substring_comun_mas_largo(contenido_transmision1, contenido_transmision2)
    print(f"{inicio} {fin}")

main()