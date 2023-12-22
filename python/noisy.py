
from dataclasses import dataclass
from noise import snoise2
from random import randint

@dataclass
class NoiseParameters:
	scale : int | float = 0.5
	octaves : int = 6
	persistence : int | float = 0.5
	lacunarity : int | float = 2.0
	repeat_x : int = 1024
	repeat_y : int = 1024
	seed : int = -1

DEFAULT_NOISE_PARAMETERS = NoiseParameters()

def generate_noise( x : float | int, y : float | int, parameters : NoiseParameters = DEFAULT_NOISE_PARAMETERS ) -> float:
	return snoise2(
		x/parameters.scale,
		y/parameters.scale,
		octaves=parameters.octaves,
		persistence=parameters.persistence,
		lacunarity=parameters.lacunarity,
		repeatx=parameters.repeat_x,
		repeaty=parameters.repeat_y,
		base=(parameters.seed == -1 and randint(1, 32768) or parameters.seed)
	)

def generate_noisemap( ox : int | float, oy : int | float, width : int, height : int, parameters : NoiseParameters ) -> list[list[float]]:
	noisemap = []
	for x in range( width ):
		inner_map = [ generate_noise( ox + x, oy + y, parameters ) for y in range(height) ]
		noisemap.append( inner_map )
	return noisemap
