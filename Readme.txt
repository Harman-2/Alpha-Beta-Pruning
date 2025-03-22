Name - Harmanpreet kaur
UTA ID - 1002273536
Programming language - Python
Subject - Artificial Intelligence 

eval function : red_blue_nim.py is the file in which evaluate function is my eval function 
                where the score is calculated based on the amount of red and blue marbles left in 
                the game according to the version selected (standard or misère).
                The score is negative in the standard version because the goal is to minimize it, 
                basically it returns a negative number, -2 * red - 3 * blue.  
                Therefore a lower score implies a better position for the player.
                Whereas the score is positive in the misère version because the goal is to maximize it.
                It returns 2 * red + 3 * blue in the misère form, which is a positive value, 
                a larger positive score implies a better position for the player.
                During the Min-Max search, we use this to evaluate the game state and make informed judgments.

Code Structure : 1. display function, displays the current state of the game.
                 2. user_move function gets the human user move in human's turn 
                    by asking which pile wants to select and from that how many marbles want to remove.
                 3. min_max_alpha_beta function is used for evaluating alpha beta pruning for depth limited MinMax search.
                 4. computer_move function gets the computer move in computer's turn according to the move order defined.
                 5. ply_red_blue_nim function is used for playing the gaming according to the format that is by defining 
                    number of red and blue marbles selected, its version, who will be the first player and the depth.

Run the code in terminal as :- red_blue_nim.py <num-red> <num-blue> [version] [first-player] [depth]
                            
                            eg-1 :   red_blue_nim.py 2 3 standard human 3
                            Output : Human's turn:
                                     Choose a pile (red or blue): red
                                     Enter the number of red marbles to remove: 2
                                     Red: 0 Blue: 3
                                     human loses with a score of 9.red_blue_nim.py 2 3 misere computer 2 

                                 Red: 2 Blue: 3
                                 Human's turn:
                                     Choose a pile (red or blue): red
                                     Enter the number of red marbles to remove: 1
                                     Red: 1 Blue: 3
                                     Computer's turn:
                                     Computer removes 3 blue marble(s).
                                     Red: 1 Blue: 0
                                     computer loses with a score of 2.

                                 Red: 2 Blue: 3
                                 Human's turn:
                                     Choose a pile (red or blue): blue
                                     Enter the number of blue marbles to remove: 2
                                     Red: 2 Blue: 1
                                     Computer's turn:
                                     Computer removes 1 blue marble(s).
                                     Red: 2 Blue: 0
                                     computer loses with a score of 4.


                            eg-2 :   red_blue_nim.py 2 3 misere computer 3
                                    Red: 2 Blue: 3
                                    Computer's turn:
                                    Computer removes 2 red marble(s).
                                    Red: 0 Blue: 3
                                    computer wins with a score of 9.

                                    python3 red_blue_nim.py 2 2 misere computer 3
                                    Red: 2 Blue: 2
                                    Computer's turn:
                                    Computer removes 2 red marble(s).
                                    Red: 0 Blue: 2
                                    computer wins with a score of 6.