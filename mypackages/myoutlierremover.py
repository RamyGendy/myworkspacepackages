def remove_outliers(df, columns, iqr_coefficient=1.5):

    """
    Remove numerical outliers by using interquertile range
    
    Args:
        df(pandas dataframe): that has outliers within on of its columns.
        columns(list): list of columns that has the outliers.
        iqr_coefficient(float):(default = 1.5) Scaling factor used to define outliers.
                                the higher the number the less outliers will be clipped

    Returns:
        pandas dataframe clipped from outliers based on the specificed columns.
    
    Examples:
        >> df_with_no_outliers = remove_outliers( dataframe_dataset, ['price'])
               
        >> df_with_no_outliers = remove_outliers( dataframe_dataset, ['price'], 1.5)
        
        >> df_with_no_outliers = remove_outliers( dataframe_dataset, ['price'], 0.5)
        
    """
    # This line calculates the first quartile of the data (the 25th percentile).
    Q1 = df[columns].quantile(0.25) 
    # This line calculates the third quartile of the data (the 75th percentile).
    Q3 = df[columns].quantile(0.75) 
    # Calculates the interquartile range, which is the range within which the middle 50% of the data falls.
    IQR = Q3 - Q1 
    # Any data point less than this value is considered an outlier.
    lower_fence = Q1 - iqr_coefficient * IQR 
    # Any data point more than this value is considered an outlier.
    upper_fence = Q3 + iqr_coefficient * IQR 
    # This line uses boolean indexing to filter the DataFrame.
    # The & operator is used to ensure that both conditions must be met.
    return df[~((df[columns] < lower_fence) | (df[columns] > upper_fence)).any(axis=1)]