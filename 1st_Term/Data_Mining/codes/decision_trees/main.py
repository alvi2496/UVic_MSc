import entropy
import average_entropy
import information_gain

print("Entropy = " + str(entropy.calculate([8,3,1])))
print("Average Entropy = " + str(average_entropy.calculate([[7,2,3],[8,3,1]])))			
print("Information gain = " + str(information_gain.calculate([[2,3],[4,0],[3,2]])))