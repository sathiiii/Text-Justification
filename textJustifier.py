def badness(i, j):
    global screenWidth, words
    totalWidth = sum(len(word) for word in words[i : j]) + len(words[i : j]) - 1
    return float("inf") if totalWidth > screenWidth else (screenWidth - totalWidth) ** 3
    
def argmin(arr):
    return min(range(len(arr)), key=lambda x: arr[x])
    
words = input().split()
screenWidth = int(words.pop(0))
DP = [0] * (len(words) + 1)
breaks = [0] * (len(words) + 1)

for i in range(len(words) - 1, -1, -1):
    temp = [DP[j] + badness(i, j) for j in range(i+1,len(words)+1)]
    index = argmin(temp)
    breaks[i] = index + i + 1
    
def reconstructText(words, breaks):                                                                                     
    lines = []
    linebreaks = []
    i = 0 
    while True:
        linebreaks.append(breaks[i])
        i = breaks[i]
        if i == len(words):
            linebreaks.append(0)
            break
    for i in range( len(linebreaks) ):
        lines.append(' '.join(words[linebreaks[i-1] : linebreaks[i]]).strip())
    return lines

print('\n'.join(reconstruct_text(words, breaks)))
