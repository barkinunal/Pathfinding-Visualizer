from collections import deque
from Queue import PriorityQueue
from time import sleep

# TODO : Add timers to algorithms.

#                                               GLOBAL VARIABLES
# --------------------------------------------------------------------------------------------------------------
global MENU, LARGE, SMALL, W_SMALL, W_LARGE, WINDOW_HEIGHT, WINDOW_WIDTH, state, SMALL_GRID
global DRAG_COUNT_LARGE, DRAG_COUNT_SMALL, i

MENU = "MENU"
LARGE = "LARGE"
SMALL = "SMALL"

state = MENU

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

SIDE_LENGTH_SMALL = 80
SIDE_LENGTH_LARGE = 160

W_SMALL = WINDOW_HEIGHT/SIDE_LENGTH_SMALL
W_LARGE = WINDOW_HEIGHT/SIDE_LENGTH_LARGE

SMALL_GRID = [ [1]*SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
SMALL_GRID[0][0] = -1
SMALL_GRID[SIDE_LENGTH_SMALL-1][SIDE_LENGTH_SMALL-1] = -1

LARGE_GRID = [ [1] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
LARGE_GRID[0][0] = -1
LARGE_GRID[SIDE_LENGTH_LARGE-1][SIDE_LENGTH_LARGE-1] = -1

DRAG_COUNT_SMALL = [ [0]*SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
DRAG_COUNT_LARGE = [ [0]*SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]

i = 0
    

#                                                 WINDOW PROCESSING
# --------------------------------------------------------------------------------------------------------------
def setup():
    background(255,204,0)
    size(1000, 800)
    state = MENU
    
def draw():
    global state
    if state == SMALL:
       process_small()
    elif state == LARGE:
        process_large()
    else:
        process_menu()
        
def process_menu():
    global WINDOW_HEIGHT, WINDOW_WIDTH
    BUTTON_HEIGHT = 70
    BUTTON_WIDTH = 200
    FONT_SIZE = 25

    largeX = WINDOW_WIDTH/2 + 150 - BUTTON_WIDTH/2
    largeY = WINDOW_HEIGHT/2 - BUTTON_HEIGHT/2

    smallX = WINDOW_WIDTH/2 - 150 - BUTTON_WIDTH/2
    smallY = WINDOW_HEIGHT/2 - BUTTON_HEIGHT/2

    fill(255,255,255)
    rect(largeX, largeY, BUTTON_WIDTH, BUTTON_HEIGHT, 7)
    fill(255,255,255)
    rect(smallX, smallY, BUTTON_WIDTH, BUTTON_HEIGHT, 7)

    textY = WINDOW_HEIGHT / 2 + FONT_SIZE / 4
    smallTextX = 190
    largeTextX = 490

    fill(0,0,0)
    textSize(FONT_SIZE)
    text("Small Grid", smallTextX, textY)

    fill(0,0,0)
    textSize(FONT_SIZE)
    text("Large Grid", largeTextX, textY)
        
def process_small():
    global SMALL_GRID, W_SMALL, i
    y = 0
    for row in SMALL_GRID:
        x = 0
        for col in row:
            if col == -1:
                fill(255, 0, 0)
            elif col == -2:
                fill(0,0,0)
            elif col == 2:
                fill(0,255,0)
            else:
                fill(255,255,255)
            rect(x,y,W_SMALL,W_SMALL)
            x += W_SMALL
        y += W_SMALL
    i+=1
    process_algorithms()
        
def process_large():
    global LARGE_GRID, W_LARGE
    y = 0
    for row in LARGE_GRID:
        x = 0
        for col in row:
            if col == -1:
                fill(255, 0, 0)
            elif col == -2:
               fill(0,0,0)
            elif col == 2:
                fill(0,255,0)
            elif col == 1:
                fill(255,255,255)
            rect(x,y,W_LARGE,W_LARGE)
            x += W_LARGE
        y += W_LARGE
        
    process_algorithms()
        
    
def process_algorithms():
    BUTTON_HEIGHT = 90
    BUTTON_WIDTH = 150
    
    buttonX = 900 - BUTTON_WIDTH/2
    
    texts = ["DFS", "BFS", "UCS", "A*", "RESET"]
    
    for i in range(5):
        buttonX = 900 - BUTTON_WIDTH/2
        buttonY = 100 + (70 * 2*i) - BUTTON_HEIGHT/2
        
        fill(255)
        rect(buttonX, buttonY, BUTTON_WIDTH, BUTTON_HEIGHT, 7)
        fill(0)
        
        fill(0,0,0)
        textSize(25)
        if i!= 4:
            text(texts[i], buttonX + BUTTON_WIDTH/2-25, buttonY+BUTTON_HEIGHT/2+15)
        else :
            text(texts[i], buttonX + BUTTON_WIDTH/2-35, buttonY+BUTTON_HEIGHT/2+10)
        
    
    
    
    

 
#                                               ACTION LISTENERS
# --------------------------------------------------------------------------------------------------------------
def mousePressed():
    global W_SMALL, state, SMALL_GRID, W_LARGE, LARGE_GRID,DRAG_COUNT_SMALL, DRAG_COUNT_LARGE
    if state == MENU:
        result = clicked(mouseX, mouseY)
        state = result
    else :
        if mouseX > 800:
            check_algo_buttons(mouseX,mouseY)
        elif state == SMALL:
            if (SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] == -2):
                SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] = 1
            elif SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] != -1:
                SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] = -2
            DRAG_COUNT_SMALL[mouseY/W_SMALL][mouseX/W_SMALL] += 1
        else:
            if (LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] == -2):
                LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] = 1
            elif LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] != -1:
                LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] = -2
            DRAG_COUNT_LARGE[mouseY/W_LARGE][mouseX/W_LARGE] += 1
            
