
def makeChange(goal, coins):
    wallets = [[coin] for coin in coins]    # separa cada valor da lista individualmente
    newWallet = []
    result = []


    while wallets:  #enquanto wallets está cheia
        for item in wallets:    # para cada iten dentro de wallets
            s = sum(item)   # retira cada moeda de dentro da lista
            for coin in coins:  # para cada valor dentro da lista coins
                if coin >= item[-1]:    # se o valor atual de coin for maior ou igual ao último valor de item
                    if s+coin < goal:      # e se a soma dos valores de S e de Coin forem menores que o objetivo
                        newWallet.append(item+[coin])   # descarte em uma outra lista
                    elif s+coin == goal:    # se não, se a soma for igual ao objetivo
                        result.append(item+[coin])  # guarde os resultados
        wallets = newWallet # iguale para que possa ter outra iteração
        newWallet = []  # descarte o que já existir em newWallet
    
    # Agora a parte da exibição
    for i in range(len(result)):  # percorra todo o array
        newResult = [result[i].count(25), result[i].count(10), result[i].count(5), result[i].count(1)]  # conte quantas vezes cada número aparece
        print(newResult)
            


if __name__ == "__main__":
    goal = 12
    coins = [25,10,5,1]
    makeChange(goal, coins)
