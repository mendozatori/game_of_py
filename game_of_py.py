# Life of Py


# imports
import random
import turtle

# CONSTANTS
COLLEGE_TUITION = 40000.00

# job dictionary
college_jobs = {'Veterinarian': [80000, 35000],
                'Lawyer': [90000, 40000],
                'Doctor': [100000, 45000],
                'Software Developer': [110000, 46000]}

work_jobs = {'Hair Stylist': [30000, 10000],
             'Mechanic': [30000, 10000],
             'Salesperson': [20000, 5000],
             'Police Officer': [40000, 15000]}


def main():
    # local variable
    USER_RUNNING_BALANCE = 10000.00
    CONSOLE_RUNNING_BALANCE = 10000.00

    # intro to game
    print("-------------Life of Py----------------")

    # called on functions
    start_game()
    initial_path(USER_RUNNING_BALANCE, CONSOLE_RUNNING_BALANCE)


def start_game():
    # welcome statement
    print("Welcome to the Life of Py, an interactive game where YOU decide your fate!\n"
          "Along the way you will make some decisions that will determine where you end up!\n"
          "Objective: to win more money than the console based off of your decisions\n"
          "Let's play!")
    # ask user for name
    name = input("Please enter your name: ")
    print("Welcome, ", name)
    # ask user for gender
    while True:
        gender = input("Please enter M for male or F for female? ")
        if gender not in ('M', 'F'):
            print("Error: Please enter vaild value.")
        else:
            break
    print("Remember that you are playing against the console! \n"
          "You and your opponent will be given $10,000 as your starting balance.")
    print("")
    # print user profile
    print("-----------------User Profile---------------\n"
          "Name: ", name + "\n"
          "Gender: ", gender + "\n"
          "Account Balance: $10,0000.00")
    # break
    print("")
    input("Press enter to continue.")


# function to allow user to determine path
def initial_path(userBalance, consoleBalance):
    # statement about path choices
    print("")
    print("It is now time to decide your path. You can choose to go to college or go straight to work.\n"
          "There are pros and cons to both. With college you will access to jobs with higher salaries but you\n"
          "will have to also take out a $40,000 loan that will be repaid as you make money. However, if\n"
          "you decide to go straight to work you can start earning money right away and it's free! The choice is yours!")
    # ask user to determine their path
    path = input("Please type 'c' for college or 'w' for work: ")
    # console gets random path
    path_console = ['college', 'work']
    path_console_choice = random.choice(path_console)
    print("")
    print("Your opponent (the console) chose " + path_console_choice)
    # functions to perform depending on the chosen path
    while True:
        # if user picks college
        if path == 'c':
            user_bal, console_bal, user_sal = college_path(userBalance, consoleBalance)
            break
       # if user picks work
        elif path == 'w':
            user_bal, user_sal = work_path(userBalance)
            break
        else:
            print("Please enter a valid value!")
            path = input("Please type 'c' for college or 'w' for work: ")

    # path functions to perform for console
    # if console chooses college
    if path_console_choice == 'college':
        console_bal1, console_sal = college_path_console(console_bal)
    #if console chooses work
    elif path_console_choice == 'work':
        console_bal1, console_sal = work_path_console(consoleBalance)

    # after work/college come together on the life path
    life_path(user_bal, console_bal1, user_sal, console_sal)


def college_path(userBalance1, consoleBalance1):
    print("")
    print("Congratulations! You've made it to college!")
    print("You have opted to borrow $40,000 from the bank. Your bank\n"
          "account will show up as negative for now but will turn positive as\n"
          "soon as you get your first paycheck.")
    # adjust balance for college loan
    userBalance1 -= COLLEGE_TUITION

    # print balance
    print("")
    print("Your current balance: " + '${:,.2f}'.format(userBalance1))

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # random event
    # returns new balances
    user_bal1, console_bal1 = good_random_chance(userBalance1, consoleBalance1)

    # user graduates from college
    print("")
    print("It's graduation day!")
    print("Congrats grad! Now time to pick a job!")

    # user picks random number
    initial_job = int(input("Pick a number 1-4 to determine your fate! "))
    # random job chosen
    user_initial_job = random.choice(list(college_jobs))
    # only let user enter numbers 1-4
    if initial_job >= 1 and initial_job <= 4:
        print("Your chosen job is a " + user_initial_job)
    else:
        print("Please enter a valid number!")
        initial_job = input("Pick a number 1-4 to determine your fate: ")
        print("")
    # variable for salary
    user_salary = college_jobs[user_initial_job][0]
    # print user career profile
    print("--------Career Profile--------")
    print("Career: ", user_initial_job)
    print("Salary: ", '${:,.2f}'.format(user_salary))
    print("")

    # if statements for careers
    # pops up Life of Py job cards
    if user_initial_job == 'Veterinarian':
        vet = "C:/Users/vmendoza/Desktop/Python_Proj/vet.gif"
        screen = turtle.Screen()
        screen.addshape(vet)
        turtle.shape(vet)
    elif user_initial_job == 'Lawyer':
        lawyer = "C:/Users/vmendoza/Desktop/Python_Proj/lawyer.gif"
        screen = turtle.Screen()
        screen.addshape(lawyer)
        turtle.shape(lawyer)
    elif user_initial_job == 'Doctor':
        doctor = "C:/Users/vmendoza/Desktop/Python_Proj/doctor.gif"
        screen = turtle.Screen()
        screen.addshape(doctor)
        turtle.shape(doctor)
    elif user_initial_job == 'Software Developer':
        software_developer = "C:/Users/vmendoza/Desktop/Python_Proj/software_developer.gif"
        screen = turtle.Screen()
        screen.addshape(software_developer)
        turtle.shape(software_developer)

    turtle.exitonclick()

    # call on payday function
    user_bal2 = payday(user_salary, user_bal1)

    # return the most recent balances
    return user_bal2, console_bal1, user_salary


