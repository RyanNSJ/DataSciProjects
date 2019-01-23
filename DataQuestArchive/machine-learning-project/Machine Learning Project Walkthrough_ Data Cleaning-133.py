## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv("loans_2007.csv")
print(loans_2007.iloc[0])
print(loans_2007.shape[0])

## 5. First group of columns ##

cols_to_drop = ['funded_amnt', # Leaks info - Funding only starts after Approval
                'funded_amnt_inv', # Same as above
                'grade', # More detailed in int_rate
                'sub_grade', # Same as above
                'emp_title', # Requires more data
                'issue_d', # Leaks info - Issued only after Approval AND Funding
                'id',
                'member_id'
               ]

loans_2007 = loans_2007.drop(cols_to_drop, axis=1)

## 7. Second group of features ##

cols_to_drop = ['zip_code', # Info is censored
                'out_prncp', # Leaks info
                'out_prncp_inv', # Leaks info
                'total_pymnt', # Leaks info
                'total_pymnt_inv', # Leaks info
                'total_rec_prncp', # Leaks info
               ]

loans_2007 = loans_2007.drop(cols_to_drop, axis=1)

## 9. Third group of features ##

cols_to_drop = ['total_rec_int', # Leaks info
                'total_rec_late_fee', # Leaks info
                'recoveries', # Leaks info
                'collection_recovery_fee', # Leaks info
                'last_pymnt_d', # Leaks info
                'last_pymnt_amnt' # Leaks info
               ]

loans_2007 = loans_2007.drop(cols_to_drop, axis=1)

## 10. Target column ##

print(loans_2007['loan_status'].value_counts())

## 12. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")]

status_replace = {
    "loan_status" : {
        "Fully Paid": 1,
        "Charged Off": 0,
    }
}

loans_2007 = loans_2007.replace(status_replace)