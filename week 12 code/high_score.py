import random #for the name gen
import time
import multiprocessing
from multiprocessing import Process, Queue
# Represents one entry of a list of high scores.
class GameEntry:
    # Create an entry with given name and score.
    def __init__(self, name, score):
        self._name = name
        self._score = score
        # Return the name of the person for this entry.
    def get_name(self):
        return self._name
        # Return the score of this entry.
    def get_score(self):
        return self._score
        # Return string representation of the entry.
    def __str__(self):
        # e.g., '(Bob, 98)'
        return '({0}, {1})'.format(self._name, self._score)


# Fixed-length sequence of high scores in ascending order.
class Scoreboard:
# Initialise scoreboard with given maximum capacity.
    def __init__(self, capacity=10):
        # All entries are initially None.
        self._board = [None] * capacity # reserve space for future scores
        self._n = 0 # number of actual entries
        # Return entry at index k.

    def __getitem__(self, k):
        return self._board[k]
    # Return string representation of the high score list.

    def __str__(self):
        # a for loop 
        return '\n'.join(str(self._board[j])  for j in range(self._n))  + f"\n[] Current number of entries is {self._n}"+ f"\n[] Entries slots left:{len(self._board)-(self._n)}"
    
    def extend(self):
        self._board.extend([None] * len(self._board)) # doubles the size of the board
        print(f"[] Scoreboard extended to {len(self._board)} entries")

    # Consider adding entry to high scores.
    def add(self, entry):
        score = entry.get_score()
        # Own add-on
        # Does new entry qualify as a high score?
        # Yes, if board is not full or score is higher than last entry
        # self.__board[self._n -1] = last entry , basically a list
        #checker if board is full 
        if self._n >= len(self._board):
            print("[] Entry list is full, adding more slots .......")
            self.extend()
        
        qualified = self._n < len(self._board) or score > self._board[self._n - 1].get_score() 
        if qualified:
            if self._n < len(self._board): # no score drops from list
                # so overall number increases
                self._n += 1
            j = self._n - 1 # start at last entry
            while j > 0 and self._board[j-1].get_score() < score:
                # shift entry from j-1 to j
                self._board[j] = self._board[j-1]
                # and decrement j
                j-=1
            # when done, add new entry
            self._board[j] = entry
        else:
            print("[] Entry list is full!")


            







# Done with one
def main():
    board = Scoreboard()
    namebank = ['Rob', 'Mike', 'Rose', 'Jill', 'Jack', 'Anna', 'Paul', 'Bob', 'timmy']
    scorebank = random.randint(100, 2000)
    numberofentries = int(input("Number of entries: "))
    start_time = time.time()

    for _ in range(numberofentries):
        name = random.choice(namebank)
        score = random.randint(100, 2000)
        ge = GameEntry(name, score)
        board.add(ge)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")




# Done with many cores
def core(namebank, n, out_list):
    for _ in range(n):
        name = random.choice(namebank)
        score = random.randint(100, 2000)
        out_list.append(GameEntry(name, score))

def main_parallel():
    from multiprocessing import Manager
    board = Scoreboard()
    namebank = ['Rob', 'Mike', 'Rose', 'Jill', 'Jack', 'Anna', 'Paul', 'Bob', 'timmy']
    numberofentries = int(input("Number of entries: "))
    start_time = time.time()
    num_cores = min(multiprocessing.cpu_count(), numberofentries)
    entries_per_core = numberofentries // num_cores
    remainder = numberofentries % num_cores

    manager = Manager()
    lists = [manager.list() for _ in range(num_cores)]
    processes = []
    for i in range(num_cores):
        n = entries_per_core + (1 if i < remainder else 0)
        p = Process(target=core, args=(namebank, n, lists[i]))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    # Flatten all lists and add to scoreboard
    all_entries = []
    for l in lists:
        all_entries.extend(l)
    for ge in all_entries:
        board.add(ge)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
    #main_parallel()