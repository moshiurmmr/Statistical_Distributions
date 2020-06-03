# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# import the Distribution class
from .GenericDistribution import Distribution


class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0, sigma=1):

        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):

        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """

        # Calculate the mean of the data set. Remember that the data set is stored in self.data
        # Change the value of the mean attribute to be the mean of the data set
        # Return the mean of the data set
        self.mean = np.mean(self.data)

        return self.mean

    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set

        """

        #   Calculate the standard deviation of the data set
        #
        #   The sample variable determines if the data set contains a sample or a population
        #   If sample = True, this means the data is a sample.
        #   Keep the value of sample in mind for calculating the standard deviation
        #
        #   Make sure to update self.stdev and return the standard deviation as well
        # """

        if sample:
            number_of_data = len(self.data) - 1
        else:
            number_of_data = len(self.data)
        # convert the data to a numpy array
        data_np = np.array(self.data)
        sigma = np.sqrt(np.sum(np.square(data_np - self.mean)) / number_of_data)
        self.stdev = sigma

        return self.stdev

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        # Plot a histogram of the data_list using the matplotlib package.

        plt.hist(self.data)
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.title('Histogram of the data')

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        # Calculate the probability density function of the Gaussian distribution
        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation
        pdf = 1 / (self.stdev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * (np.square(x - self.mean)
                                                                     * (1 / np.square(self.stdev))))

        return pdf

    def plot_histogram_pdf(self, n_spaces=50):

        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """


        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):

        """Magic method to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """

        # Calculate the results of summing two Gaussian distributions
        #   When summing two Gaussian distributions, the mean value is the sum
        #       of the means of each Gaussian.
        #
        #   When summing two Gaussian distributions, the standard deviation is the
        #       square root of the sum of square ie sqrt(stdev_one ^ 2 + stdev_two ^ 2)

        # create a new Gaussian object
        result = Gaussian()

        # calculate the mean and standard deviation of the sum of two Gaussians
        # mean of the result distribution
        result.mean = self.mean + other.mean
        # standard deviation of the result distribution
        result.stdev = np.sqrt(np.square(self.stdev) + np.square(other.stdev))

        return result

    def __repr__(self):

        """Magic method to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        # TODO: Return a string in the following format -
        # "mean mean_value, standard deviation standard_deviation_value"
        # where mean_value is the mean of the Gaussian distribution
        # and standard_deviation_value is the standard deviation of
        # the Gaussian.
        # For example "mean 3.5, standard deviation 1.3"
        # "mean {}, standard deviation {}".format(self.mean, self.stdev)
        # represent = print("mean {}, standard deviation {}".format(self.mean, self.stdev))

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

