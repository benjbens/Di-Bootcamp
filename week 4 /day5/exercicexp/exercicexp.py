my_str = input("enter words: ")
words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)
































def cash_out(account):

    cash_out = -1 * int(input("how much u cash out: "))
    if cash_out > account:

        print("dont have enought money")
        return

    else:
        account += cash_out
        return cash_out



def deposit(account):

    deposit = int(input("how much u deposit: "))
    account += deposit
    return deposit


# ask_user = input("press o to cash out or press d to deposit:  ")
# transactions = []

# if ask_user == "o":
#    transactions.append(cash_out(account))
    
# if ask_user == "d":
#     transactions.append(deposit(account))

# print(transactions)

account = 5000
transactions = []

while True:

    print(account)
    ask_user = input("press o to cash out or press d to deposit:  ")

    if ask_user == "o":
        transactions.append(cash_out(account))     

    elif ask_user == "d":
        transactions.append(deposit(account))
        
    print(transactions)

    account = account + transactions[-1]










