import numpy as np

def generate_bandit_distributions(N, mean_range=(-10, 10), std_range=(1, 5)):
    bandit_distributions = []
    for _ in range(N):
        mean = np.random.uniform(*mean_range)
        std = np.random.uniform(*std_range)
        distribution = np.random.normal(mean, std, size=1000)
        bandit_distributions.append(distribution)
    return bandit_distributions

def simulate_guests_playing(N, M, bandit_distributions, Tmax=10000):
    total_winnings = np.zeros(M, dtype=float)
    best_machine_global = None
    for _ in range(Tmax):
        guest_results = np.zeros((N, M), dtype=float)
        for j in range(M):
            chosen_machine = np.random.randint(N)
            
            # Losujemy, czy gracz wygrywa czy przegrywa z pewnym prawdopodobieństwem
            win_prob = np.random.rand()
            if win_prob < 0.5:
                plays_results = np.random.choice(bandit_distributions[chosen_machine], 1)
                mean_result = plays_results[0]
            else:
                mean_result = np.random.uniform(-10, 10)  # Przegrana - losujemy wartość z zakresu [-10, 10]
                
            guest_results[chosen_machine, j] = mean_result
            total_winnings[j] += mean_result
            
        best_machine_global = np.argmax(total_winnings)
    
    total_winnings_usd = np.round(total_winnings * 0.01, 2)
    
    return guest_results, total_winnings_usd, best_machine_global

N = 100  # Liczba jednorękich bandytów
M = 50   # Liczba gości
Tmax = 10000  # Liczba kroków w pętli

bandit_distributions = generate_bandit_distributions(N)

guest_results, total_winnings_usd, best_machine_global = simulate_guests_playing(N, M, bandit_distributions, Tmax)

print("Sumaryczne wygrane dla każdego gracza w dolarach (zaokrąglone do dwóch miejsc po przecinku):")
print(total_winnings_usd)

print("Najlepsza maszyna globalnie:", best_machine_global)