def college_path_console(consoleBalance1):
    # subtract college tuition from balance
    consoleBalance1 -= COLLEGE_TUITION
    # pick random job for the console
    console_initial_job = random.choice(list(college_jobs))
    # variable for console salary
    salary_console = college_jobs[console_initial_job][0]
    # print console career profile
    print("")
    print("Your opponents job is a " + console_initial_job + "!")
    print("--------Opponent Career Profile--------")
    print("Career: " + console_initial_job)
    print("Salary: ", '${:,.2f}'.format(salary_console))

    # call on payday for console
    payday_console(salary_console, consoleBalance1)

    # return most recent balances for console and salary
    return consoleBalance1, salary_console


def work_path(userBalance1):
    print("")
    print("Congratulations! You've made it into the work force")
    print("It is now time to pick a job!")
    # user enters random number
    initial_job = int(input("Pick a number 1-4 to determine your fate! "))
    # random job chosen
    user_initial_job = random.choice(list(work_jobs))
    # variable for salary
    user_salary = work_jobs[user_initial_job][0]
    # only allow user to enter numbers 1-4
    if initial_job >= 1 and initial_job <= 4:
        print("Your chosen job is a " + user_initial_job)
    else:
        print("Please enter a valid number!")
        initial_job = input("Pick a number 1-4 to determine your fate: ")
        print("")
    # print career profile
    print("--------Career Profile--------")
    print("Career: ", user_initial_job)
    print("Salary: ", '${:,.2f}'.format(user_salary))
    print("")

    # if/then statements for career choice and career cards
    if user_initial_job == 'Hair Stylist':
        hair_stylist = "C:/Users/vmendoza/Desktop/Python_Proj/hair_stylist.gif"
        screen = turtle.Screen()
        screen.addshape(hair_stylist)
        turtle.shape(hair_stylist)
    elif user_initial_job == 'Mechanic':
        mechanic = "C:/Users/vmendoza/Desktop/Python_Proj/mechanic.gif"
        screen = turtle.Screen()
        screen.addshape(mechanic)
        turtle.shape(mechanic)
    elif user_initial_job == 'Salesperson':
        salesperson = "C:/Users/vmendoza/Desktop/Python_Proj/salesperson.gif"
        screen = turtle.Screen()
        screen.addshape(salesperson)
        turtle.shape(salesperson)
    elif user_initial_job == 'Police Officer':
        police = "C:/Users/vmendoza/Desktop/Python_Proj/police_officer.gif"
        screen = turtle.Screen()
        screen.addshape(police)
        turtle.shape(police)

    turtle.exitonclick()

    # call on payday function for user
    user_bal = payday(user_salary, userBalance1)

    # return most recent balances and user salary
    return user_bal, user_salary


def work_path_console(consoleBalance1):
    print("")
    # random job chosen
    console_initial_job = random.choice(list(work_jobs))
    # variable for console salary
    salary_console = work_jobs[console_initial_job][0]
    print("")
    # print career profile
    print("Your opponents job is a " + console_initial_job + "!")
    print("--------Opponent Career Profile--------")
    print("Career: " + console_initial_job)
    print("Salary: ", '${:,.2f}'.format(salary_console))

    # call on payday function for console
    consoleBalance2 = payday_console(salary_console, consoleBalance1)

    # return most recent balance and console salary
    return consoleBalance2, salary_console


def payday(salary, balance):
    print("")
    # add salary to balance
    balance += salary
    # print statements
    print("It's payday!")
    print("New balance: " + '${:,.2f}'.format(balance))

    # return balance
    return balance


