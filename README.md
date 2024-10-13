#  Data Financial Analysis Project - Investment 

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation Guide](#installation-guide)
4. [Usage Instructions](#usage-instructions)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [Testing](#testing)
8. [Project Structure](#project-structure)
9. [Technologies Used](#technologies-used)
10. [License](#license)
11. [FAQ](#faq)
12. [Contact Information](#contact-information)


---

### Introduction
This program provides an optimal portfolio solution by analyzing market data for six industries. It calculates the minimum variance portfolio, helping investors make informed decisions.

### Features
- Analyze market conditions of various industries.
- Calculate the optimal investment ratio for a portfolio.
- Display expected returns and mean returns for the selected stocks.
- Handle missing data and ensure data accuracy.
---

### Installation Guide
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository/investment-portfolio.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the required data file (`data.xlsx`) is placed in the correct directory.

---

### Usage Instructions
1. Place your `data.xlsx` file containing the raw stock returns data in the root directory.
2. Run the program:
    ```bash
    python main.py
    ```
3. The program will analyze the data and output:
   - Mean returns for the portfolio
   - Optimal stock ratios for minimizing portfolio variance
   - Expected portfolio return
  Example:

The mean returns of those stocks is ... Ratio of stock in portfolio is ... Expected return of this portfolio is ...

---

### Configuration

- You can modify the Excel data file (`data.xlsx`) to include other stocks or industries.
- The program assumes that your data has six industries, with columns representing the returns of each.

---

### Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push the changes to your fork (`git push origin feature-branch`).
5. Create a pull request.

---

### Testing

To test the program, ensure your data file (`data.xlsx`) is correct and run:
```bash
python main.py
```
The program includes built-in assertions to confirm the accuracy of the final results.

---

### Project Structure

- `main.py`: Entry point of the program, which processes the stock data and calculates portfolio ratios.
- `Investment.py`: Contains the `Investment` class, responsible for handling the calculations of stock ratios and returns.
- `data.xlsx`: Excel file containing raw stock return data.

---

## Technologies Used

- Python 3.8+
- Pandas
- NumPy
- Excel (for input data)

---

## License

This project is licensed under the MIT License.

---

## FAQ

**1. What kind of data is required?**  
The program expects an Excel file with returns data for six industries, each represented as a column.

**2. What does the portfolio calculation show?**  
It calculates the minimum variance portfolio, displaying the optimal ratio for each stock and the expected return.

---

## Contact Information

For questions or further information, please contact:
- Name: Boyan Zhang
- Email: your.email@example.com

