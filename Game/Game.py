from random import randrange
import itertools

class Game():
    '''
        Tic Tac Toe Game
    '''

    def __init__(self):
        self.list_of_plots = list()
        self.player_1_positions = list()
        self.player_2_positions = list()
        self.player_1_list = list()
        self.player_2_list = list()
        self.sym = list()
        self.player_name = list()

    def clear_data(self):
        self.list_of_plots.clear()
        self.player_1_positions.clear()
        self.player_2_positions.clear()
        self.player_1_list.clear()
        self.player_2_list.clear()
        self.sym.clear()
        self.player_name.clear()

    def details(self):
        '''
        Get the Basic details of Players

        o/p: Returns palyers Details

        '''
        print("***************** Tic Tac Toe *****************")
        print("Select 2 player Game or vs computer Game :")
        print("      Enter '1' for two player Game")
        print("      Enter '2' for one player vs Computer Game")
        valid = True
        while(valid):
            gameMode = input("Please select your input: ")
            if(gameMode and gameMode in "12"):
                player1 = input("Enter Player1 name: ")
                print("\n Welcome {} \n".format(player1.upper()))
                if(gameMode == "1"):
                    valid = False
                    player2 = input("Enter Player2 name: ")
                    print("\n Welcome {} \n".format(player2.upper()))
                    print("Start Game {0} vs {1} \n".format(player1.capitalize(), player2.capitalize()))
                    self.player_name.append(player1.capitalize())
                    self.player_name.append(player2.capitalize())
                    return player1, player2
                elif(gameMode == "2"):
                    valid = False
                    print("Start Game {} vs Computer".format(player1.capitalize()))
                    self.player_name.append(player1.capitalize())
                    self.player_name.append("Computer")
                    return player1, "Computer"
            else:
                valid = True
                print("Entered Invalid Number, please select valid Number")


    def symbols(self): 
        '''
        Get the Symbols and validate
        
        o/p: Returns palyers symbols along with names

        '''
        valid = True
        player_details = GAME.details()
        while(valid):
            inputSymbol = input("{}, Choose Your Symbol X or O: \n".format(player_details[0].capitalize()))
            if(inputSymbol in "XOxo"):
                if(inputSymbol):
                    player_1_symbol =  inputSymbol.capitalize()
                    if(player_1_symbol in "Xx"):
                        player_2_symbol = "O"
                    elif(player_1_symbol in "oO"):
                        player_2_symbol = "X"
                else:
                    player_2_symbol = "O"
                    player_1_symbol = "X"
                print("{0} selected symbol is : {1}".format(player_details[0].capitalize(), player_1_symbol.upper()))
                print("{0} symbol is: {1}".format(player_details[1].capitalize(), player_2_symbol.upper()))
                valid = False
            else:
                player_2_symbol = player_1_symbol = False
                print("Entered Invalid symbol, please enter correct symbol")   
        if(player_2_symbol and player_1_symbol):
            self.sym.append(player_1_symbol)
            self.sym.append(player_2_symbol)
            return (player_1_symbol, player_2_symbol, player_details[0], player_details[1])


    def calc(self, inputNumber):
        '''
        cal the pos of number in x y axis co ordinates
        
        o/p: Returns position

        '''
        if(inputNumber <= 3):
                xposition, yposition = 2,inputNumber-1
        if(inputNumber > 3 and inputNumber < 7 ):
                xposition, yposition = 1,inputNumber-4
        if(inputNumber >= 7):
                xposition, yposition = 0,inputNumber-7
        return xposition,yposition



    def getting_input(self,i):
        '''
        Get the Inputs from user
        
        o/p: Returns palyer calculated pos by calc fun

        '''
        valid = True
        num_range = range(1, 10)
        while (valid):
            if(i%2==0):
                try:
                    num = int(input("\n{} Enter Your plot Number: ".format(self.player_name[0])))
                    if(num in num_range):
                        if(num not in self.list_of_plots):
                            self.list_of_plots.append(num)
                            pos = GAME.calc(num)
                            self.player_1_positions.append(pos)
                            self.player_1_list.append(num)
                            self.player_1_list.sort()
                            return self.player_1_positions
                            valid = False
                        else:
                            print("Entered plot is already used please select another plot number")
                    
                    else:
                        print("Your selected number not in 1 to 10, Please enter valid num,")
                except:
                    continue
                    print("Not a valid number, please enter valid number")

            elif(i%2 == 1):
                if(self.player_name[1] == "Computer"):
                    num = randrange(1, 10)
                    if(num not in self.list_of_plots):
                        print("Computer selected {} Number".format(num))
                        self.list_of_plots.append(num)
                        pos = GAME.calc(num)
                        self.player_2_positions.append(pos)
                        self.player_2_list.append(num)
                        self.player_2_list.sort()
                        return self.player_2_positions

                else:
                    try:
                        num = int(input("\n{} Enter Your plot Number: ".format(self.player_name[1])))
                        if(num in num_range):
                            if(num not in self.list_of_plots ):
                                self.list_of_plots.append(num)
                                pos = GAME.calc(num)
                                self.player_2_positions.append(pos)
                                self.player_2_list.append(num)
                                self.player_2_list.sort()
                                return self.player_2_positions
                            else:
                                print("Entered plot is already used please select another plot number")                     
                        else:
                            print("Your entered number is not in 1 to 10, Please enter valid number")
                    except:
                        print("Not a valid number, please enter valid number")
            else:
                print("Please enter valid num, Either Entered Number is was already used or Enter Number between 1 to 9")


    def validation(self):
        '''
        Checks wheather player won the game or not
        
        o/p: Returns Won or loss

        '''
        list_of_possible_outputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
        for _ in range(0, len(self.player_1_list)+1):
            for _list in itertools.combinations(self.player_1_list, 3):
                if(list(_list) in list_of_possible_outputs):
                    return "Won", self.player_name[0]
        for _ in range(0, len(self.player_2_list)+1):
            for _list in itertools.combinations(self.player_2_list, 3):
                if(list(_list) in list_of_possible_outputs):
                    return "Won", self.player_name[1]
        return "noresult"

    def game_flow(self):
        '''
        Flow of the game
        
        o/p: displays Won or loss

        '''
        user_input = str()
        GAME.clear_data()  # To clear all the data avaliable if exist
        GAME.symbols()
        loop = True
        i = 0
        while(loop):
            GAME.getting_input(i)
            i += 1
            GAME.display()
            val = GAME.validation()
            if(val[0] == "Won"):
                print("\n \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("       {} WON THE GAME        ".format(val[1]))
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                loop = False
                user_input = input("press 1 to play the game again or enter key to close the console ")
            elif(i == 9):
                print("\n \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("     Game Draw      ")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                halt = False
                user_input = input("press 1 to play the game again or enter key to close the console ")
            else:
                loop = True
            if(user_input == '1'):
                GAME.game_flow()

    def display(self):
        '''
        Displays the formate

        '''
        player_1_symbol = self.sym[0]
        player_2_symbol = self.sym[1]
        for i in range(3):
            print("\n")
            for j in range(3):
                for num in self.player_1_positions:
                    if(num[0] == i and num[1] == j):
                        print(player_1_symbol, end="")
                for num in self.player_2_positions:
                    if(num[0] == i and num[1] == j):
                        print(player_2_symbol, end="")
                else:
                    print("-", end="")
                    print("|", end = "")
        print("\n")

GAME = Game()
GAME.game_flow()