def payday_console(salary, balance):
    print("")
    # add salary to balance
    balance += salary
    # print statements
    print("It's payday for your opponent!")
    print("Opponent new balance: " + '${:,.2f}'.format(balance))

    # return balance
    return balance


def life_path(userBalance2, consoleBalance2, userSalary, consoleSalary):
    # break
    print("")
    input("Press enter to continue.")
    print("")
    print("Now back to the life of py...")
    print("")

    # roulette game
    print("You decide to stop at a casino and gamble a bit. Let's see how lucky you are!")
    print("Let's play a game of roulette!")
    # insert roulette game
    # return updated balances
    user_bal1, console_bal1 = roulette_game(userBalance2, consoleBalance2)

    # break
    print("")
    input("Press enter to continue.")

    # payday functions
    # return new user balance
    user_bal2 = payday(userSalary, user_bal1)
    # return new console balance
    console_bal2 = payday_console(consoleSalary, console_bal1)

    # life event statement
    print("")
    print("----------Life Event----------")
    print("You got married! Congrats!")

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # insert random event
    # return updated balances
    user_bal3, console_bal3 = random_chance(user_bal2, console_bal2)

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # kids function
    kids()
    print("")

    # insert random event
    # return updated balances
    user_bal4, console_bal4 = good_random_chance(user_bal3, console_bal3)

    # dice game
    print("")
    print("You decide to stop at a casino AGAIN and gamble a bit. Let's see how lucky you are!")
    print("Let's play game of dice!")
    # insert dice game
    # return updated balances
    user_bal5, console_bal5 = dicegame(user_bal4, console_bal4)

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # insert random event
    # return updated balances
    user_bal6, console_bal6 = random_chance(user_bal5, console_bal5)

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # payday functions
    # returns new user balance
    user_bal7 = payday(userSalary, user_bal6)
    # returns new console balance
    console_bal7 = payday_console(consoleSalary, console_bal6)

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # retirement
    print("")
    print("Congrats you've made it to retirement!")
    print("You've truly had a great life! Let's total up the balances to see who the winner is!")

    # print final balances
    print("")
    print("Your final balance: " + '${:,.2f}'.format(user_bal7))
    print("Opponent final balance: " + '${:,.2f}'.format(console_bal7))
    print("")

    # print statements for winners/losers
    if user_bal7 > console_bal7:
        print("Congrats! You've WON the Life of Py!!\n"
              "Enjoy this virtual high-five!")

    elif console_bal7 > user_bal7:
        print("Sorry! You have lost the Life of Py.\n"
              "Try again next time!")

    else:
        print("It's a TIE! Everyone wins!!")



def random_chance(userBalance3, consoleBalance3):
    print("---------RANDOM CHANCE CARD---------")
    # open .txt file
    chance_file = open('chance.txt', 'r')
    # read file
    chance = chance_file.readlines()
    # random event for user
    random_chance = random.choice(chance).rstrip('\n')
    # random amount for user
    random_chance_currency = random.uniform(100, 1000)
    # print statements
    print("Your random chance: " + random_chance)
    print("This costs you " + '${:,.2f}'.format(random_chance_currency))
    # subtract from balance (for user)
    userBalance3 -= random_chance_currency
    print("")
    # random event for console
    random_chance_console = random.choice(chance).rstrip('\n')
    # random amount for console
    random_chance_currency_console = random.uniform(100, 1000)
    # print statements
    print("Random chance for your opponent: " + random_chance_console)
    print("This costs your opponent " + '${:,.2f}'.format(random_chance_currency_console))
    # subtract amount from balance (for console)
    consoleBalance3 -= random_chance_currency_console

    # return updated balances
    return userBalance3, consoleBalance3


def good_random_chance(userBalance4, consoleBalance4):
    print("---------RANDOM CHANCE CARD---------")
    # open .txt file
    good_chance_file = open('goodchance.txt', 'r')
    # read file
    good_chance = good_chance_file.readlines()
    # random chance for user
    good_random_chance = random.choice(good_chance).rstrip('\n')
    # random amount for user
    good_random_chance_currency = random.uniform(100, 1000)
    # print statements
    print("Your random chance: " + good_random_chance)
    print("You won " + '${:,.2f}'.format(good_random_chance_currency))
    # add to user balance
    userBalance4 += good_random_chance_currency
    print("")
    # random chance for console
    good_random_chance_console = random.choice(good_chance).rstrip('\n')
    # random amount for console
    good_random_chance_currency_console = random.uniform(100, 1000)
    # print statements
    print("Random chance for your opponent: " + good_random_chance_console)
    print("Your opponent won " + '${:,.2f}'.format(good_random_chance_currency_console))
    # add to console balance
    consoleBalance4 += good_random_chance_currency_console

    # return updated balances
    return userBalance4, consoleBalance4


