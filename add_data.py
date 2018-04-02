import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS BlueCheese (mood TEXT, url TEXT, file_id TEXT, caption TEXT)")

def add(mood, url, file_id, caption):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO BlueCheese (mood, url, file_id, caption) VALUES (?,?,?,?)",
              (mood, url, file_id, caption))
    conn.commit()
    c.close()
    conn.close()



# create_table()

add("Fresh Tunes",
    "https://itunes.apple.com/ru/playlist/urban-vibes/pl.0a6e08e1248a441284c3eb5a355adfc6?l=en",
    "AgADAgAD_6cxG3ELKUgZPsTzNvG3TYfCDw4ABAN1KgPtW4gJzsQCAAEC",
    "Playlist")

add("Fresh Tunes",
    "https://itunes.apple.com/ru/playlist/new-hip-hop/pl.4355fef8c209446f82fe6fdf9fa97e03?l=en",
    "AgADAgAEqDEbcQspSKwMIDi7gIsmwsUPDgAEmW8z883ZMAnLwAIAAQI",
    "Playlist")

add("Essentials",
    "https://itunes.apple.com/ru/playlist/chill/pl.6d2f03aab577450cb9f357f63020f7a3?l=en",
    "AgADAgADiqgxG3ELIUgzNG0rKMyElCQWSw0ABPvjY1ajkkJN2MgRAAEC",
    "Playlist")

add("Essentials",
    "https://itunes.apple.com/ru/playlist/mood/pl.daa2a689923d4562bf5650a96809f929?l=en",
    "AgADAgADi6gxG3ELIUjV-epUrFpYulgYMw4ABDwY-GMpHR1ofWcAAgI",
    "Playlist")

add("Essentials",
    "https://itunes.apple.com/ru/playlist/late-night-hip-hop/pl.c15a5391c65e44759efc3083463f88c4?l=en",
    "AgADAgADAagxG3ELKUik62c-KGM8FwYxSw0ABBHtf-EagwUbxNkRAAEC",
    "Playlist")

add("Essentials",
    "https://itunes.apple.com/ru/playlist/onrepeat/pl.426a1044619f47d6b1f86b3f79ecf857?l=en",
    "AgADAgADAqgxG3ELKUh8ZKtOfe0rYcIaMw4ABGOFUItGU30tCWsAAgI",
    "Playlist")

add("Chill",
    "https://itunes.apple.com/ru/album/88glam/1308490281?l=en",
    "AgADAgADwKgxG4S8GEg62sqbtY3uyijPDw4ABI5eLSFTYLyXJcACAAEC",
    "88GLAM - 88GLAM")

add("Chill",
    "https://itunes.apple.com/ru/album/stoney-deluxe/1170616610?l=en",
    "AgADAgADwagxG4S8GEhbhRYoC-HKugUIMw4ABE_uIIFNvSQ3H2EAAgI",
    "Post Malone - Stoney")

add("Chill",
    "https://itunes.apple.com/ru/album/welcome-to-gazi/1118065829?l=en",
    "AgADAgADwqgxG4S8GEjaczKYtIh2Pn0OMw4ABI2Pf79lDv-fIWIAAgI",
    "A.CHAL - Welcome to GAZI")

add("Chill",
    "https://itunes.apple.com/ru/album/blonde/1146195596?l=en",
    "AgADAgADxagxG4S8GEiNbTq6U3jKnCQ7Sw0ABEtuOO9B2CxhetoRAAEC",
    "Frank Ocean - Blonde")

add("Chill",
    "https://itunes.apple.com/ru/album/lil-boat/1130017345?l=en",
    "AgADAgADw6gxG4S8GEgx4Di9V7xwcjv-Mg4ABCwZXaMSS8K4zGAAAgI",
    "Lil Yachty - Lil Boat")

add("Chill",
    "https://itunes.apple.com/ru/album/worlds/886037928?l=en",
    "AgADAgADxKgxG4S8GEiD5TyUisfvKNLaDw4ABOUErDdmaJt50cECAAEC",
    "Porter Robinson - Worlds")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/issa-album/1254351754?l=en",
    "AgADAgADxqgxG4S8GEgFH-YR1QkdhhLODw4ABHGTF7rVjx9MhL0CAAEC",
    "21 Savage - Issa Album")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/birds-in-the-trap-sing-mcknight/1150135681?l=en",
    "AgADAgADx6gxG4S8GEiPb3HCf_QFkIkAATMOAAR-1J-Jh-tGjbRgAAIC",
    "Travis Scott - Birds in the Trap Sing McKnight")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/damn/1223618217?l=en",
    "AgADAgADyKgxG4S8GEjyxuafRAmREyvNDw4ABD_4VF4gy19HcL8CAAEC",
    "Kendrick Lamar - DAMN.")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/still-striving/1266713355?l=en",
    "AgADAgADBKgxG3ELKUigHYANxgP-XO_BDw4ABGIJsWJfQQahvsYCAAEC",
    "A$AP Ferg - Still Striving")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/at-long-last-a%24ap/994727168?l=en",
    "AgADAgADBagxG3ELKUg0YO9ORtd-rjMcMw4ABFbMeVPQKum4gmoAAgI",
    "A$AP Rocky - AT.LONG.LAST.A$AP")

add("All The Way Up",
    "https://itunes.apple.com/ru/album/more-life/1216996902?l=en",
    "AgADAgADA6gxG3ELKUhwirTDO8N3WmsKMw4ABGcPj8CwkPr332kAAgI",
    "Drake - More Life")
