import entropy
import average_entropy
import information_gain

print("Entropy = " + str(entropy.calculate([2,3])))
print("Average Entropy = " + str(average_entropy.calculate([[2,3],[4,0],[3,2]])))			
print("Information gain = " + str(information_gain.calculate([[2,3],[4,0],[3,2]])))