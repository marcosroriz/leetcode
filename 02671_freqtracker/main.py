from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.raw_map = defaultdict(int)
        self.freq_map = defaultdict(list)

    def add(self, number: int) -> None:
        curr_freq = self.raw_map[number]
        if curr_freq > 0:
            self.freq_map[curr_freq].remove(number)
        
        curr_freq += 1
        self.raw_map[number] = curr_freq
        self.freq_map[curr_freq].append(number)
        

    def deleteOne(self, number: int) -> None:
        if self.raw_map[number] > 0:
            curr_freq = self.raw_map[number]
            self.freq_map[curr_freq].remove(number)
            
            curr_freq -= 1
            self.raw_map[number] = curr_freq
            self.freq_map[curr_freq].append(number)
        

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq_map[frequency]) > 0

if __name__ == "__main__":
    frequencyTracker = FrequencyTracker()
    frequencyTracker.add(3); 
    frequencyTracker.add(3); 
    print(frequencyTracker.hasFrequency(2)); 
