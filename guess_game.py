secret_no = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
	    guess = int(input("Guess: "))
	    guess_count += 1
	    if guess == secret_no:
	        print("You won")
	        break
else:
	   print("you failed to guess")