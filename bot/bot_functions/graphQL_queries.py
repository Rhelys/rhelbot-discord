# graphQL_queries.py
# Storing the graphQL queries separate from the rest of the bot's code

def allstar (character_name, ff_server):
    all_star_query = """query {characterData {character(name: "{character_name}", serverSlug: "{ff_server}", serverRegion: "NA") {name, hidden, canonicalID, zoneRankings}}""".format(character_name, ff_server)


    return all_star_query
