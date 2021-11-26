def f(x,y):
    return (1/2)*(x) ** 2 + (7/2)*(y) ** 2


def df(x,y):

    return (x,7*y)


def descente1(f, df, a,b, alpha=0.1940299, eps=10e-10, maxIter=1000):
    # Recherche le minimum d'une fonction f par descente de gradient
    # df doit être la dérivée de f
    # a est la valeur initiale
    # alpha est le taux d'apprentissage qui détermine la rapidité de la descente (par défaut 1/100)
    # eps est la précision souhaitée (par défaut 1/1000000000)
    # maxIter est le nombre maximum d'itération (par défaut 1000)

    grad = df(a,b)
    i = 0
    while abs(grad[0]) > eps and abs(grad[1]) > eps:  # tant que la pente n'est pas approximativement nulle
        grad = df(a, b) # on calcule la pente
        alpha = (a**2 + (7**2)*b**2)/(a**2+(7**3)*b**2 )
        a = a - alpha * grad[0]  # on effectue un petit pas vers le bas
        b = b - alpha * grad[1]
        i += 1
        print(i, a,b ,grad) # décommenter cette ligne pour imprimer les itérations
        if i > maxIter:
            return None  # on abandonne si le nombre d'itérations est trop élevé
    return a



print(descente1(f, df, 7,1.5))



