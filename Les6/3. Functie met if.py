Lengte = int(input("wat is jou lengte in centimeters? "))
def lang_genoeg(lengte):
    if Lengte >= 120:
        return "Je bent lang genoeg voor de attractie"
    else:
        return "Je bent helaas niet lang genoeg voor de attractie"

print(lang_genoeg(Lengte))