# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# import the Distribution class
from .GenericDistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    #

    def __init__(self, p=0.2, size=30):
        # store the probability of the distribution in an instance variable p
        self.p = p
        # store the size of the distribution in an instance variable n
        self.n = size
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.p * self.n

        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        standard deviation, sigma = sqrt(n * p * (1 - p))

        """
        self.stdev = np.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = np.sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        x = ['0', '1']
        y = [(1 - self.p) * self.n, self.p * self.n]
        plt.bar(x=x, height=y)
        plt.show()
        plt.xlabel('bins')
        plt.ylabel('data')
        plt.title('Histogram for data')

    def pdf(self, k):

        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function

        pdf for k positive in an n number of trial (with a probability of p) is:
        P (k; p,n) = n!/(k! * (n-k)!) * p^k * (1 - p)^(n-k)
        Returns:
            float: probability density function output
        """
        n = self.n
        pdf = np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k)) * (self.p) ** k * \
              (1 - self.p) ** (n - k)

        return pdf


    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        # Use a bar chart to plot the probability density function from
        # k = 0 to k = n

        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.

        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
        x = []
        y = []
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(x))
        plt.bar(x, y)
        plt.xlabel('Values')
        plt.ylabel('PDF')
        plt.title('PDF of the binomial distribution')

        return x, y

    def __add__(self, other):
        """Function (magic method) to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        # Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        # result.mean = self.mean + other.mean
        # result.stdev = np.sqrt((result.n) * self.p * (1-self.p))
        result.calculate_mean()
        result.calculate_stdev()
        return result

    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function (magic method) to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)


