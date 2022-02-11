from scenes.game.templates import *
from math import atan2, degrees, pi
import pathfinding

class Fence(BasicObject):
    def __init__(self, row, column):
        BasicObject.__init__(self, [column*32+15,row*32+31])
        if self.IS_OBSTACLE:
            GRID.GRID_PATHFINDING[row][column] = 1

    def load_animations(self):
        self.AM.add_animation("idle", 0, 1)
        self.AM.add_animation_component("idle", "scenes/game/assets/fence.png", (0, 0*32, 32, 32))
        self.AM.change_animation("idle")

class Character0(BasicObject):
    def __init__(self):
        BasicObject.__init__(self, [0*32+15,0*32+31], [22,11], [22,44], [-22,-13])
        self.IS_OBSTACLE = False
        self.MM = MovementManager(self.POS, 100, 0.6)

        self.MOVE_TARGET = []
        
    def load_animations(self):
        self.AM.add_animation("idle", 300, 3)
        self.AM.add_animation_component("idle", "scenes/game/assets/idle_body.png", (0, 0*64, 64, 64))
        self.AM.add_animation_component("idle", "scenes/game/assets/idle_legs.png", (0, 0*64, 64, 64))
        self.AM.add_animation_component("idle", "scenes/game/assets/idle_armor.png", (0, 0*64, 64, 64))
        self.AM.add_animation_component("idle", "scenes/game/assets/idle_head.png", (0, 0*64, 64, 64))

        self.AM.add_animation("run", 70, 4)
        self.AM.add_animation_component("run", "scenes/game/assets/run_body.png", (0, 0*64, 64, 64))

        self.AM.add_animation("attackWeapon3", 100, 3)
        self.AM.add_animation_component("attackWeapon3", "scenes/game/assets/attackWeapon3_body.png", (0, 0*64, 64, 64))
        self.AM.add_animation_component("attackWeapon3", "scenes/game/assets/attackWeapon3_sword.png", (0, 0*64, 64, 64))

    def load_states(self):
        obj = self

        # Declaring states
        class Idle(State):
            def __init__(self):
                State.__init__(self, "idle")

            def enter(self):
                obj.AM.change_animation("idle")

            def execute(self):
                if len(obj.MOVE_TARGET) != 0:
                    obj.SM.change_state("run")
                    obj.move_to_point(obj.MOVE_TARGET[0])

        class Run(State):
            def __init__(self):
                State.__init__(self, "run")
            
            def enter(self):
                obj.AM.change_animation("run")

            def execute(self):
                if len(obj.MOVE_TARGET) != 0:
                    if obj.MM.velocity[0] > 0:
                        obj.AM.is_flip = True
                    else:
                        obj.AM.is_flip = False

                    # TODO CHANGE CONDITION/ TOLERANCE                        
                    if abs(obj.POS[0]-obj.MOVE_TARGET[0][0])<2 and abs(obj.POS[1]-obj.MOVE_TARGET[0][1])<2:
                        del obj.MOVE_TARGET[0]
                        obj.MM.direction = [0, 0]
                        obj.MM.angle = 0
                        obj.MM.velocity = [0, 0]
                        if len(obj.MOVE_TARGET) != 0:
                            obj.move_to_point(obj.MOVE_TARGET[0])
                else:
                    obj.SM.change_state("idle")

        class AttackWeapon3(State):
            def __init__(self):
                State.__init__(self, "attackWeapon3")
                self.timer = None
                self.positionspx = None
            
            def enter(self):
                obj.AM.change_animation("attackWeapon3")
                self.timer = pg.time.get_ticks()
                self.positionspx = obj.MM.positionspx

            def execute(self):
                obj.MM.positionspx = self.positionspx
                if pg.time.get_ticks() - self.timer > obj.AM.animations["attackWeapon3_duration"]*obj.AM.animations["attackWeapon3_count"]:
                    print("damage")
                    if obj.MM.direction == [0, 0]:
                        obj.SM.change_state("idle")
                    else:
                        obj.SM.change_state("run")

        class Trans0(Transition):
            def __init__(self):
                Transition.__init__(self, "idle", "run")

        class Trans1(Transition):
            def __init__(self):
                Transition.__init__(self, "run", "idle")

        class Trans2(Transition):
            def __init__(self):
                Transition.__init__(self, "idle", "attackWeapon3")

        class Trans3(Transition):
            def __init__(self):
                Transition.__init__(self, "run", "attackWeapon3")

        class Trans4(Transition):
            def __init__(self):
                Transition.__init__(self, "attackWeapon3", "idle")

        class Trans5(Transition):
            def __init__(self):
                Transition.__init__(self, "attackWeapon3", "run")

        # Init Manager
        self.SM.add_state(Idle())
        self.SM.add_state(Run())
        self.SM.add_state(AttackWeapon3())
        self.SM.add_transition(Trans0())
        self.SM.add_transition(Trans1())
        self.SM.add_transition(Trans2())
        self.SM.add_transition(Trans3())
        self.SM.add_transition(Trans4())
        self.SM.add_transition(Trans5())
        self.SM.start("idle")

    def click(self, is_down, mouse_pos):
        print("hey")

    def collision_fix(self):
        #TODO diagonal walk collision
        collision_tolerance = 2
        for i in range(self.GRID_POS[0]-1, self.GRID_POS[0]+2):
            for j in range(self.GRID_POS[1]-1, self.GRID_POS[1]+2):
                for k in GRID.GRID[i][j]:
                    if k != self and k.IS_OBSTACLE and self.RECT.colliderect(k.RECT):
                        if abs(k.RECT.top - self.RECT.bottom) < collision_tolerance or self.MM.direction[1]<0: # bottom collision
                            self.MM.positionspx[1] = (k.RECT.top-1)*100
                        if abs(k.RECT.bottom - self.RECT.top) < collision_tolerance or self.MM.direction[1]>0: # top collision
                            self.MM.positionspx[1] = (k.RECT.bottom+self.SIZE[1])*100
                        if abs(k.RECT.right - self.RECT.left) < collision_tolerance or self.MM.direction[0]<0: # left collision
                            self.MM.positionspx[0] = (k.RECT.right+self.SIZE[0]//2)*100
                        if abs(k.RECT.left - self.RECT.right) < collision_tolerance or self.MM.direction[0]>0: # right collision
                            self.MM.positionspx[0] = (k.RECT.left-self.SIZE[0]//2-1)*100
                        self.new_rect()
                        self.new_rectscreen()
                        self.update_grid()

    def move_to_point(self, pos):
        dx = CHARACTER0.POS[0] - pos[0]
        dy = CHARACTER0.POS[1] - pos[1]
        rads = atan2(-dy,dx)
        rads %= 2*pi
        degs = degrees(rads)
        CHARACTER0.MM.direction = [-1, 0]
        CHARACTER0.MM.angle = degs
        CHARACTER0.MM.velocity = [0, 0]

    def move_to_block_pathfinding(self, target_block):
        path = pathfinding.astar(GRID.GRID_PATHFINDING, self.GRID_POS, target_block)
        path = pathfinding.simplify_path(path)
        del path[0]

        # CONVERT blocks to middle-of-block coords
        new_path = []
        for i in path:
            new_path.append((i[1]*32+15, i[0]*32+15))

        self.MOVE_TARGET = new_path

    def move_to_point_pathfinding(self, target_point):
        self.MM.direction = [0, 0]
        self.MM.angle = 0
        self.MM.velocity = [0, 0]

        clicked_grid = (target_point[1]//32, target_point[0]//32)
        self.move_to_block_pathfinding(clicked_grid)

        # COMMENT OUT IF MOVING TO SPECIFIC POINT VS MIDDLE OF BLOCK
        self.MOVE_TARGET.append((target_point[0], target_point[1]))

        self.move_to_point(self.MOVE_TARGET[0])

    def loop(self):
        self.MM.loop()
        self.POS = self.MM.position
        self.new_rect()
        self.new_rectscreen()
        self.update_grid()

        self.SM.loop()

class ContextMenu(Panel):
    def __init__(self, pos=(100,100), size=(200,30)):
        Panel.__init__(self, pos, size)
        self.OFFSET = [0,size[1]]

    def add_element(self, obj):
        obj.POS = (self.POS[0] + self.OFFSET[0], self.POS[1] + self.OFFSET[1])
        self.OFFSET[1] += obj.SIZE[1]
        obj.new_rect()
        self.ELEMENTS.append(obj)

        self.SIZE = (self.SIZE[0], self.SIZE[1]+obj.SIZE[1])
        self.new_rect()

CHARACTER0 = Character0()
