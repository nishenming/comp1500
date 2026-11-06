# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data = []

        with open(filename, "rt") as infile:
            for line in infile:
                line = line.strip()
                if line != "":
                    self.data.append(float(line))

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        total = 0
        for value in self.data:
            total = total + value

        return total / len(self.data)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        sorted_data = self.data.copy()
        sorted_data.sort()

        size = len(sorted_data)
        middle = size // 2

        if size % 2 == 1:
            return sorted_data[middle]
        else:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
