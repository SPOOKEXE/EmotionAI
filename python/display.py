
from __future__ import annotations

import pygame
import time
import numpy

from pygame.time import Clock
from pygame.font import Font, SysFont
from threading import Thread

class Fonts:
	font_cache : dict[str, Font] = { }
	config : dict[str, str] = { 'freesansbold' : 'freesansbold.ttf' }
	def get_font( self, index : str, size : int ) -> Font:
		assert self.config.get(index) != None, 'Target font does not exist.'
		return SysFont( self.config.get(index), size )
FONTS = Fonts()

class Colors:
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

class BaseViewport:
	WIDTH : int
	HEIGHT : int
	TARGET_FPS : int
	CURRENT_FPS : int
	TARGET_TPS : int
	CURRENT_TPS : int
	TARGET_CPS : int # max( TARGET_FPS, TARGET_TPS )

	BACKGROUND = Colors.BLACK
	SCREEN : pygame.Surface

	CYCLE_CLOCK : Clock

	IS_FPS_UPDATING : bool
	IS_TPS_UPDATING : bool
	NEXT_FPS_UPDATE : float
	NEXT_TPS_UPDATE : float
	LAST_TPS_UPDATE : float
	LAST_FPS_UPDATE : float

	def __init__( self, width : int, height : int ) -> BaseViewport:
		self.set_window_size( width, height )

		self.TARGET_FPS = 60
		self.CURRENT_FPS = 0
		self.TARGET_TPS = 120
		self.CURRENT_TPS = 0

		self.IS_FPS_UPDATING = False
		self.IS_TPS_UPDATING = False
		self.NEXT_FPS_UPDATE = time.time()
		self.NEXT_TPS_UPDATE = time.time()
		self.LAST_FPS_UPDATE = time.time()
		self.LAST_TPS_UPDATE = time.time()
		self.COUNTER_LENGTH = 8
		self.FPS_COUNTERS = [self.TARGET_FPS] * self.COUNTER_LENGTH
		self.TPS_COUNTERS = [self.TARGET_TPS] * self.COUNTER_LENGTH
		self.FPS_BUFF_INDEX = 0
		self.TPS_BUFF_INDEX = 0

		self.CYCLE_CLOCK = Clock()

	def set_window_size( self, width : int, height : int ) -> None:
		self.WIDTH = width
		self.HEIGHT = height
		self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

	def set_framerate( self, framerate : int ) -> None:
		self.TARGET_FPS = framerate

	def set_tickrate( self, tickrate : int ) -> None:
		self.TARGET_TPS = tickrate

	def update_title( self ) -> None:
		pygame.display.set_caption(f'FPS: { self.CURRENT_FPS } / { self.TARGET_FPS } | TPS: { self.CURRENT_TPS } / { self.TARGET_TPS } | AGENTS: { 0 }')

	def tick( self ) -> None:
		'''
		Set IS_TPS_UPDATING to False when completed.
		'''
		raise NotImplementedError

	def render( self ) -> None:
		'''
		Set IS_FPS_UPDATING to False when completed.
		'''
		raise NotImplementedError

	def update( self ) -> None:
		pygame.event.pump()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.RUNNING = False
		current_ns = time.time( )

		if (not self.IS_TPS_UPDATING) and current_ns > self.NEXT_TPS_UPDATE:
			self.IS_TPS_UPDATING = True

			self.TPS_COUNTERS[ self.TPS_BUFF_INDEX ] = (current_ns - self.LAST_TPS_UPDATE)
			self.TPS_BUFF_INDEX += 1
			if self.TPS_BUFF_INDEX > self.COUNTER_LENGTH - 1:
				self.TPS_BUFF_INDEX = 0
			new_tps = 1 / ( numpy.sum( self.TPS_COUNTERS ) / self.COUNTER_LENGTH )
			self.CURRENT_TPS = round((self.CURRENT_TPS * 0.95) + (new_tps * 0.05), 1)
			Thread(target=self.tick).start()
			self.NEXT_TPS_UPDATE = current_ns + (1 / self.TARGET_TPS)
			self.LAST_TPS_UPDATE = current_ns

		if (not self.IS_FPS_UPDATING) and current_ns > self.NEXT_FPS_UPDATE:
			self.IS_FPS_UPDATING = True

			self.FPS_COUNTERS[ self.FPS_BUFF_INDEX ] = (current_ns - self.LAST_FPS_UPDATE)
			self.FPS_BUFF_INDEX += 1
			if self.FPS_BUFF_INDEX > self.COUNTER_LENGTH - 1:
				self.FPS_BUFF_INDEX = 0
			new_fps = 1 / ( numpy.sum( self.FPS_COUNTERS ) / self.COUNTER_LENGTH )
			self.CURRENT_FPS = round((self.CURRENT_FPS * 0.95) + (new_fps * 0.05), 1)
			Thread(target=self.render).start()
			self.NEXT_FPS_UPDATE = current_ns + (1 / self.TARGET_FPS)
			self.LAST_FPS_UPDATE = current_ns

	def start( self ) -> None:
		pygame.init()
		self.RUNNING = True
		while self.RUNNING:
			self.update()
			self.update_title( )
			self.CYCLE_CLOCK.tick(1000)
		try: pygame.quit()
		except: pass

	def stop( self ) -> None:
		self.RUNNING = False
		try: pygame.quit()
		except: pass