def roulette_game(userBalance3, consoleBalance3):
    print("Cost to play is $200.\n"
          "If you win, you win $800!")
    print("The console will also be playing!")
    # list of colors and range of numbers
    colors = ['black', 'red']
    numbers = list(range(1, 10))
    # random color chosen
    roulette_color = random.choice(colors)
    # random number chosen
    roulette_num = random.choice(numbers)
    # have console pick random color
    roulette_color_console = random.choice(colors)
    # have console pick random number
    roulette_num_console = random.choice(numbers)
    while True:
        # user inputs guess on color
        user_roulette_color = input("Pick a color (black or red): ")
        # error message
        if user_roulette_color not in colors:
            print("Error: Please enter vaild color.")
        else:
            break

    while True:
        # user inputs guess on number
        user_roulette_num = int(input("Pick a number 1-10: "))
        # error message
        if user_roulette_num not in numbers:
            print("Error: Please enter vaild number.")
        else:
            break

    # if statements when user wins or loses game
    if user_roulette_color == roulette_color and user_roulette_num == roulette_num:
        # print statements
        print("Congratulations! You WIN!!\n"
              "$800 will be added to your balance!")
        # add $800 to balance
        userBalance3 += 800.00
    else:
        # print statements
        print("You lose! Better luck next time!")
        print("The ball landed on number " + str(roulette_num) + " in the color " + roulette_color)
        # subtract $200 from balance
        userBalance3 -= 200.00

    # if statements when console wins or loses game
    if roulette_color_console == roulette_color and roulette_num_console == roulette_num:
        print("Your opponent WON!\n"
              "$800 will be added to your opponents balance!")
        # add $800 to balance
        consoleBalance3 += 800.00
    else:
        print("")
        print("The console's time to play!")
        print("The console (your opponent) lost their game!")
        # subtract $200 from balance
        consoleBalance3 -= 200.00

    # break
    print("")
    input("Press enter to continue.")
    print("")

    # print statements
    print("Here is your current balance: ", '${:,.2f}'.format(userBalance3))
    print("This is your opponents balance: ", '${:,.2f}'.format(consoleBalance3))

    # return updated balances
    return userBalance3, consoleBalance3


def kids():
    # statement explaining game
    print("It's time to see if you're lucky enough to be a parent!")
    print("Roll the dice to determine your fate.\n"
          "0-1: no kid\n"
          "2-3: 1 kid\n"
          "4-5: twins\n"
          "6: triplets\n")

    # insert dice game
    min = 1
    max = 6

    # allow user to roll
    roll = input("Enter to roll the dice")

    # pick random number
    number = random.randint(min, max)

    # print what user rolled
    print("You roll: ", number)

    # if statements/print statments for outcomes
    if number == 1:
        print("You have no kids!")
    elif number in range(2, 4):
        print("You have 1 kid!")
    elif number in range(3, 5):
        print("You have twins!!")
    elif number == 6:
        print("You have triplets!!!")

    # break
    print("")
    input("Press enter to continue.")
    print("")


def dicegame(userBalance5, consoleBalance5):
    print("You will roll the dice 3 times!")
    print("Whoever has the higher number will win $100 from the other!")

    # call on player function
    playerc = player()
    # print total
    print("")
    print("Your total is", playerc)
    print("")

    # call on computer function
    computerc = computer()
    # print computer total
    print("")
    print("The computer total is", computerc)
    print("")

    # call on compare function to determine winner
    compare(playerc, computerc)

    # if statements to update balances
    if playerc > computerc:
        userBalance5 += 100.00
        consoleBalance5 -= 100.00
    elif computerc > playerc:
        consoleBalance5 += 100.00
        userBalance5 -= 100.00
    else:
        "It's a tie, no one loses money and everyone WINS!"

    # return updated balances
    return userBalance5, consoleBalance5


# part of dice game
def player():
    # initialize total
    player_total = 0
    # roll 3 times
    for count in range(3):
        print("")
        # pick random number each time
        number = random.randint(1, 6)
        # allow user to roll
        roll = input("Enter to roll the dice")
        # print what they rolled
        print("You roll:", number)

        # update player total
        player_total += number

    # return player total
    return player_total


# part of dice game
def computer():
    # initialize total
    computer_total = 0
    # roll 3 times
    for count in range(3):
        # pick random number
        number = random.randint(1, 6)
        # print what computer rolled
        print("The computer roll:", number)

        # update computer total
        computer_total += number

    # return computer total
    return computer_total


# part of dice game
def compare(p, c):
    # if statements to determine who wins
    if p > c:
        print("You win!")
    elif c > p:
        print("Computer wins!")


# call on main function
main()
