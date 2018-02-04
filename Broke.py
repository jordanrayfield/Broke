#most updated code 1:04 am
while True:
    #saveAmount = int(input("how much do you want to save per year?"))
    moneySaved = int(input("How much money do you have saved up? "))
    saveRate = float(input("Enter the percentage rate (1-99%) you want to save per week: "))
    incomeRate = str(input("Do you make money per hour or by weekly allowance? 'h'(hourly) / 'w'(weekly): "))
    #incomeType ="allowance"
    if incomeRate == "h" or incomeRate == "H":
        #Suggestion: just say incomeType ="job"
        hourMoney = int(input("How much money do you make per hour? "))
        hourCheck = int(input("How many hours do you work a week? "))
        weeklySpent = int(input("How much do you spend per week? "))
        weeklyIncome = hourMoney * hourCheck
        #take note of lines 19 to 22 because they might have weird interactions
        weeklyTotal = moneySaved + weeklyIncome 
        weeklySavings = weeklyTotal - weeklySpent
        weekCosted = weeklySpent / weeklyTotal
        weeklyEndCost = weeklyTotal - weeklySpent
        if weeklySpent >= weeklyIncome - (weeklyIncome * (saveRate / 100)):
            print("Your expenditures are cutting into your saving budget! The max you should spend is 70% of your total budget." )
            print("You spent " + str(weekCosted * 100) +  "% of your weekly budget this week")
            print("Your weekly income is: $" + str(weeklyIncome - weeklySpent))
            print("Total balance for the next week: $" + str(weeklyTotal))
            restart = str(input("Do you want to restart? [Y/N]: "))
            if restart == "Y" or restart == "y":
                continue
            elif restart == "N" or restart == "n":
                print("Good luck budgeting!")
                break
            else:
                print("Good luck budgeting!")
        else:
            print("Good job, you stayed within your budget this week!")
            print("You spent " + str(weekCosted * 100) +  "% of your weekly budget this week")
            print("Your weekly savings is: $" + str(weeklyIncome - weeklySpent))
            print("Total balance for the next week:$" + str(weeklyTotal))
            
        desiredYearlySavings = int(input("How much money would you like to save in the next year?"))
        while desiredYearlySavings > (weeklyEndCost * 52):          
            desiredYearlySavings = int(input("Remember, your yearly savings goal must be within reach based on your current budget"))
            
        
        print("In order to reach this goal, you must save $" + str(desiredYearlySavings / 52) + " per week.")
        break
        
    elif incomeRate == "w" or incomeRate == "W":
        #Sugestin: just say incomeType ="allowance"
        weeklyAllowance = int(input("How much money do you get per week? "))
        weeklySpent = int(input("How much do you spend per week? "))
        weeklySavings = weeklyAllowance - weeklySpent
        weeklyTotal = moneySaved + weeklyIncome 
        weekCosted = weeklySpent / weeklyTotal
        weeklyEndCost = weeklyTotal - weeklySavings
        if weeklySpent >= weeklyIncome - (weeklyAllowance * (saveRate / 100 )):
                print("Your expenditures are cutting into your saving budget! The max you should spend is 70% of your total budget")
                print("You spent " + str(weekCosted * 100) +  "% of your weekly budget this week")
                print("Your weekly income is: $" + str(weeklyIncome - weeklySpent))
                print("Total balance: $" + str(weeklyTotal))
                restart = str(input("Do you want to restart? [Y/N]: "))
                if restart == "Y" or restart == "y":
                    continue
                elif restart == "N" or restart == "n":
                    print("Good luck budgeting!")
                    break
                else:
                    print("Good luck budgeting!")
        else:
            print("Good job, you stayed within your budget this week!")
            print("You spent " + str(weekCosted * 100) +  "% of your weekly budget this week")
            print("Your weekly allowance is " + str(weeklyAllowance))
            
        desiredYearlySavings = int(input("How much money would you like to save in the next year?"))
        while desiredYearlySavings > (weeklyEndCost * 52):
        
             desiredYearlySavings = int(input("Remember, your yearly savings goal must be within reach based on your current budget"))

        
        print("In order to reach this goal, you must save at least $" + str(desiredYearlySavings / 52) + " per week.")
        break
        
    else: 
        print("Error, please make sure you entered the correct input.(h/H or w/W)")
        continue
    
    
    