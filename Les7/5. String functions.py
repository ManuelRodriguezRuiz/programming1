willekeurig = input('Voer hier een willekeurige zin in:')


def gemiddelde():
    lengte = len(willekeurig.replace(' ', ''))
    woorden = len(willekeurig.split())
    print (int(lengte / woorden))


gemiddelde()