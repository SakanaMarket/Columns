## Project 5
## Graphical User Interace of Columns Game
## Ha Tran 53409673
## Lab 5 Eletriby, M.

import pygame
import columns_logic as cm

default_size = (300, 650)

NONE = '   '

class ColumnsGame:

    def __init__(self):
        self._running = True
        self._outter_loop = True

    def run(self)->None:
        try:
            pygame.init()
            Game = cm.board()
            surface = self._create_surface(default_size)
            clock = pygame.time.Clock()
            self.load_images()
            while self._outter_loop:
                while self._running:
                    self._handle_window()
                    faller = cm.generate_faller()
                    move = cm.fall(faller)
                    if Game.match():
                        Game.mark_matched()
                        self._redraw(Game)
                        self._draw_matched(Game)
                        clock.tick(1)
                        Game.empty_matched()
                        self._redraw(Game)
                    while move.landed == False:
                        try:
                            clock.tick(3)
                            Game.fall(move)
                            self.fall_jewels(move)
                            self._handle_events(Game, move)
                            pygame.display.flip()
                            if move.landed:
                                self.landed_jewels(Game,move)
                                
                                clock.tick(2)
                                Game.frozen(move)
                                break
                            if Game.Game_Over:
                                break
                        finally:
                            self._redraw(Game)
                            pass
                    
                        
                    if Game.Game_Over:
                        self._running = False
                        break
                clock.tick(5)
                self._handle_window()
                self._draw_end(Game)
        except:
            pass
        
    def fall_jewels(self, fall)->None:
        '''
        Starts dropping the jewels.
        '''
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        deltax = (fall.col-1) * width_scale
        deltay = (fall.num_rows_moved-1) * height_scale
        self.assign_jewels(fall)
        self._surface.blit(self.g1, (0+deltax,0+deltay-(height_scale*2)))
        self._surface.blit(self.g2, (0+deltax,0+deltay-height_scale))
        self._surface.blit(self.g3, (0+deltax,0+deltay))
        

    def landed_jewels(self, game, fall)->None:
        '''
        Changes jewels to blank white jewels if landed.
        '''
        self._redraw(game)
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        deltax = (fall.col-1) * width_scale
        deltay = (fall.num_rows_moved-1) * height_scale
        jL_scaled = pygame.transform.scale(self.jL, (width_scale, height_scale))
        if fall.num_rows_moved == 13:
            self._surface.blit(jL_scaled, (0+deltax,0+(12*height_scale)-(height_scale*2)))
            self._surface.blit(jL_scaled, (0+deltax,0+(12*height_scale)-height_scale))
            self._surface.blit(jL_scaled, (0+deltax,0+(12*height_scale)))
        else:
            self._surface.blit(jL_scaled, (0+deltax,0+deltay-(height_scale*2)))
            self._surface.blit(jL_scaled, (0+deltax,0+deltay-height_scale))
            self._surface.blit(jL_scaled, (0+deltax,0+deltay))
        pygame.display.flip()


    def _scale_jewels(self)->None:
        '''
        Scales the Jewels to 1/6 width and 1/13 height
        '''
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        self.j1_scaled = pygame.transform.scale(self.j1, (width_scale, height_scale))
        self.j2_scaled = pygame.transform.scale(self.j2, (width_scale, height_scale))
        self.j3_scaled = pygame.transform.scale(self.j3, (width_scale, height_scale))
        self.j4_scaled = pygame.transform.scale(self.j4, (width_scale, height_scale))
        self.j5_scaled = pygame.transform.scale(self.j5, (width_scale, height_scale))
        self.j6_scaled = pygame.transform.scale(self.j6, (width_scale, height_scale))
        self.j7_scaled = pygame.transform.scale(self.j7, (width_scale, height_scale))
            
    def assign_jewels(self, fall)->None:
        '''
        Assigns each letter from the game logic to a colored jewel.
        '''
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        self._jewel_block = []
        
        for jewel in fall.block:
            if jewel == 'S':
                j1_scaled = pygame.transform.scale(self.j1, (width_scale, height_scale))
                self._jewel_block.append(j1_scaled)

            elif jewel == 'T':
                j2_scaled = pygame.transform.scale(self.j2, (width_scale, height_scale))
                self._jewel_block.append(j2_scaled)

            elif jewel == 'V':
                j3_scaled = pygame.transform.scale(self.j3, (width_scale, height_scale))
                self._jewel_block.append(j3_scaled)

            elif jewel == 'W':
                j4_scaled = pygame.transform.scale(self.j4, (width_scale, height_scale))
                self._jewel_block.append(j4_scaled)

            elif jewel == 'X':
                j5_scaled = pygame.transform.scale(self.j5, (width_scale, height_scale))
                self._jewel_block.append(j5_scaled)

            elif jewel == 'Y':
                j6_scaled = pygame.transform.scale(self.j6, (width_scale, height_scale))
                self._jewel_block.append(j6_scaled)

            elif jewel == 'Z':
                j7_scaled = pygame.transform.scale(self.j7, (width_scale, height_scale))
                self._jewel_block.append(j7_scaled)
        self.g1 = self._jewel_block[0]
        self.g2 = self._jewel_block[1]
        self.g3 = self._jewel_block[2]
        
    def load_images(self)->None:
        '''
        Loads all the images needed for the game.
        '''
        self._game_over = pygame.image.load('gameover.png')
        self._bg = pygame.image.load('VP.jpg')
        self.j1 = pygame.image.load('G1.png')
        self.j2 = pygame.image.load('G2.png')
        self.j3 = pygame.image.load('G3.png')
        self.j4 = pygame.image.load('G4.png')
        self.j5 = pygame.image.load('G5.png')
        self.j6 = pygame.image.load('G6.png')
        self.j7 = pygame.image.load('G7.png')
        self.jL = pygame.image.load('GL.png')
        self.jM = pygame.image.load('GM.png')

    def _existing_coordinates(self, game)->None:
        '''
        Finds all the existing tiles from the game logic.
        '''
        existing_coordinates=[]
        for i in range(13):
            for x in range(6):
                if game.GameState.board[i][x] != NONE:
                    box = game.GameState.board[i][x]
                    letter = box[1]
                    existing_coordinates.append((letter,i,x))
        return existing_coordinates

    def _matched_coordinates(self, game)->None:
        '''
        Finds all the matched coordinates from the game logic.
        '''
        matched_coordinates=[]
        for i in range(13):
            for x in range(6):
                if '*' in game.GameState.board[i][x]:
                    box = game.GameState.board[i][x]
                    letter = box[1]
                    matched_coordinates.append((letter,i,x))
        return matched_coordinates

    def _draw_matched(self,game)->None:
        '''
        If a matching sequence has been found, the jewels will turn into a silvered gem, indicating a match.
        '''
        matched = self._matched_coordinates(game)
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        jM_scaled = pygame.transform.scale(self.jM, (width_scale, height_scale))
        for item in matched:
            m,i,x = item
            self._surface.blit(jM_scaled, (0+(x*width_scale), 0+(i*height_scale)))
        pygame.display.flip()
