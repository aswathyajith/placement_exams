#include <stdio.h>
#include <string.h>

int palindrome(char* str, int start, int end){
	if (start >= end)
		return 1;
	else{
		if (str[start] == str[end])
			palindrome(str, start+1, end-1);
		else return 0;
	}
}

int main(){
	char ch, str[250];
	scanf("%s", str);
	int n = strlen(str);
	//printf("%s",str);
	if (palindrome(str, 0, n-1) == 1) printf("PALINDROME\n");
	else printf("NOT PALINDROME\n");
	return 0;
}