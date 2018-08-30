import random
import itertools

map_card_to_value = {"A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}

map_card_term_to_num = {
    "AS":0,  "2S": 1,  "3S":2,  "4S":3,  "5S": 4,  "6S": 5,  "7S": 6,  "8S": 7,  "9S": 8,  "TS": 9,  "JS": 10, "QS": 11, "KS": 12,
    "AH":13, "2H": 14, "3H":15, "4H":16, "5H": 17, "6H": 18, "7H": 19, "8H": 20, "9H": 21, "TH": 22, "JH": 23, "QH": 24, "KH": 25,
    "AD":26, "2D": 27, "3D":28, "4D":29, "5D": 30, "6D": 31, "7D": 32, "8D": 33, "9D": 34, "TD": 35, "JD": 36, "QD": 37, "KD": 38,
    "AC":39, "2C": 40, "3C":41, "4C":42, "5C": 43, "6C": 44, "7C": 45, "8C": 46, "9C": 47, "TC": 48, "JC": 49, "QC": 50, "KC": 51
}

map_card_num_to_term = {
     0:"AS",  1:"2S",  2:"3S",  3:"4S",  4:"5S",  5:"6S",  6:"7S",  7:"8S",  8:"9S",  9:"TS", 10:"JS", 11:"QS", 12:"KS",
    13:"AH", 14:"2H", 15:"3H", 16:"4H", 17:"5H", 18:"6H", 19:"7H", 20:"8H", 21:"9H", 22:"TH", 23:"JH", 24:"QH", 25:"KH",
    26:"AD", 27:"2D", 28:"3D", 29:"4D", 30:"5D", 31:"6D", 32:"7D", 33:"8D", 34:"9D", 35:"TD", 36:"JD", 37:"QD", 38:"KD",
    39:"AC", 40:"2C", 41:"3C", 42:"4C", 43:"5C", 44:"6C", 45:"7C", 46:"8C", 47:"9C", 48:"TC", 49:"JC", 50:"QC", 51:"KC"
}

all_hand_cards_term = [
    ["AS","2S"],["AS","3S"],["AS","4S"],["AS","5S"],["AS","6S"],["AS","7S"],["AS","8S"],["AS","9S"],["AS","TS"],["AS","JS"],["AS","QS"],["AS","KS"],["AS","AH"],["AS","2H"],["AS","3H"],["AS","4H"],["AS","5H"],["AS","6H"],["AS","7H"],["AS","8H"],["AS","9H"],["AS","TH"],["AS","JH"],["AS","QH"],["AS","KH"],["AS","AD"],["AS","2D"],["AS","3D"],["AS","4D"],["AS","5D"],["AS","6D"],["AS","7D"],["AS","8D"],["AS","9D"],["AS","TD"],["AS","JD"],["AS","QD"],["AS","KD"],["AS","AC"],["AS","2C"],["AS","3C"],["AS","4C"],["AS","5C"],["AS","6C"],["AS","7C"],["AS","8C"],["AS","9C"],["AS","TC"],["AS","JC"],["AS","QC"],["AS","KC"],
    ["2S","3S"],["2S","4S"],["2S","5S"],["2S","6S"],["2S","7S"],["2S","8S"],["2S","9S"],["2S","TS"],["2S","JS"],["2S","QS"],["2S","KS"],["2S","AH"],["2S","2H"],["2S","3H"],["2S","4H"],["2S","5H"],["2S","6H"],["2S","7H"],["2S","8H"],["2S","9H"],["2S","TH"],["2S","JH"],["2S","QH"],["2S","KH"],["2S","AD"],["2S","2D"],["2S","3D"],["2S","4D"],["2S","5D"],["2S","6D"],["2S","7D"],["2S","8D"],["2S","9D"],["2S","TD"],["2S","JD"],["2S","QD"],["2S","KD"],["2S","AC"],["2S","2C"],["2S","3C"],["2S","4C"],["2S","5C"],["2S","6C"],["2S","7C"],["2S","8C"],["2S","9C"],["2S","TC"],["2S","JC"],["2S","QC"],["2S","KC"],
    ["3S","4S"],["3S","5S"],["3S","6S"],["3S","7S"],["3S","8S"],["3S","9S"],["3S","TS"],["3S","JS"],["3S","QS"],["3S","KS"],["3S","AH"],["3S","2H"],["3S","3H"],["3S","4H"],["3S","5H"],["3S","6H"],["3S","7H"],["3S","8H"],["3S","9H"],["3S","TH"],["3S","JH"],["3S","QH"],["3S","KH"],["3S","AD"],["3S","2D"],["3S","3D"],["3S","4D"],["3S","5D"],["3S","6D"],["3S","7D"],["3S","8D"],["3S","9D"],["3S","TD"],["3S","JD"],["3S","QD"],["3S","KD"],["3S","AC"],["3S","2C"],["3S","3C"],["3S","4C"],["3S","5C"],["3S","6C"],["3S","7C"],["3S","8C"],["3S","9C"],["3S","TC"],["3S","JC"],["3S","QC"],["3S","KC"],
    ["4S","5S"],["4S","6S"],["4S","7S"],["4S","8S"],["4S","9S"],["4S","TS"],["4S","JS"],["4S","QS"],["4S","KS"],["4S","AH"],["4S","2H"],["4S","3H"],["4S","4H"],["4S","5H"],["4S","6H"],["4S","7H"],["4S","8H"],["4S","9H"],["4S","TH"],["4S","JH"],["4S","QH"],["4S","KH"],["4S","AD"],["4S","2D"],["4S","3D"],["4S","4D"],["4S","5D"],["4S","6D"],["4S","7D"],["4S","8D"],["4S","9D"],["4S","TD"],["4S","JD"],["4S","QD"],["4S","KD"],["4S","AC"],["4S","2C"],["4S","3C"],["4S","4C"],["4S","5C"],["4S","6C"],["4S","7C"],["4S","8C"],["4S","9C"],["4S","TC"],["4S","JC"],["4S","QC"],["4S","KC"],
    ["5S","6S"],["5S","7S"],["5S","8S"],["5S","9S"],["5S","TS"],["5S","JS"],["5S","QS"],["5S","KS"],["5S","AH"],["5S","2H"],["5S","3H"],["5S","4H"],["5S","5H"],["5S","6H"],["5S","7H"],["5S","8H"],["5S","9H"],["5S","TH"],["5S","JH"],["5S","QH"],["5S","KH"],["5S","AD"],["5S","2D"],["5S","3D"],["5S","4D"],["5S","5D"],["5S","6D"],["5S","7D"],["5S","8D"],["5S","9D"],["5S","TD"],["5S","JD"],["5S","QD"],["5S","KD"],["5S","AC"],["5S","2C"],["5S","3C"],["5S","4C"],["5S","5C"],["5S","6C"],["5S","7C"],["5S","8C"],["5S","9C"],["5S","TC"],["5S","JC"],["5S","QC"],["5S","KC"],
    ["6S","7S"],["6S","8S"],["6S","9S"],["6S","TS"],["6S","JS"],["6S","QS"],["6S","KS"],["6S","AH"],["6S","2H"],["6S","3H"],["6S","4H"],["6S","5H"],["6S","6H"],["6S","7H"],["6S","8H"],["6S","9H"],["6S","TH"],["6S","JH"],["6S","QH"],["6S","KH"],["6S","AD"],["6S","2D"],["6S","3D"],["6S","4D"],["6S","5D"],["6S","6D"],["6S","7D"],["6S","8D"],["6S","9D"],["6S","TD"],["6S","JD"],["6S","QD"],["6S","KD"],["6S","AC"],["6S","2C"],["6S","3C"],["6S","4C"],["6S","5C"],["6S","6C"],["6S","7C"],["6S","8C"],["6S","9C"],["6S","TC"],["6S","JC"],["6S","QC"],["6S","KC"],
    ["7S","8S"],["7S","9S"],["7S","TS"],["7S","JS"],["7S","QS"],["7S","KS"],["7S","AH"],["7S","2H"],["7S","3H"],["7S","4H"],["7S","5H"],["7S","6H"],["7S","7H"],["7S","8H"],["7S","9H"],["7S","TH"],["7S","JH"],["7S","QH"],["7S","KH"],["7S","AD"],["7S","2D"],["7S","3D"],["7S","4D"],["7S","5D"],["7S","6D"],["7S","7D"],["7S","8D"],["7S","9D"],["7S","TD"],["7S","JD"],["7S","QD"],["7S","KD"],["7S","AC"],["7S","2C"],["7S","3C"],["7S","4C"],["7S","5C"],["7S","6C"],["7S","7C"],["7S","8C"],["7S","9C"],["7S","TC"],["7S","JC"],["7S","QC"],["7S","KC"],
    ["8S","9S"],["8S","TS"],["8S","JS"],["8S","QS"],["8S","KS"],["8S","AH"],["8S","2H"],["8S","3H"],["8S","4H"],["8S","5H"],["8S","6H"],["8S","7H"],["8S","8H"],["8S","9H"],["8S","TH"],["8S","JH"],["8S","QH"],["8S","KH"],["8S","AD"],["8S","2D"],["8S","3D"],["8S","4D"],["8S","5D"],["8S","6D"],["8S","7D"],["8S","8D"],["8S","9D"],["8S","TD"],["8S","JD"],["8S","QD"],["8S","KD"],["8S","AC"],["8S","2C"],["8S","3C"],["8S","4C"],["8S","5C"],["8S","6C"],["8S","7C"],["8S","8C"],["8S","9C"],["8S","TC"],["8S","JC"],["8S","QC"],["8S","KC"],
    ["9S","TS"],["9S","JS"],["9S","QS"],["9S","KS"],["9S","AH"],["9S","2H"],["9S","3H"],["9S","4H"],["9S","5H"],["9S","6H"],["9S","7H"],["9S","8H"],["9S","9H"],["9S","TH"],["9S","JH"],["9S","QH"],["9S","KH"],["9S","AD"],["9S","2D"],["9S","3D"],["9S","4D"],["9S","5D"],["9S","6D"],["9S","7D"],["9S","8D"],["9S","9D"],["9S","TD"],["9S","JD"],["9S","QD"],["9S","KD"],["9S","AC"],["9S","2C"],["9S","3C"],["9S","4C"],["9S","5C"],["9S","6C"],["9S","7C"],["9S","8C"],["9S","9C"],["9S","TC"],["9S","JC"],["9S","QC"],["9S","KC"],
    ["TS","JS"],["TS","QS"],["TS","KS"],["TS","AH"],["TS","2H"],["TS","3H"],["TS","4H"],["TS","5H"],["TS","6H"],["TS","7H"],["TS","8H"],["TS","9H"],["TS","TH"],["TS","JH"],["TS","QH"],["TS","KH"],["TS","AD"],["TS","2D"],["TS","3D"],["TS","4D"],["TS","5D"],["TS","6D"],["TS","7D"],["TS","8D"],["TS","9D"],["TS","TD"],["TS","JD"],["TS","QD"],["TS","KD"],["TS","AC"],["TS","2C"],["TS","3C"],["TS","4C"],["TS","5C"],["TS","6C"],["TS","7C"],["TS","8C"],["TS","9C"],["TS","TC"],["TS","JC"],["TS","QC"],["TS","KC"],
    ["JS","QS"],["JS","KS"],["JS","AH"],["JS","2H"],["JS","3H"],["JS","4H"],["JS","5H"],["JS","6H"],["JS","7H"],["JS","8H"],["JS","9H"],["JS","TH"],["JS","JH"],["JS","QH"],["JS","KH"],["JS","AD"],["JS","2D"],["JS","3D"],["JS","4D"],["JS","5D"],["JS","6D"],["JS","7D"],["JS","8D"],["JS","9D"],["JS","TD"],["JS","JD"],["JS","QD"],["JS","KD"],["JS","AC"],["JS","2C"],["JS","3C"],["JS","4C"],["JS","5C"],["JS","6C"],["JS","7C"],["JS","8C"],["JS","9C"],["JS","TC"],["JS","JC"],["JS","QC"],["JS","KC"],
    ["QS","KS"],["QS","AH"],["QS","2H"],["QS","3H"],["QS","4H"],["QS","5H"],["QS","6H"],["QS","7H"],["QS","8H"],["QS","9H"],["QS","TH"],["QS","JH"],["QS","QH"],["QS","KH"],["QS","AD"],["QS","2D"],["QS","3D"],["QS","4D"],["QS","5D"],["QS","6D"],["QS","7D"],["QS","8D"],["QS","9D"],["QS","TD"],["QS","JD"],["QS","QD"],["QS","KD"],["QS","AC"],["QS","2C"],["QS","3C"],["QS","4C"],["QS","5C"],["QS","6C"],["QS","7C"],["QS","8C"],["QS","9C"],["QS","TC"],["QS","JC"],["QS","QC"],["QS","KC"],
    ["KS","AH"],["KS","2H"],["KS","3H"],["KS","4H"],["KS","5H"],["KS","6H"],["KS","7H"],["KS","8H"],["KS","9H"],["KS","TH"],["KS","JH"],["KS","QH"],["KS","KH"],["KS","AD"],["KS","2D"],["KS","3D"],["KS","4D"],["KS","5D"],["KS","6D"],["KS","7D"],["KS","8D"],["KS","9D"],["KS","TD"],["KS","JD"],["KS","QD"],["KS","KD"],["KS","AC"],["KS","2C"],["KS","3C"],["KS","4C"],["KS","5C"],["KS","6C"],["KS","7C"],["KS","8C"],["KS","9C"],["KS","TC"],["KS","JC"],["KS","QC"],["KS","KC"],
    ["AH","2H"],["AH","3H"],["AH","4H"],["AH","5H"],["AH","6H"],["AH","7H"],["AH","8H"],["AH","9H"],["AH","TH"],["AH","JH"],["AH","QH"],["AH","KH"],["AH","AD"],["AH","2D"],["AH","3D"],["AH","4D"],["AH","5D"],["AH","6D"],["AH","7D"],["AH","8D"],["AH","9D"],["AH","TD"],["AH","JD"],["AH","QD"],["AH","KD"],["AH","AC"],["AH","2C"],["AH","3C"],["AH","4C"],["AH","5C"],["AH","6C"],["AH","7C"],["AH","8C"],["AH","9C"],["AH","TC"],["AH","JC"],["AH","QC"],["AH","KC"],
    ["2H","3H"],["2H","4H"],["2H","5H"],["2H","6H"],["2H","7H"],["2H","8H"],["2H","9H"],["2H","TH"],["2H","JH"],["2H","QH"],["2H","KH"],["2H","AD"],["2H","2D"],["2H","3D"],["2H","4D"],["2H","5D"],["2H","6D"],["2H","7D"],["2H","8D"],["2H","9D"],["2H","TD"],["2H","JD"],["2H","QD"],["2H","KD"],["2H","AC"],["2H","2C"],["2H","3C"],["2H","4C"],["2H","5C"],["2H","6C"],["2H","7C"],["2H","8C"],["2H","9C"],["2H","TC"],["2H","JC"],["2H","QC"],["2H","KC"],
    ["3H","4H"],["3H","5H"],["3H","6H"],["3H","7H"],["3H","8H"],["3H","9H"],["3H","TH"],["3H","JH"],["3H","QH"],["3H","KH"],["3H","AD"],["3H","2D"],["3H","3D"],["3H","4D"],["3H","5D"],["3H","6D"],["3H","7D"],["3H","8D"],["3H","9D"],["3H","TD"],["3H","JD"],["3H","QD"],["3H","KD"],["3H","AC"],["3H","2C"],["3H","3C"],["3H","4C"],["3H","5C"],["3H","6C"],["3H","7C"],["3H","8C"],["3H","9C"],["3H","TC"],["3H","JC"],["3H","QC"],["3H","KC"],
    ["4H","5H"],["4H","6H"],["4H","7H"],["4H","8H"],["4H","9H"],["4H","TH"],["4H","JH"],["4H","QH"],["4H","KH"],["4H","AD"],["4H","2D"],["4H","3D"],["4H","4D"],["4H","5D"],["4H","6D"],["4H","7D"],["4H","8D"],["4H","9D"],["4H","TD"],["4H","JD"],["4H","QD"],["4H","KD"],["4H","AC"],["4H","2C"],["4H","3C"],["4H","4C"],["4H","5C"],["4H","6C"],["4H","7C"],["4H","8C"],["4H","9C"],["4H","TC"],["4H","JC"],["4H","QC"],["4H","KC"],
    ["5H","6H"],["5H","7H"],["5H","8H"],["5H","9H"],["5H","TH"],["5H","JH"],["5H","QH"],["5H","KH"],["5H","AD"],["5H","2D"],["5H","3D"],["5H","4D"],["5H","5D"],["5H","6D"],["5H","7D"],["5H","8D"],["5H","9D"],["5H","TD"],["5H","JD"],["5H","QD"],["5H","KD"],["5H","AC"],["5H","2C"],["5H","3C"],["5H","4C"],["5H","5C"],["5H","6C"],["5H","7C"],["5H","8C"],["5H","9C"],["5H","TC"],["5H","JC"],["5H","QC"],["5H","KC"],
    ["6H","7H"],["6H","8H"],["6H","9H"],["6H","TH"],["6H","JH"],["6H","QH"],["6H","KH"],["6H","AD"],["6H","2D"],["6H","3D"],["6H","4D"],["6H","5D"],["6H","6D"],["6H","7D"],["6H","8D"],["6H","9D"],["6H","TD"],["6H","JD"],["6H","QD"],["6H","KD"],["6H","AC"],["6H","2C"],["6H","3C"],["6H","4C"],["6H","5C"],["6H","6C"],["6H","7C"],["6H","8C"],["6H","9C"],["6H","TC"],["6H","JC"],["6H","QC"],["6H","KC"],
    ["7H","8H"],["7H","9H"],["7H","TH"],["7H","JH"],["7H","QH"],["7H","KH"],["7H","AD"],["7H","2D"],["7H","3D"],["7H","4D"],["7H","5D"],["7H","6D"],["7H","7D"],["7H","8D"],["7H","9D"],["7H","TD"],["7H","JD"],["7H","QD"],["7H","KD"],["7H","AC"],["7H","2C"],["7H","3C"],["7H","4C"],["7H","5C"],["7H","6C"],["7H","7C"],["7H","8C"],["7H","9C"],["7H","TC"],["7H","JC"],["7H","QC"],["7H","KC"],
    ["8H","9H"],["8H","TH"],["8H","JH"],["8H","QH"],["8H","KH"],["8H","AD"],["8H","2D"],["8H","3D"],["8H","4D"],["8H","5D"],["8H","6D"],["8H","7D"],["8H","8D"],["8H","9D"],["8H","TD"],["8H","JD"],["8H","QD"],["8H","KD"],["8H","AC"],["8H","2C"],["8H","3C"],["8H","4C"],["8H","5C"],["8H","6C"],["8H","7C"],["8H","8C"],["8H","9C"],["8H","TC"],["8H","JC"],["8H","QC"],["8H","KC"],
    ["9H","TH"],["9H","JH"],["9H","QH"],["9H","KH"],["9H","AD"],["9H","2D"],["9H","3D"],["9H","4D"],["9H","5D"],["9H","6D"],["9H","7D"],["9H","8D"],["9H","9D"],["9H","TD"],["9H","JD"],["9H","QD"],["9H","KD"],["9H","AC"],["9H","2C"],["9H","3C"],["9H","4C"],["9H","5C"],["9H","6C"],["9H","7C"],["9H","8C"],["9H","9C"],["9H","TC"],["9H","JC"],["9H","QC"],["9H","KC"],
    ["TH","JH"],["TH","QH"],["TH","KH"],["TH","AD"],["TH","2D"],["TH","3D"],["TH","4D"],["TH","5D"],["TH","6D"],["TH","7D"],["TH","8D"],["TH","9D"],["TH","TD"],["TH","JD"],["TH","QD"],["TH","KD"],["TH","AC"],["TH","2C"],["TH","3C"],["TH","4C"],["TH","5C"],["TH","6C"],["TH","7C"],["TH","8C"],["TH","9C"],["TH","TC"],["TH","JC"],["TH","QC"],["TH","KC"],
    ["JH","QH"],["JH","KH"],["JH","AD"],["JH","2D"],["JH","3D"],["JH","4D"],["JH","5D"],["JH","6D"],["JH","7D"],["JH","8D"],["JH","9D"],["JH","TD"],["JH","JD"],["JH","QD"],["JH","KD"],["JH","AC"],["JH","2C"],["JH","3C"],["JH","4C"],["JH","5C"],["JH","6C"],["JH","7C"],["JH","8C"],["JH","9C"],["JH","TC"],["JH","JC"],["JH","QC"],["JH","KC"],
    ["QH","KH"],["QH","AD"],["QH","2D"],["QH","3D"],["QH","4D"],["QH","5D"],["QH","6D"],["QH","7D"],["QH","8D"],["QH","9D"],["QH","TD"],["QH","JD"],["QH","QD"],["QH","KD"],["QH","AC"],["QH","2C"],["QH","3C"],["QH","4C"],["QH","5C"],["QH","6C"],["QH","7C"],["QH","8C"],["QH","9C"],["QH","TC"],["QH","JC"],["QH","QC"],["QH","KC"],
    ["KH","AD"],["KH","2D"],["KH","3D"],["KH","4D"],["KH","5D"],["KH","6D"],["KH","7D"],["KH","8D"],["KH","9D"],["KH","TD"],["KH","JD"],["KH","QD"],["KH","KD"],["KH","AC"],["KH","2C"],["KH","3C"],["KH","4C"],["KH","5C"],["KH","6C"],["KH","7C"],["KH","8C"],["KH","9C"],["KH","TC"],["KH","JC"],["KH","QC"],["KH","KC"],
    ["AD","2D"],["AD","3D"],["AD","4D"],["AD","5D"],["AD","6D"],["AD","7D"],["AD","8D"],["AD","9D"],["AD","TD"],["AD","JD"],["AD","QD"],["AD","KD"],["AD","AC"],["AD","2C"],["AD","3C"],["AD","4C"],["AD","5C"],["AD","6C"],["AD","7C"],["AD","8C"],["AD","9C"],["AD","TC"],["AD","JC"],["AD","QC"],["AD","KC"],
    ["2D","3D"],["2D","4D"],["2D","5D"],["2D","6D"],["2D","7D"],["2D","8D"],["2D","9D"],["2D","TD"],["2D","JD"],["2D","QD"],["2D","KD"],["2D","AC"],["2D","2C"],["2D","3C"],["2D","4C"],["2D","5C"],["2D","6C"],["2D","7C"],["2D","8C"],["2D","9C"],["2D","TC"],["2D","JC"],["2D","QC"],["2D","KC"],
    ["3D","4D"],["3D","5D"],["3D","6D"],["3D","7D"],["3D","8D"],["3D","9D"],["3D","TD"],["3D","JD"],["3D","QD"],["3D","KD"],["3D","AC"],["3D","2C"],["3D","3C"],["3D","4C"],["3D","5C"],["3D","6C"],["3D","7C"],["3D","8C"],["3D","9C"],["3D","TC"],["3D","JC"],["3D","QC"],["3D","KC"],
    ["4D","5D"],["4D","6D"],["4D","7D"],["4D","8D"],["4D","9D"],["4D","TD"],["4D","JD"],["4D","QD"],["4D","KD"],["4D","AC"],["4D","2C"],["4D","3C"],["4D","4C"],["4D","5C"],["4D","6C"],["4D","7C"],["4D","8C"],["4D","9C"],["4D","TC"],["4D","JC"],["4D","QC"],["4D","KC"],
    ["5D","6D"],["5D","7D"],["5D","8D"],["5D","9D"],["5D","TD"],["5D","JD"],["5D","QD"],["5D","KD"],["5D","AC"],["5D","2C"],["5D","3C"],["5D","4C"],["5D","5C"],["5D","6C"],["5D","7C"],["5D","8C"],["5D","9C"],["5D","TC"],["5D","JC"],["5D","QC"],["5D","KC"],
    ["6D","7D"],["6D","8D"],["6D","9D"],["6D","TD"],["6D","JD"],["6D","QD"],["6D","KD"],["6D","AC"],["6D","2C"],["6D","3C"],["6D","4C"],["6D","5C"],["6D","6C"],["6D","7C"],["6D","8C"],["6D","9C"],["6D","TC"],["6D","JC"],["6D","QC"],["6D","KC"],
    ["7D","8D"],["7D","9D"],["7D","TD"],["7D","JD"],["7D","QD"],["7D","KD"],["7D","AC"],["7D","2C"],["7D","3C"],["7D","4C"],["7D","5C"],["7D","6C"],["7D","7C"],["7D","8C"],["7D","9C"],["7D","TC"],["7D","JC"],["7D","QC"],["7D","KC"],
    ["8D","9D"],["8D","TD"],["8D","JD"],["8D","QD"],["8D","KD"],["8D","AC"],["8D","2C"],["8D","3C"],["8D","4C"],["8D","5C"],["8D","6C"],["8D","7C"],["8D","8C"],["8D","9C"],["8D","TC"],["8D","JC"],["8D","QC"],["8D","KC"],
    ["9D","TD"],["9D","JD"],["9D","QD"],["9D","KD"],["9D","AC"],["9D","2C"],["9D","3C"],["9D","4C"],["9D","5C"],["9D","6C"],["9D","7C"],["9D","8C"],["9D","9C"],["9D","TC"],["9D","JC"],["9D","QC"],["9D","KC"],
    ["TD","JD"],["TD","QD"],["TD","KD"],["TD","AC"],["TD","2C"],["TD","3C"],["TD","4C"],["TD","5C"],["TD","6C"],["TD","7C"],["TD","8C"],["TD","9C"],["TD","TC"],["TD","JC"],["TD","QC"],["TD","KC"],
    ["JD","QD"],["JD","KD"],["JD","AC"],["JD","2C"],["JD","3C"],["JD","4C"],["JD","5C"],["JD","6C"],["JD","7C"],["JD","8C"],["JD","9C"],["JD","TC"],["JD","JC"],["JD","QC"],["JD","KC"],
    ["QD","KD"],["QD","AC"],["QD","2C"],["QD","3C"],["QD","4C"],["QD","5C"],["QD","6C"],["QD","7C"],["QD","8C"],["QD","9C"],["QD","TC"],["QD","JC"],["QD","QC"],["QD","KC"],
    ["KD","AC"],["KD","2C"],["KD","3C"],["KD","4C"],["KD","5C"],["KD","6C"],["KD","7C"],["KD","8C"],["KD","9C"],["KD","TC"],["KD","JC"],["KD","QC"],["KD","KC"],
    ["AC","2C"],["AC","3C"],["AC","4C"],["AC","5C"],["AC","6C"],["AC","7C"],["AC","8C"],["AC","9C"],["AC","TC"],["AC","JC"],["AC","QC"],["AC","KC"],
    ["2C","3C"],["2C","4C"],["2C","5C"],["2C","6C"],["2C","7C"],["2C","8C"],["2C","9C"],["2C","TC"],["2C","JC"],["2C","QC"],["2C","KC"],
    ["3C","4C"],["3C","5C"],["3C","6C"],["3C","7C"],["3C","8C"],["3C","9C"],["3C","TC"],["3C","JC"],["3C","QC"],["3C","KC"],
    ["4C","5C"],["4C","6C"],["4C","7C"],["4C","8C"],["4C","9C"],["4C","TC"],["4C","JC"],["4C","QC"],["4C","KC"],
    ["5C","6C"],["5C","7C"],["5C","8C"],["5C","9C"],["5C","TC"],["5C","JC"],["5C","QC"],["5C","KC"],
    ["6C","7C"],["6C","8C"],["6C","9C"],["6C","TC"],["6C","JC"],["6C","QC"],["6C","KC"],
    ["7C","8C"],["7C","9C"],["7C","TC"],["7C","JC"],["7C","QC"],["7C","KC"],
    ["8C","9C"],["8C","TC"],["8C","JC"],["8C","QC"],["8C","KC"],
    ["9C","TC"],["9C","JC"],["9C","QC"],["9C","KC"],
    ["TC","JC"],["TC","QC"],["TC","KC"],
    ["JC","QC"],["JC","KC"],
    ["QC","KC"]
]


CARD_NO_RANK            = 0
CARD_HIGH_CARD          = 1
CARD_ONE_PAIR           = 2
CARD_TWO_PAIR           = 3
CARD_THREE_OF_A_KIND    = 4
CARD_STRAIGHT           = 5
CARD_FLUSH              = 6
CARD_FULLHOUSE          = 7
CARD_FOUR_OF_A_KIND     = 8
CARD_FLUSH_STRAIGHT     = 9
CARD_ROYAL_FLUSH        = 10


listCardRankString = [
    "CARD_NO_RANK",
    "CARD_HIGH_CARD",
    "CARD_ONE_PAIR",
    "CARD_TWO_PAIR",
    "CARD_THREE_OF_A_KIND",
    "CARD_STRAIGHT",
    "CARD_FLUSH",
    "CARD_FULLHOUSE",
    "CARD_FOUR_OF_A_KIND",
    "CARD_FLUSH_STRAIGHT",
    "CARD_ROYAL_FLUSH"
]


def card_term_to_num(cards_term):
    return [map_card_term_to_num[x] for x in cards_term]


def card_num_to_term(cards_value):
    return [map_card_num_to_term[x] for x in cards_value]


def card_term_to_value(cards_term):
    return [map_card_to_value[x[0]] for x in cards_term]


def get_card_value(x):
    return map_card_to_value[x[0]]


def get_flush_info(cards):
    suit = {
        "S" : 0,
        "H" : 0,
        "D" : 0,
        "C" : 0
    }
    
    flush_info = {
        "suit" : "",
        "cards" : []
    }
    
    for x in cards:
        flush_suit = x[1]
        suit[flush_suit] += 1
        if suit[flush_suit] == 5:
            flush_info["suit"] = flush_suit
            break
    
    if flush_info["suit"]:
        for x in cards:
            if x[1] == flush_info["suit"]:
                flush_info["cards"] += [x]
    
    return flush_info


def get_straight_info(cards_value):
    cards_bit = 0
    for x in cards_value:
        cards_bit |= (1 << x)
    
    if cards_bit & 0x4000:
        cards_bit |= 0x0002
    
    straight_key = 0x7C00
    for i in range(10):
        if straight_key & cards_bit == straight_key:
            return 14 - i
        else:
            cards_bit <<= 1
    
    return 0


def get_seven_set_rank(cards_info):
    # ABCDEFG
    # CARD_HIGH_CARD
    # CARD_STRAIGHT
    # CARD_FLUSH
    # CARD_FLUSH_STRAIGHT
    # CARD_ROYAL_FLUSH
    
    cards_rank = {
        "rank" : CARD_NO_RANK,
        "info" : []
    }
    
    flush_info = cards_info["flush"]
    straight_info = cards_info["straight"]
    
    if flush_info["suit"]:
        flush_straight_info = cards_info["flush_straight"]
        if flush_straight_info:
            if flush_straight_info == 14:
                cards_rank["rank"] = CARD_ROYAL_FLUSH
            else:
                cards_rank["rank"] = CARD_FLUSH_STRAIGHT
                cards_rank["info"] = [flush_straight_info]
        else:
            cards_rank["rank"] = CARD_FLUSH
            cards_rank["info"] = card_term_to_value(cards_info["flush"]["cards"][0:5])
    elif straight_info:
        cards_rank["rank"] = CARD_STRAIGHT
        cards_rank["info"] = [straight_info]
    else:
        cards_rank["rank"] = CARD_HIGH_CARD
        cards_rank["info"] = cards_info["value"][0:5]
    
    return cards_rank
    
    
def get_six_set_rank(cards_info):
    # AABCDEF
    # CARD_ONE_PAIR
    # CARD_STRAIGHT
    # CARD_FLUSH
    # CARD_FLUSH_STRAIGHT
    # CARD_ROYAL_FLUSH
    
    cards_rank = {
        "rank" : CARD_NO_RANK,
        "info" : []
    }
    
    flush_info = cards_info["flush"]
    straight_info = cards_info["straight"]
    
    if flush_info["suit"]:
        flush_straight_info = cards_info["flush_straight"]
        if flush_straight_info:
            if flush_straight_info == 14:
                cards_rank["rank"] = CARD_ROYAL_FLUSH
            else:
                cards_rank["rank"] = CARD_FLUSH_STRAIGHT
                cards_rank["info"] = [flush_straight_info]
        else:
            cards_rank["rank"] = CARD_FLUSH
            cards_rank["info"] = card_term_to_value(cards_info["flush"]["cards"][0:5])
    elif straight_info:
        cards_rank["rank"] = CARD_STRAIGHT
        cards_rank["info"] = [straight_info]
    else:
        cards_rank["rank"] = CARD_ONE_PAIR
        cards_rank["info"] = cards_info["two"] + cards_info["one"][0:3]
    
    return cards_rank
    
    
def get_five_set_rank(cards_info):
    # AABBCDE
    # AAABCDE
    # CARD_TWO_PAIR
    # CARD_THREE_OF_A_KIND
    # CARD_STRAIGHT
    # CARD_FLUSH
    # CARD_FLUSH_STRAIGHT
    # CARD_ROYAL_FLUSH
    
    cards_rank = {
        "rank" : CARD_NO_RANK,
        "info" : []
    }
    
    flush_info = cards_info["flush"]
    straight_info = cards_info["straight"]
    
    if flush_info["suit"]:
        flush_straight_info = cards_info["flush_straight"]
        if flush_straight_info:
            if flush_straight_info == 14:
                cards_rank["rank"] = CARD_ROYAL_FLUSH
            else:
                cards_rank["rank"] = CARD_FLUSH_STRAIGHT
                cards_rank["info"] = [flush_straight_info]
        else:
            cards_rank["rank"] = CARD_FLUSH
            cards_rank["info"] = card_term_to_value(cards_info["flush"]["cards"][0:5])
    elif straight_info:
        cards_rank["rank"] = CARD_STRAIGHT
        cards_rank["info"] = [straight_info]
    elif cards_info["two"]:
        cards_rank["rank"] = CARD_TWO_PAIR
        cards_rank["info"] = cards_info["two"] + cards_info["one"][0:1]
    elif cards_info["three"]:
        cards_rank["rank"] = CARD_THREE_OF_A_KIND
        cards_rank["info"] = cards_info["three"] + cards_info["one"][0:2]
    
    return cards_rank
    
    
def get_four_set_rank(cards_info):
    # AABBCCD
    # AAABBCD
    # AAAABCD
    # CARD_TWO_PAIR
    # CARD_FULLHOUSE
    # CARD_FOUR_OF_A_KIND
    
    cards_rank = {
        "rank" : CARD_NO_RANK,
        "info" : []
    }
    
    if cards_info["three"]:
        cards_rank["rank"] = CARD_FULLHOUSE
        cards_rank["info"] = cards_info["three"] + cards_info["two"]
    elif cards_info["four"]:
        cards_rank["rank"] = CARD_FOUR_OF_A_KIND
        cards_rank["info"] = cards_info["four"] + cards_info["one"][0:1]
    else:
        cards_rank["rank"] = CARD_TWO_PAIR
        if cards_info["two"][2] > cards_info["one"][0]:
            cards_rank["info"] = cards_info["two"]
        else:
            cards_rank["info"] = cards_info["two"][0:2] + cards_info["one"]
    
    return cards_rank
    
    
def get_three_set_rank(cards_info):
    # AAABBCC
    # AAABBBC
    # AAAABBC
    # CARD_FULLHOUSE
    # CARD_FOUR_OF_A_KIND
    
    cards_rank = {
        "rank" : CARD_NO_RANK,
        "info" : []
    }
    
    if cards_info["four"]:
        cards_rank["rank"] = CARD_FOUR_OF_A_KIND
        if cards_info["two"] > cards_info["one"]:
            cards_rank["info"] = cards_info["four"] + cards_info["two"]
        else:
            cards_rank["info"] = cards_info["four"] + cards_info["one"]
    else:
        cards_rank["rank"] = CARD_FULLHOUSE
        if cards_info["two"]:
            cards_rank["info"] = cards_info["three"] + cards_info["two"][0:1]
        else:
            cards_rank["info"] = cards_info["three"]
    
    return cards_rank
    
    
def get_two_set_rank(cards_info):
    # AAAABBB
    # CARD_FOUR_OF_A_KIND
    
    cards_rank = {
        "rank" : CARD_FOUR_OF_A_KIND,
        "info" : cards_info["four"] + cards_info["three"]
    }
    
    return cards_rank
    
    
def get_cards_info(cards):
    cards_value = card_term_to_value(cards)
    cards_info = {
        "cards" : cards,
        "value" : cards_value,
        "set" : len(set(cards_value)),
        "flush" : {"suit" : "", "cards" : ""},
        "straight" : 0,
        "flush_straight" : 0,
        "one" : [],
        "two" : [],
        "three" : [],
        "four" : []
    }
    
    cards_set = cards_info["set"]
    if cards_set >= 5:
        cards_info["flush"] = get_flush_info(cards)
        cards_info["straight"] = get_straight_info(cards_value)
        if cards_info["flush"]["suit"] and cards_info["straight"] != 0:
            flush_cards_value = card_term_to_value(cards_info["flush"]["cards"])
            cards_info["flush_straight"] = get_straight_info(flush_cards_value)
    
    x = cards_value[0]
    c = 1
    for y in cards_value[1:] + [0]:
        if x == y:
            c += 1
        else:
            if c == 1:
                cards_info["one"] += [x]
            elif c == 2:
                cards_info["two"] += [x]
            elif c == 3:
                cards_info["three"] += [x]
            elif c == 4:
                cards_info["four"] += [x]
            c = 1
            x = y
    
    return cards_info
    
    
def get_seven_cards_rank(cards):
    cards_info = get_cards_info(cards)
    cards_set = cards_info["set"]
    
    if cards_set == 7:
        return get_seven_set_rank(cards_info)
    elif cards_set == 6:
        return get_six_set_rank(cards_info)
    elif cards_set == 5:
        return get_five_set_rank(cards_info)
    elif cards_set == 4:
        return get_four_set_rank(cards_info)
    elif cards_set == 3:
        return get_three_set_rank(cards_info)
    elif cards_set == 2:
        return get_two_set_rank(cards_info)


def get_my_cards_rank(public_cards, hand_cards):
    cards = public_cards + hand_cards
    cards = sorted(cards, key=get_card_value, reverse=True)
    cards_rank = get_seven_cards_rank(cards)
    
    return cards_rank


def get_win_rate(public_cards, hand_cards, my_cards_rank):
    win_rate = 0.0
    better_hand_cards = 0
    known_cards = public_cards + hand_cards
    
    for sub_hand_cards in all_hand_cards_term:
        if (sub_hand_cards[0] in known_cards) or (sub_hand_cards[1] in known_cards):
            continue
        cards = public_cards + sub_hand_cards
        cards = sorted(cards, key=get_card_value, reverse=True)
        cards_rank = get_seven_cards_rank(cards)
        if cards_rank["rank"] > my_cards_rank["rank"]:
            better_hand_cards += 1
        elif cards_rank["rank"] == my_cards_rank["rank"]:
            if cards_rank["info"] > my_cards_rank["info"]:
                better_hand_cards += 1
    
    win_rate = 1.0 - better_hand_cards / 990.0  # 990 = C(45, 2) = 45 * 22
    
    return win_rate
    
    
def simulate_win_rate(public_cards, hand_cards):
    result = {
        "win_rate" : 0.0,
        "rank_info" : {}
    }
    
    simulated_times = 1081
    
    known_cards = public_cards + hand_cards
    all_cards_term = map_card_term_to_num.keys()
    unknown_cards = list(set(all_cards_term).difference(known_cards))
    len_public_cards = len(public_cards)
    
    if len_public_cards == 3:    # Flop
        simulated_hand_cards = [list(x) for x in itertools.combinations(unknown_cards, 2)]
        random.shuffle(simulated_hand_cards)
        
        win_rate = 0.0
        flop_simulate_times = min(simulated_times, 1081)    # 1081 = C(47,2) = 47*23
        
        for n in range(flop_simulate_times):
            simulated_public_cards = public_cards + simulated_hand_cards[n]
            simulated_cards_rank = get_my_cards_rank(simulated_public_cards, hand_cards)
            if simulated_cards_rank["rank"] == CARD_ROYAL_FLUSH:
                win_rate += 1.0
            else:
                win_rate += get_win_rate(simulated_public_cards, hand_cards, simulated_cards_rank)
        result["win_rate"] = win_rate / flop_simulate_times
        
    elif len_public_cards == 4:    # Turn
        random.shuffle(unknown_cards)
        
        win_rate = 0.0
        turn_simulate_times = min(simulated_times, 46)
        
        for n in range(turn_simulate_times):
            simulated_public_cards = public_cards + [unknown_cards[n]]
            simulated_cards_rank = get_my_cards_rank(simulated_public_cards, hand_cards)
            if simulated_cards_rank["rank"] == CARD_ROYAL_FLUSH:
                win_rate += 1.0
            else:
                win_rate += get_win_rate(simulated_public_cards, hand_cards, simulated_cards_rank)
        result["win_rate"] = win_rate / turn_simulate_times
        
    elif len_public_cards == 5:    # Rover
        result["rank_info"] = get_my_cards_rank(public_cards, hand_cards)
        result["win_rate"] = get_win_rate(public_cards, hand_cards, result["rank_info"])
    
    return result
    
    