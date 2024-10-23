import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
			"shields": 100, 
			"weapons": 100, 
			"engines": 100, 
			"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000,
			"credits": 100, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 


def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	simFlag = True
	while simFlag: 
		display_status()
		
		actionFlag = True
		while actionFlag:
			action = get_user_action() 
			actionFlag = False
			if action == "1": 
				score += run_mission() 
			elif action == "2": 
				repair_system() 
			elif action == "3": 
				add_crew_member() 
			elif action == "4": 
				print(f"Simulation ended. Final score: {score}")
				simFlag = False
			else: 
				print("Invalid action. Please try again.")
				actionFlag = True
			
		turns += 1
		handle_random_event() 

		if turns % 3 == 0: 
			replenish_resources() 


def display_status():
	print("\n======== SHIP STATUS ========")
	print(f"systems:\n {ship["systems"]}")
	print(f"resources:\n {ship["resources"]}")
	print(f"crew:\n {ship["crew"]}\n")

# TODO: Implement function to display ship status, resources, and crew 


def get_user_action():
	userAction = input("action (1:mission, 2:repair, 3:crew, 4:end): ")
	return userAction

# TODO: Implement function to get and return user's chosen action 


def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}")


	## testing
	ship["systems"]["shields"] -= 20
	missionScore = 222

	return missionScore
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 
	# transfer energy to system to repair
	choiceFlag = True
	while choiceFlag:
		systemToRepair = int(input(f"system to repair (1:shields, 2:weapons, 3:engines, 4:sensors, 5:all, 6:none): "))
		choiceFlag = False
		if systemToRepair == 1:
			ship["resources"]["energy"] -= (100-ship["systems"]["shields"])
			ship["systems"]["shields"] = 100
			print("shields repaired")
		elif systemToRepair == 2:
			ship["resources"]["energy"] -= (100-ship["systems"]["weapons"])
			ship["systems"]["weapons"] = 100
			print("weapons repaired")
		elif systemToRepair == 3:
			ship["resources"]["energy"] -= (100-ship["systems"]["engines"])
			ship["systems"]["engines"] = 100
			print("engines repaired")
		elif systemToRepair == 4:
			ship["resources"]["energy"] -= (100-ship["systems"]["sensors"])
			ship["systems"]["sensors"] = 100
			print("sensors repaired")
		elif systemToRepair == 5:
			ship["resources"]["energy"] -= (100-ship["systems"]["shields"])
			ship["systems"]["shields"] = 100
			ship["resources"]["energy"] -= (100-ship["systems"]["weapons"])
			ship["systems"]["weapons"] = 100
			ship["resources"]["energy"] -= (100-ship["systems"]["engines"])
			ship["systems"]["engines"] = 100
			ship["resources"]["energy"] -= (100-ship["systems"]["sensors"])
			ship["systems"]["sensors"] = 100
			print("All systems repaired")
		elif systemToRepair == 6:
			print("No system repaired")
		else:
			print("Invalid response: ")
			choiceFlag = True

# TODO: Implement system repair functionality
 
def add_crew_member():
	crewAddFlag = True
	while crewAddFlag:
		crewType = int(input("input crew type (1: command, 2: operations, 3:sciences): "))
		crewName = input("input crew name:")
		crewAddFlag = False
		if crewType == 1:
			ship["crew"] += crewName
			print("crew member added")
		if crewType == 2:
			ship["crew"] += crewName
			print("crew member added")
		if crewType == 3:
			ship["crew"] += crewName
			print("crew member added")
		else:
			print("Invalid crew role")
			crewAddFlag = True


	# command, operations, sciences
# TODO: Implement functionality to add a new crew member 

def handle_random_event():
	EVENTS = ("event1 etc")
	pass
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount):
	pass
# TODO: Implement resource usage logic 

def replenish_resources():
	pass
# TODO: Implement resource replenishment logic 

main()
