letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {}
for key,value in zip(letters,points):
  letter_to_points[key]=value
#print(letter_to_points)

#Add key of " " and a point value of 0
letter_to_points[" "]=0
print(letter_to_points)

#create a function that will take in a word and return how many points that word is worth
#adds the point value of each letter to point_total.If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
def score_word(word):
  point_total=0
  for each in word:
    point_total += letter_to_points.get(each,0)
  return point_total

#Call function with an input of "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Create a dictionary called player_to_words that maps players to a list of the words they have played as follows:
player_to_words={"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
#Create an empty dictionary called player_to_points.
player_to_points = {}

#Iterate through the items in player_to_words. Call each player player and each list of words words.Within your loop, create a variable called player_points and set it to 0.

for key,value in player_to_words.items():
  player_points = 0
  for each in value:
    player_points += score_word(each)
  player_to_points[key]=player_points

print(player_to_points)