def mouseDragged():
    global W_SMALL, state, SMALL_GRID, W_LARGE, LARGE_GRID, DRAG_COUNT_SMALL, DRAG_COUNT_LARGE
    if mouseY < 0 or mouseX < 0 or mouseX >= 800 or mouseY >= 800:
        return
    if state == SMALL and DRAG_COUNT_SMALL[mouseY/W_SMALL][mouseX/W_SMALL] == 0:
        if (SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] == -2):
            SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] = 1
        elif SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] != -1:
            SMALL_GRID[mouseY/W_SMALL][mouseX/W_SMALL] = -2
        DRAG_COUNT_SMALL[mouseY/W_SMALL][mouseX/W_SMALL] += 1
    elif state == LARGE and DRAG_COUNT_LARGE[mouseY/W_LARGE][mouseX/W_LARGE] == 0:
        if (LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] == -2):
            LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] = 1
        elif LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] != -1:
            LARGE_GRID[mouseY/W_LARGE][mouseX/W_LARGE] = -2
        DRAG_COUNT_LARGE[mouseY/W_LARGE][mouseX/W_LARGE] += 1

def mouseReleased():
    global DRAG_COUNT_SMALL, DRAG_COUNT_LARGE
    DRAG_COUNT_SMALL = [ [0]*SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
    DRAG_COUNT_LARGE = [ [0]*SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]

def clicked(x, y):
    if y >= 360 and y <= 450 and x >= 450 and x <= 650:
        return LARGE
    
    elif y >= 360 and y <= 450 and x <= 350 and x >= 150:
        return SMALL
        
    else:
        return MENU
        print("FALSE")
        
def check_algo_buttons(mouseX, mouseY) :

    algos = [dfs, bfs, ucs, astar, reset]
    algos_str = ['dfs', 'bfs', 'ucs', 'astar', 'reset']
    
    try :
        corresponding = algos[max((mouseY-50)/135, 0)]
        corresponding_str = algos_str[max((mouseY-50)/135, 0)]
    except:
        print("out of border")
    
    if (corresponding_str != 'reset'):
        check_time(corresponding, corresponding_str)
    else:
        reset()
        
        
def check_time(corresponding, corresponding_str):
    print("\nFINISHED: ")
    start = millis()
    corresponding()
    end = millis()
    print("algorithm: " + corresponding_str)
    print("map: " + state)
    print("duration: " + str(end-start))
    
#                                               ALGORITHMS
# --------------------------------------------------------------------------------------------------------------
    
def dfs() :
    if state == LARGE:
        current_visited = [[False] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
        map = LARGE_GRID
    else:
        current_visited = [[False] * SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
        map = SMALL_GRID
        
    ## Iterative DFS
    
    stack = []
    
    stack.append((0,0))
    found = False
    
    
    while(len(stack)):
        current = stack[-1]
        stack.pop()
        
        row = current[0]
        column = current[1]
        
        if row >= len(map) or row < 0 or column >= len(map[0]) or column < 0 or \
            map[row][column] == -2 or current_visited[row][column]:
                continue
                
        current_visited[row][column] = True

        if map[row][column] == -1 and row != 0 and column != 0:
            make_green(current_visited,map)
            found = True
            break
         
        stack.append((row, column+1))
        stack.append((row, column-1))
        stack.append((row+1, column))
        stack.append((row-1, column))
            
    if not found:
        print("NOT FOUND")

        
def bfs() :
    if state == LARGE:
        current_visited = [[False] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
        map = LARGE_GRID
    else:
        current_visited = [[False] * SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
        map = SMALL_GRID
        
    queue = deque()
    
    queue.append((0,0))
    found = False
    
    while queue:
        current = queue.popleft()
        row = current[0]
        column = current[1]
        
        if row >= len(map) or row < 0 or column >= len(map[0]) or column < 0 or \
        map[row][column] == -2 or current_visited[row][column]:
            continue
            
        current_visited[row][column] = True
            
        if map[row][column] == -1 and row != 0 and column != 0:
            make_green(current_visited,map)
            found = True
            break
        
        queue.append((row, column+1))
        queue.append((row, column-1))
        queue.append((row+1, column))
        queue.append((row-1, column))
        
    if not found:
        print("NOT FOUND")
        
        
def ucs():
    global LARGE_GRID, SMALL_GRID
    if state == LARGE:
        map = LARGE_GRID
        goal = (SIDE_LENGTH_LARGE-1, SIDE_LENGTH_LARGE-1)
        size = (SIDE_LENGTH_LARGE, SIDE_LENGTH_LARGE)
        current_visited = [[False] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
    else:
        map = SMALL_GRID
        goal = (SIDE_LENGTH_SMALL-1, SIDE_LENGTH_SMALL-1)
        size = (SIDE_LENGTH_SMALL, SIDE_LENGTH_SMALL)
        current_visited = [[False] * SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]

    start = (0,0)
    pq = PriorityQueue()
    pq.put((0, start)) # (priority, node)
    found = False
    current_visited[0][0] = True

    
    while True:
        ucs_w, current_node = pq.get()
        row, column = current_node
#        print(current_node)
        
        if current_node == goal:
            found = True
            make_green(current_visited, map)
            break
        
        
        for neighbor in find_neighbors(current_node, map):
            row, column = neighbor
            if not current_visited[row][column]:
                current_visited[row][column] = True;
                pq.put((ucs_w + 1,neighbor))
    
    if not found:
        print("NOT FOUND")
    
    
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(start=(0,0)):
    if state == LARGE:
        map = LARGE_GRID
        goal = (SIDE_LENGTH_LARGE-1, SIDE_LENGTH_LARGE-1)
        size = (SIDE_LENGTH_LARGE, SIDE_LENGTH_LARGE)
        current_visited = [[False] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
        end = (SIDE_LENGTH_LARGE - 1, SIDE_LENGTH_LARGE - 1)
    else:
        map = SMALL_GRID
        goal = (SIDE_LENGTH_SMALL-1, SIDE_LENGTH_SMALL-1)
        size = (SIDE_LENGTH_SMALL, SIDE_LENGTH_SMALL)
        current_visited = [[False] * SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
        end = (SIDE_LENGTH_SMALL - 1, SIDE_LENGTH_SMALL - 1)


    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    found = False

    # Initialize both open and closed list
    open_list = []

    # Add the start node
    open_list.append(start_node)
    current_visited[start_node.position[0]][start_node.position[1]] = True

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        
        # Found the goal
        if current_node == end_node:
            make_green(current_visited, map)
            found = True
            break

        # Generate children
        children = []
        for new_position in find_neighbors(current_node.position, map): # Adjacent squares

            # Create new node
            new_node = Node(current_node, new_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
        
            if current_visited[child.position[0]][child.position[1]]:
                continue

            current_visited[child.position[0]][child.position[1]] = True

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            
    if not found:
        print("NOT FOUND")
    
    
def find_neighbors(point, grid):
    x, y = point
    children = [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]
    result = []
    for child in children:
        row, col = child
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid)) or grid[row][col] == -2:
            continue
        result.append(child)
    return result
    

def make_green(current_visited, map):
    for i in range(len(current_visited)):
        for j in range(len(current_visited[i])):
            if current_visited[i][j] and (i,j) != (0,0) and (i,j) != (len(map)-1, len(map[i])-1):
                map[i][j] = 2

    

def reset():
    global LARGE_GRID, SMALL_GRID, DRAG_COUNT_LARGE, DRAG_COUNT_SMALL
    if state == LARGE:
        LARGE_GRID[0][0] = -1
        current_grid = LARGE_GRID
        LARGE_GRID[SIDE_LENGTH_LARGE-1][SIDE_LENGTH_LARGE-1] = -1
        DRAG_COUNT_LARGE = [ [0]*SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
        temp_grid = [ [1] * SIDE_LENGTH_LARGE for n in range(SIDE_LENGTH_LARGE)]
    else:
        SMALL_GRID[0][0] = -1
        current_grid = SMALL_GRID
        SMALL_GRID[SIDE_LENGTH_SMALL-1][SIDE_LENGTH_SMALL-1] = -1
        DRAG_COUNT_SMALL = [ [0]*SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]
        temp_grid = [ [1] * SIDE_LENGTH_SMALL for n in range(SIDE_LENGTH_SMALL)]

    for i in range(len(temp_grid)):
        for j in range(len(temp_grid[i])):
            if current_grid[i][j] != 2:
                temp_grid[i][j] = current_grid[i][j]
            
    if state == LARGE:
        LARGE_GRID = temp_grid
    else:
        SMALL_GRID = temp_grid
