for _ in  range(int(input())):
	
	N = int(input())
	
	S = list(map(int,input().split()))
	
	string=0
	for i in range(len(S)-1):
	    if S[i+1]!=S[i]:
	        string+=abs(S[i+1]-S[i])-1
	    else:
	        string+=0
	print(string)
