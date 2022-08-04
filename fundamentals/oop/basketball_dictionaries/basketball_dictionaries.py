players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, players_dict):
        self.name = players_dict["name"]
        self.age = players_dict["age"]
        self.position = players_dict["position"]
        self.team = players_dict["team"]
    
    def __repr__(self):
        return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name, self.age, self.position, self.team)

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

# player_kevin = Player(kevin)
# print(player_kevin)

# player_jason = Player(jason)
# print(player_jason)

# player_kyrie = Player(kyrie)
# print(player_kyrie)

#looping through and creating a new list

#for loop over the list of dictionaries
    #each time use that dictionary info 
    #create a new player instance

fantasy_team = []

for player_dict in players:
    player= Player(player_dict)
    fantasy_team.append(player)

print(fantasy_team)