##        self._draw_matched(self, game)

    def _draw_end(self,game)->None:
        '''
        Draws the End Screen.
        '''
        height_scale = self._frac_y(.2)
        width_scale = self._frac_x(1)
        self._redraw(game)
        self._game_over_scale = pygame.transform.scale(self._game_over, (width_scale, height_scale))
        self._surface.blit(self._game_over_scale, ((0,self._surface.get_height()/2)))
        pygame.display.flip()

    def _game_over(self)->None:
        '''
        Initiates a "GAME OVER" text if the game has ended.
        '''
        height_scale = self._frac_y(1)
        width_scale = self._frac_x(.4)
        self._game_over_scale = pygame.transform.scale(self._game_over, (width_scale, height_scale))
        self._surface.blit(self._game_over_scale, ((0,0)))

    def _draw_background(self):
        '''
        Draws a background.
        '''
        self._bg_scale = pygame.transform.scale(self._bg, (self._surface.get_width(), self._surface.get_height()))
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(220,20,60))
        self._surface.blit(self._bg_scale, ((0,0)))
        
    def _redraw(self, game):
        '''
        Redraws the window with all the gems that have frozen.
        '''
        coord = self._existing_coordinates(game)
        height_scale = self._frac_y(.0769)
        width_scale = self._frac_x(.1667)
        self._draw_background()
        for item in coord:
            l,i,x = item
            if item[0] == 'S':
                e1_scaled = pygame.transform.scale(self.j1, (width_scale, height_scale))
                self._surface.blit(e1_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'T':
                e2_scaled = pygame.transform.scale(self.j2, (width_scale, height_scale))
                self._surface.blit(e2_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'V':
                e3_scaled = pygame.transform.scale(self.j3, (width_scale, height_scale))
                self._surface.blit(e3_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'W':
                e4_scaled = pygame.transform.scale(self.j4, (width_scale, height_scale))
                self._surface.blit(e4_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'X':
                e5_scaled = pygame.transform.scale(self.j5, (width_scale, height_scale))
                self._surface.blit(e5_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'Y':
                e6_scaled = pygame.transform.scale(self.j6, (width_scale, height_scale))
                self._surface.blit(e6_scaled, (0+(x*width_scale), 0+(i*height_scale)))
            elif item[0] == 'Z':
                e7_scaled = pygame.transform.scale(self.j7, (width_scale, height_scale))
                self._surface.blit(e7_scaled, (0+(x*width_scale), 0+(i*height_scale)))
        pygame.display.flip()

    def _handle_events(self, Game, fall)->None:
        '''
        Handles the events that deal with in-game function (rotating, moving left/right).
        '''
        for event in pygame.event.get():
            if not fall.landed:
                self._window_events(event)
                pygame.event.poll()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Game.move_right(fall)
                    elif event.key == pygame.K_LEFT:
                        Game.move_left(fall)
                    elif event.key == pygame.K_SPACE:
                        Game.rotater(fall)
                    elif event.key == pygame.K_q:
                        self._quit()
                elif event.type == pygame.NOEVENT:
                    pass
                elif event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.flip()

    def _handle_window(self)->None:
        '''
        Handles the events that deal with window options.
        '''
        for event in pygame.event.get():
            self._window_events(event)

    def _window_events(self, event)->None:
        '''
        Directs the events that deal with window options.
        '''
        if event.type == pygame.QUIT:
            pygame.quit()
            self._quit()
        if event.type == pygame.VIDEORESIZE:
            self._resize(event.size)    
    
    def _quit(self)->None:
        '''
        Quits the current game get breaking the while loop.
        '''
        self._running = False

    def _resize(self, size:(int, int))->None:
        '''
        Makes the surface resizable.
        '''
        surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _create_surface(self, size:(int, int))->None:
        '''
        Creates a surface.
        '''
        self._surface = pygame.display.set_mode(default_size, pygame.RESIZABLE)

    def _frac_to_pixel(self, frac: float, max_pixel: int)->int:
        '''
        Converts fractions to its pixel equivalent of a screen.
        '''
        return int(frac*max_pixel)

    def _frac_y(self, frac_y: float)->int:
        '''
        Returns a fractional equivalent of a y-coordinate.
        '''
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_x(self, frac_x: float)->int:
        '''
        Returns a fractional equivalent of a x-coordinate.
        '''
        return self._frac_to_pixel(frac_x, self._surface.get_width())

if __name__ == '__main__':
    game  = ColumnsGame()
    game.run()
