print(r'''
                             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')          
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
directions = input('Type "left" or "right"\n').lower()
if directions == "left":
    print("You've come to the lake. There is an island in the middle of the lake")
    activity = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
elif directions == "right":
    print("Fall into a hole. Game over")
else:
    print("That is not an option, please try again")    
if directions == "left":
  if activity == "wait":
     print("You arrive at the island unharmed. There is a house  with 3 doors")
     door = input('One red, one yellow and one blue. Which colour do you choose?\n').lower()
  elif activity == "swim":
     print("Attacked by trout. Game over.")
  else:
     print("That is not an option, please try again")   
if directions == "left":
  if activity == "wait":
    if door == "yellow":
      print("you found the treasure! you win!!")
    elif door == "red":
      print("Burned by fire. Game over")  
    elif door == "blue":
       print("Eaten by beasts. Game over")
    else:
       print("That is not an option, please try again")                       
