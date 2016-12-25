#include<stdio.h>

int main(){
	int i, score, total = 0, clean = 0;
	for (i = 0; i < 10; i++){
		scanf("%d", &score);
		if (score == 6){
			clean = 1;
			break;
		}
		else{
			total += score;
			if (total >= 30){
				clean = 1;
				break;
			}
		}
	}

	if (clean == 1) {
		printf("CLEAN\n");
	}else{
		printf("DO NOT CLEAN\n");
	}
	
	return 0;
}