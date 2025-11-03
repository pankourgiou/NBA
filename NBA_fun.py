import random

# NBA Champions from 1985–2024
nba_champions = {
    1985: "Los Angeles Lakers",
    1986: "Boston Celtics",
    1987: "Los Angeles Lakers",
    1988: "Los Angeles Lakers",
    1989: "Detroit Pistons",
    1990: "Detroit Pistons",
    1991: "Chicago Bulls",
    1992: "Chicago Bulls",
    1993: "Chicago Bulls",
    1994: "Houston Rockets",
    1995: "Houston Rockets",
    1996: "Chicago Bulls",
    1997: "Chicago Bulls",
    1998: "Chicago Bulls",
    1999: "San Antonio Spurs",
    2000: "Los Angeles Lakers",
    2001: "Los Angeles Lakers",
    2002: "Los Angeles Lakers",
    2003: "San Antonio Spurs",
    2004: "Detroit Pistons",
    2005: "San Antonio Spurs",
    2006: "Miami Heat",
    2007: "San Antonio Spurs",
    2008: "Boston Celtics",
    2009: "Los Angeles Lakers",
    2010: "Los Angeles Lakers",
    2011: "Dallas Mavericks",
    2012: "Miami Heat",
    2013: "Miami Heat",
    2014: "San Antonio Spurs",
    2015: "Golden State Warriors",
    2016: "Cleveland Cavaliers",
    2017: "Golden State Warriors",
    2018: "Golden State Warriors",
    2019: "Toronto Raptors",
    2020: "Los Angeles Lakers",
    2021: "Milwaukee Bucks",
    2022: "Golden State Warriors",
    2023: "Denver Nuggets",
    2024: "Boston Celtics"
}

# Perfume and cocktail ideas by team vibe
vibes = {
    "Los Angeles Lakers": {
        "perfumes": ["Dior Sauvage", "Tom Ford Black Orchid", "Le Labo Santal 33"],
        "cocktails": ["Margarita", "Champagne Cocktail", "Mai Tai"]
    },
    "Boston Celtics": {
        "perfumes": ["Chanel Bleu de Chanel", "Creed Green Irish Tweed", "Burberry London"],
        "cocktails": ["Irish Whiskey Sour", "Old Fashioned", "Irish Coffee"]
    },
    "Chicago Bulls": {
        "perfumes": ["Versace Eros", "Armani Code", "YSL Y Eau de Parfum"],
        "cocktails": ["Negroni", "Bloody Mary", "Manhattan"]
    },
    "Detroit Pistons": {
        "perfumes": ["Paco Rabanne Invictus", "Diesel Only The Brave", "Azzaro Wanted"],
        "cocktails": ["Whiskey Sour", "Rusty Nail", "Long Island Iced Tea"]
    },
    "Houston Rockets": {
        "perfumes": ["Jean Paul Gaultier Le Male", "Mugler A*Men", "Spicebomb by Viktor&Rolf"],
        "cocktails": ["Tequila Sunrise", "Cosmopolitan", "Bloody Mary"]
    },
    "San Antonio Spurs": {
        "perfumes": ["Hermès Terre d’Hermès", "Guerlain Vetiver", "Prada L’Homme"],
        "cocktails": ["Gin & Tonic", "Mojito", "Caipirinha"]
    },
    "Miami Heat": {
        "perfumes": ["Dolce & Gabbana Light Blue", "Acqua di Gio", "Creed Aventus"],
        "cocktails": ["Mojito", "Pina Colada", "Cuba Libre"]
    },
    "Dallas Mavericks": {
        "perfumes": ["Bleu de Chanel", "Montblanc Explorer", "Gucci Guilty"],
        "cocktails": ["Texas Mule", "Whiskey Smash", "Gin Rickey"]
    },
    "Golden State Warriors": {
        "perfumes": ["Maison Margiela Jazz Club", "Chanel Allure Homme Sport", "Dior Homme Intense"],
        "cocktails": ["Espresso Martini", "Paloma", "Gin Fizz"]
    },
    "Cleveland Cavaliers": {
        "perfumes": ["YSL La Nuit de L’Homme", "Givenchy Gentleman", "Armani Stronger With You"],
        "cocktails": ["Manhattan", "Black Russian", "Old Fashioned"]
    },
    "Toronto Raptors": {
        "perfumes": ["Creed Aventus", "Maison Francis Kurkdjian Baccarat Rouge 540", "Montale Intense Café"],
        "cocktails": ["Maple Old Fashioned", "Bloody Caesar", "Vodka Cranberry"]
    },
    "Milwaukee Bucks": {
        "perfumes": ["Burberry Hero", "Montblanc Legend", "Loewe Esencia"],
        "cocktails": ["Brandy Old Fashioned", "Beer Cocktail", "Whiskey Smash"]
    },
    "Denver Nuggets": {
        "perfumes": ["Ermenegildo Zegna Uomo", "Coach for Men", "John Varvatos Artisan"],
        "cocktails": ["Colorado Bulldog", "Whiskey Sour", "Mountain Mule"]
    }
}

# NBA legends list
nba_legends = [
    "John Stockton & Steve Kerr",
    "Toni Kukoc & Gary Payton",
    "Michael Jordan & Charles Barkley",
    "Scottie Pippen & Karl Malone",
    "Patrick Ewing & Dennis Rodman",
    "Shaquille O’Neal & Tim Duncan",
    "David Robinson & Hakeem Olajuwon",
    "Shawn Kemp"
]

# --- Interactive Program ---
print("🏀 Welcome to the NBA Champions Perfume & Cocktail Recommender! 🍸\n")

user_input = input("Enter a year between 1985 and 2024: ")

# Check if user entered a valid year
if user_input.isdigit():
    year = int(user_input)
    if year in nba_champions:
        team = nba_champions[year]
        vibe = vibes.get(team)
        perfume = random.choice(vibe["perfumes"])
        cocktail = random.choice(vibe["cocktails"])
        print(f"\n🏆 The {year} NBA Champion was the {team}!")
        print(f"💐 Perfume recommendation: {perfume}")
        print(f"🍹 Cocktail pairing: {cocktail}")
        print("\nStay stylish and hydrated like a true champion! ✨")
    else:
        # Invalid numeric but not in range
        print("\n🎸 Listen to Foo Fighters and drink a ‘Rock the Barrel’!")
        print("Here are some NBA legends you can always trust on the court:\n")
        for duo in nba_legends:
            print(f"🏀 {duo}")
else:
    # Not even a number
    print("\n🎸 Listen to Foo Fighters and drink a ‘Rock the Barrel’!")
    print("Here are some NBA legends you can always trust on the court:\n")
    for duo in nba_legends:
        print(f"🏀 {duo}")
