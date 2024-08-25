 ## 2. Identify the most frequent customers based on their order history
    frequent_customers = order_data['customer_id'].value_counts().reset_index()
    frequent_customers.columns = ['customer_id', 'order_count']

    # Create a bar chart for the top 10 most frequent customers
    top_10_customers = frequent_customers.head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_customers['customer_id'], top_10_customers['order_count'], color='salmon')
    plt.title('Top 10 Most Frequent Customers Based on Order History')
    plt.xlabel('Customer ID')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()