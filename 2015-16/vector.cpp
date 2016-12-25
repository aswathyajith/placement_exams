#include <iostream>
#include <vector>

using namespace std;

int v, e;
vector<int> G[1000];
vector<int> visited(e);

int main(){
	int start, end;
	cin>>v>>e;
	
	for (int i=0; i < e; i++){
		cin>>start>>end;
		for (int j=0; j < v; j++){
			G[start].push_back(end);
			G[end].push_back(start);
		}
	}
}