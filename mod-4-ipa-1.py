'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    list_namefr=from_member[1:]
    list_nameto=to_member[1:]

    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return("friends")
    elif from_member in social_graph[to_member]["following"]:
        return("followed by")
    elif to_member in social_graph[from_member]["following"]:
        return("following")
    else:
        return("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    try:
        
        #rows  
        for row in board:
            if all([ i == "X" for i in row ]) == True: #Replace "X" if the player uses another symbol
                return row[0]
            elif all([ i == "O" for i in row ]) == True: #Replace "O" if the player uses another symbol
                return row[0]
        
        #diagonals
        if (len(set([board[j][j] for j in range(len(board))])) == 1) and (board[0][0] != ''):
            return board[0][0]
        if (len(set([board[len(board)-1-k][k] for k in range(len(board))])) == 1) and (board[len(board)-1][0] != ''):
            return board[len(board)-1][0]
        
        #columns
        column = [col for col in zip(*board) if len(set(col)) == 1]
        if column[0][0] != '': 
            return column[0][0]
        else: 
            return "NO WINNER"
    
    except: 
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Placing the contents of the route_map dictionary here, so that in testing the code, only `legs` would be needed for the route_map
    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","ust"):{
         "travel_time_mins":55
     },
     ("ust","upd"):{
         "travel_time_mins":50
     }
    }

    #At the start
    travel_time = 0
    on_board = False #Shuttle van service has not begun traveling
    current_stop = ""
    next_stop = ""
    
    # Loop because the route is circular and one-way
    while next_stop != second_stop:
        for i in route_map:
            if i[0] == first_stop: #Looking for the first stop
                current_stop = first_stop
                next_stop = i[1]
                on_board = True #Shuttle van service is traveling
                travel_time += route_map[(current_stop, next_stop)]["travel_time_mins"]
                if next_stop == second_stop:
                    break
                else:
                    continue # Go to the next iteration
            if on_board: #Shuttle van service is traveling
                current_stop = next_stop
                next_stop = i[1]
                travel_time += route_map[(current_stop, next_stop)]["travel_time_mins"]
            if next_stop == second_stop:
                break
        if next_stop == second_stop:
            break
    
    return travel_time
