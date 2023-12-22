
# emotions
# memory
# experience
# skills
# race
# identity

# memory affects the brain activity,
# brain keeps slight attention

# go through each agent and calculate what their next move will be (DO NOT ACTUALLY DO IT)
# after that, go through and do each action, if attacking, see who has faster speed, etc, and calculating combat that way.

class Emotions:
	'''https://www.oysterenglish.com/emotions-vocabulary.html'''
	AFRAID = 0
	AMUSED = 1
	ANGRY = 2
	ANNOYED = 3
	APPALED = 4
	ASTONISHED = 5
	AWE = 6
	BORED = 7
	BROODING = 8
	COMBATATIVE = 9
	COMPOSED = 10
	CONFUSED = 11
	CURIOUS = 12
	CONTENTED = 13
	DELIGHTED = 14
	DEPRESSED = 15
	DETERMINED = 16
	DISAPPOINTED = 17
	DISGUST = 18
	EXHAUSTED = 19
	EXHILIRATED = 20
	GRATEFUL = 21
	HAPPY = 22
	HATE = 23
	HYSTERICAL = 24
	HOPEFUL = 25
	INDIGNANT = 26
	LOATHING = 27
	MODEST = 28
	SAD = 29
	SATISFIED = 30
	SERENE = 31
	SHY = 32
	SNEAKY = 33
	SILLY = 34
	SURPRISED = 35
	WEEPY = 36
	WITHDRAWN = 37
	WONDER = 38

class Personality:
	'''https://www.16personalities.com/articles/our-theory'''

	class Types:
		NEUTRAL = 0
		ENERGETIC = 1
		MIND = 2
		NATURE = 3
		TACTICS = 4
		IDENTITY = 5

	class Energy:
		NEUTRAL = 0
		INTROVERTED = 1
		EXTRAVERTED = 2

	class Mind:
		NEUTRAL = 0
		OBSERVANT = 1
		INTUITIVE = 2

	class Nature:
		NEUTRAL = 0
		THINKING = 1
		FEELING = 2

	class Tactics:
		NEUTRAL = 0
		JUDGING = 1
		PROSPECTING = 2

	class Identity:
		TURBULENT = 0
		ASSERTIVE = 1

# class Disorders:

# 	class Personality:
# 		EXTREMIST = 0
# 		SUPREMIST = 1

# 	class ActiveTraits:
# 		IMPULSIVE = 0

# 	class PassiveTraits:
# 		CRAZY = 0
# 		IMPULSIVE = 1

class Relationship:
	FAMILY = 0
	REMARRIED = 1
	WIDOW = 2
	MARRIED = 3
	ENGAGED = 4
	DATING = 5
	CLOSE_FRIEND = 6
	FRIEND = 7
	ACQUAINTANCE = 8
	STRANGER = 9

class EventType:
	DEATH = 0
	FIRST_TIME = 1
	FIRST_MEET = 2
	PHYSICAL_EVENT = 3

class DeathType:
	DROWNED = 0
	PASSED_AWAY = 1
	SUFFOCATED = 2
	BURNED = 3

class SocialStatus:
	LEADER = 0
	CITIZEN = 1

class SkillRole:
	LEADER = 1
	MINER = 2
	CARPENTER = 3
	HUNTER = 4
	TEXTILE = 5

class EmotionValues:
	ENVIRONMENTALIST = 0
	PRODUCTIVITIST = 1
	PASSIVIST = 2
	CORRUPTIVIST = 3
