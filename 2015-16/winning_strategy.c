#include<stdio.h>

int main(){
	int i, start_amount, bet_amount, rounds, toss, current_bet;

	scanf("%d", &start_amount);
	scanf("%d", &bet_amount);
	scanf("%d", &rounds);
	current_bet = bet_amount;
	if (rounds < 1 || rounds > 1000 || bet_amount > start_amount) {
		return 0;
	}
	for (i = 0; i < rounds; i++){
		if (start_amount <= 0){
			break;
		}

		scanf("%d", &toss);

		if (toss == 0){
			start_amount -= current_bet;
			current_bet = (current_bet * 2 < start_amount) ? current_bet * 2 : start_amount;
		}
		else{
			start_amount += current_bet; 
			current_bet = (bet_amount < start_amount) ? bet_amount : start_amount;; 
		}
	}

	if (start_amount <= 0){
		printf("%s\n", "BROKE");
	}
	else{
		printf("%d\n", start_amount);
	}
	return 0;
}