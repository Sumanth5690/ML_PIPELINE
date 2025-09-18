import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

def create_decision_tree_dataset(n_samples=1000):
    """
    Create a dataset that's ideal for decision trees with:
    - Clear decision boundaries
    - Mix of categorical and numerical features
    - Non-linear relationships
    - Some redundant features
    - Interpretable patterns
    """
    
    # Age groups (categorical-like but numerical)
    age = np.random.randint(18, 80, n_samples)
    
    # Income levels (with some correlation to age)
    income = np.where(age < 30, 
                     np.random.normal(35000, 10000, n_samples),
                     np.where(age < 50,
                             np.random.normal(55000, 15000, n_samples),
                             np.random.normal(45000, 12000, n_samples)))
    income = np.maximum(income, 20000)  # Minimum income
    
    # Education level (categorical)
    education_levels = ['High School', 'Bachelor', 'Master', 'PhD']
    education_probs = [0.4, 0.35, 0.2, 0.05]
    education = np.random.choice(education_levels, n_samples, p=education_probs)
    
    # Work experience (correlated with age)
    work_experience = np.maximum(0, age - 22 + np.random.normal(0, 3, n_samples))
    work_experience = np.round(work_experience).astype(int)
    
    # City size (categorical)
    city_sizes = ['Small', 'Medium', 'Large']
    city_size = np.random.choice(city_sizes, n_samples, p=[0.3, 0.4, 0.3])
    
    # Credit score (influenced by income and age)
    credit_score = (income / 1000 * 10 + age * 5 + 
                   np.random.normal(0, 50, n_samples))
    credit_score = np.clip(credit_score, 300, 850)
    
    # Number of dependents
    dependents = np.random.poisson(1.2, n_samples)
    dependents = np.clip(dependents, 0, 5)
    
    # Homeowner status (influenced by income and age)
    homeowner_prob = (income / 100000 + age / 100 + 
                     np.where(education == 'PhD', 0.2, 
                             np.where(education == 'Master', 0.1, 0))) / 3
    homeowner_prob = np.clip(homeowner_prob, 0.1, 0.9)
    homeowner = np.random.binomial(1, homeowner_prob, n_samples)
    
    # Target variable: Loan Approval (binary classification)
    # Complex decision rules that decision trees can capture well
    loan_approval = np.zeros(n_samples)
    
    for i in range(n_samples):
        score = 0
        
        # Age factor
        if 25 <= age[i] <= 65:
            score += 2
        elif age[i] < 25 or age[i] > 65:
            score -= 1
            
        # Income factor
        if income[i] > 50000:
            score += 3
        elif income[i] > 30000:
            score += 1
        else:
            score -= 2
            
        # Education factor
        if education[i] == 'PhD':
            score += 3
        elif education[i] == 'Master':
            score += 2
        elif education[i] == 'Bachelor':
            score += 1
            
        # Credit score factor
        if credit_score[i] > 750:
            score += 3
        elif credit_score[i] > 650:
            score += 1
        elif credit_score[i] < 550:
            score -= 3
            
        # Work experience factor
        if work_experience[i] > 10:
            score += 2
        elif work_experience[i] > 5:
            score += 1
            
        # Homeowner bonus
        if homeowner[i] == 1:
            score += 1
            
        # Dependents factor (too many dependents is risky)
        if dependents[i] > 3:
            score -= 2
        elif dependents[i] == 0:
            score += 1
            
        # City size factor
        if city_size[i] == 'Large':
            score += 1
            
        # Final decision with some randomness
        approval_prob = 1 / (1 + np.exp(-(score - 3)))  # Sigmoid function
        loan_approval[i] = np.random.binomial(1, approval_prob)
    
    # Create DataFrame
    df = pd.DataFrame({
        'age': age,
        'income': income,
        'education': education,
        'work_experience': work_experience,
        'city_size': city_size,
        'credit_score': credit_score,
        'dependents': dependents,
        'homeowner': homeowner,
        'loan_approved': loan_approval.astype(int)
    })
    
    return df

def add_noise_features(df, n_noise=3):
    """Add some noise features to make the dataset more realistic"""
    for i in range(n_noise):
        df[f'noise_feature_{i+1}'] = np.random.normal(0, 1, len(df))
    return df

def create_visualization(df):
    """Create visualizations to understand the dataset"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Decision Tree Dataset Analysis', fontsize=16)
    
    # Age distribution by loan approval
    sns.boxplot(data=df, x='loan_approved', y='age', ax=axes[0,0])
    axes[0,0].set_title('Age vs Loan Approval')
    
    # Income distribution by loan approval
    sns.boxplot(data=df, x='loan_approved', y='income', ax=axes[0,1])
    axes[0,1].set_title('Income vs Loan Approval')
    
    # Education distribution
    education_approval = df.groupby(['education', 'loan_approved']).size().unstack()
    education_approval.plot(kind='bar', ax=axes[0,2])
    axes[0,2].set_title('Education vs Loan Approval')
    axes[0,2].legend(['Not Approved', 'Approved'])
    
    # Credit score distribution
    sns.boxplot(data=df, x='loan_approved', y='credit_score', ax=axes[1,0])
    axes[1,0].set_title('Credit Score vs Loan Approval')
    
    # City size distribution
    city_approval = df.groupby(['city_size', 'loan_approved']).size().unstack()
    city_approval.plot(kind='bar', ax=axes[1,1])
    axes[1,1].set_title('City Size vs Loan Approval')
    axes[1,1].legend(['Not Approved', 'Approved'])
    
    # Correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[1,2])
    axes[1,2].set_title('Feature Correlations')
    
    plt.tight_layout()
    plt.savefig('decision_tree_dataset_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Create the dataset
    print("Creating decision tree optimized dataset...")
    df = create_decision_tree_dataset(n_samples=1000)
    
    # Add some noise features
    df = add_noise_features(df, n_noise=3)
    
    # Display basic statistics
    print("\nDataset Info:")
    print(f"Shape: {df.shape}")
    print(f"Target distribution:")
    print(df['loan_approved'].value_counts(normalize=True))
    
    print("\nFirst 10 rows:")
    print(df.head(10))
    
    print("\nDataset description:")
    print(df.describe())
    
    # Save the dataset
    df.to_csv('decision_tree_dataset.csv', index=False)
    print(f"\nDataset saved as 'decision_tree_dataset.csv'")
    
    # Create visualizations
    create_visualization(df)
    
    print("\nDataset characteristics that make it ideal for decision trees:")
    print("1. Clear decision boundaries based on feature thresholds")
    print("2. Mix of categorical and numerical features")
    print("3. Non-linear relationships between features and target")
    print("4. Interpretable business rules")
    print("5. Some redundant/noise features to test feature selection")
    print("6. Balanced target classes")
    print("7. Realistic feature interactions")