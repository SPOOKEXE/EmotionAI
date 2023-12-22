
from __future__ import annotations

import pygame
import time

from display import BaseViewport, Colors

from random import randint

class AIViewport(BaseViewport):

	TPS_MICROSTEPS = 4

	def __init__( self, width : int, height : int ) -> AIViewport:
		BaseViewport.__init__( self, width, height )

	def update_title( self ) -> None:
		pygame.display.set_caption(f'FPS: { self.CURRENT_FPS } / { self.TARGET_FPS } | TPS: { self.CURRENT_TPS * self.TPS_MICROSTEPS } / { self.TARGET_TPS * self.TPS_MICROSTEPS } | AGENTS: { 0 }')

	def tick( self ) -> None:
		# sleep( 1 )
		for _ in range( self.TPS_MICROSTEPS ):
			pass
		self.IS_TPS_UPDATING = False

	def render( self ) -> None:
		self.SCREEN.fill( self.BACKGROUND )
		self.SCREEN.fill( Colors.WHITE, pygame.Rect(randint(0, 500), randint(0, 500), 50, 50) )
		pygame.display.flip()
		self.IS_FPS_UPDATING = False

if __name__ == '__main__':

	pygame.display.set_icon( pygame.image.load('docs/hammer_tools_repair_tool_equipment.png') )

	v = AIViewport( 800, 600 )
	v.set_framerate( 60 )
	v.set_tickrate( 60 )
	v.start()
