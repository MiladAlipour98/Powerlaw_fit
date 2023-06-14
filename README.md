# Network Analysis and Power Law Fitting

This project focuses on analyzing and fitting the power law distribution to a chosen dataset from the link provided: [http://tuvalu.santafe.edu/~aaronc/powerlaws/data.htm](http://tuvalu.santafe.edu/~aaronc/powerlaws/data.htm). The following tasks will be performed:

## Dataset Selection
Choose a dataset from the provided link for analysis and power law fitting.

## Degree Distribution Analysis
1. Plot the Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of the degree distribution for the selected network. Plot both in normal form and log-log form to visualize the distribution characteristics.

### Normal CDF
![2 cdf](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/f235f4c3-d0f9-4035-b51c-c3116cb80ada)

### Log-Log CDF
![2 log-log cdf](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/52803556-7d80-414f-a930-1edf6bb7c00d)


### Normal PDF
![2 pdf](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/94e5be2b-4f60-4d7f-8013-c9e84a859e81)

### Log-Log PDF
![2 log-log pdf](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/52092c73-02d8-4aa9-adb5-f991ddc9d333)


## Power Law Fitting
1. Fit the Power Law distribution to the PDF and CDF plots using the goodness of fit method.
2. Draw the fitted Power Law distribution along with the original data to visualize the fit quality.

![fitted cdf 3](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/df09a23c-d35d-4062-a3a9-ab31dec2955e)

![fitted pdf 3](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/2462f0fd-b496-4181-9c76-f5dd2bd6974c)


## Configuration Model Network Construction
1. Follow the steps described in the book to build a network using the Configuration Model method.
2. Write the code for the different steps of this method.
3. Use the degree sequence 𝑘=(1,1,1,1,1,1,1,2,2,2,2,3,3) to construct the network using the Configuration Model method.
4. Visualize the constructed network.

![Figure_1](https://github.com/MiladAlipour98/Powerlaw_fit/assets/105122009/416ca3c7-53ad-4109-8ddd-a6d61062d20c)

## Dependencies
- Python
- Appropriate Python packages for network analysis, power law fitting, and visualization (e.g., NetworkX, SciPy, Matplotlib)

## Usage
1. Clone the project repository.
2. Install the required dependencies, including Python and the necessary packages for network analysis and visualization.
3. Select a dataset from the provided link.
4. Run the provided Python scripts for degree distribution analysis, power law fitting, and network construction.
5. Examine the generated plots and analysis results for the selected dataset and network construction.

This project aims to provide insights into network analysis techniques, power law fitting, and network construction using the Configuration Model method. It facilitates understanding of degree distributions and their characteristics, as well as the assessment of power law fits and the construction of networks with specific degree sequences.
