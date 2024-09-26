# Importing necessary modules
import sys

# defining the reducer function for the sum of the layoff_count
def reducer_sumLayoffs():
    # Define a dictionary mapping industries to their corresponding categories
    industry_categories = {
        'Consumer': 'Consumer',
        'Energy': 'Consumer',
        'Food': 'Consumer',
        'Fitness': 'Consumer',
        'Media': 'Consumer',
        'Marketing': 'Consumer',
        'Retail': 'Consumer',
        'Travel': 'Consumer',
        'Education': 'Education',
        'Finance': 'Finance',
        'Healthcare': 'Health',
        'AI': 'IT',
        'Crypto': 'IT',
        'Data': 'IT',
        'Hardware': 'IT',
        'Construction': 'Infrastructure',
        'Infrastructure': 'Infrastructure',
        'Real Estate': 'Infrastructure',
        'Aerospace': 'Manufacturing',
        'Logistics': 'Manufacturing',
        'Manufacturing': 'Manufacturing',
        'Product': 'Manufacturing',
        'Transportation': 'Manufacturing',
        'HR': 'Professional',
        'Legal': 'Professional',
        'Recruiting': 'Professional',
        'Sales': 'Professional',
        'Support': 'Professional',
        'Security': 'Professional',
        'Other': 'Others',
        'Unknown': 'Others'
    }

    # Initialize total counts for each industry category
    category_totals = {category: 0 for category in set(industry_categories.values())}

    # Iterate over each line in the input
    for line in sys.stdin:
        line = line.strip()
        industry, _, layoff_count = line.split('\t')
        
        # Check if layoff_count is not empty
        if layoff_count:
            # Convert layoff_count to an integer
            count = int(layoff_count)
            # Find the category of the industry
            category = industry_categories.get(industry, 'Others')
            # Update the total count for the corresponding category
            category_totals[category] += count

    # Output the total layoffs for each industry category
    for category, total in category_totals.items():
        print(f"{category}\t{total}")

if __name__ == "__main__":
    # Call the reducer function when the script is run directly
    reducer_sumLayoffs()