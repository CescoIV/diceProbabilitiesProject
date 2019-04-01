#Scroll down to start() function to follow code flow

def findPartitions(n):
    #code that finds integer partitions of a number's sums i.e. 6 = [3,3], [4,2] etc.
    final = []
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1

        while x <= y:
            a[k] = x
            y -= x
            k += 1  
        a[k] = x + y

        final.append(a[:k + 1])

    return final

def generateSideProbs(r, diceNum, diceSideNum):
  sideSums = {}
  for i in r:
    # filter every partition array to diceNum length (can't have more than 2 nums in a partition if I only have 2 dices)
    #also filter out paritions that have a num > max diceSides

    parts = findPartitions(i)
    flat_list = []
    
    for sublist in parts:
        for item in sublist:
            flat_list.append(item)
    parts = list(filter(lambda x: len(x) == diceNum and x[1] <= diceSideNum, parts))

    sideSums[i] = parts
  return sideSums

def generatePercents(d):
  #find total combinations
  total = 0
  for a,b in d.iteritems():
    total += len(b)
  #use the total to find the chance percentage of a number based on its partitions
  for a,b in d.iteritems():
    cent = (len(b)/float(total)) *100
    cent = round(cent,2)
    print("Your probability of rolling the sum " + str(a) + " is " +  str(cent) + "%")

def start():
  diceNum = 2
  leastNum = 1 * diceNum # the script will always start at the minimum sum of all die we can roll
  diceSideNum = 6

  r = range(leastNum, diceNum * diceSideNum + 1)
  
  nums = generateSideProbs(r, diceNum, diceSideNum)
  generatePercents(nums)

start()