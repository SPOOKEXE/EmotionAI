
from dataclasses import dataclass
from noisy import generate_noise, generate_noisemap, NoiseParameters

# class Agent:
# 	pass

@dataclass
class Tile:
	x : int = 0
	y : int = 0
	tile_id : str = 'none'

# class Structure:
# 	pass

# class World:
# 	agent : dict[str, Agent]
# 	structures : dict[str, Structure]
# 	tiles : dict[str, Tile]
