score = int(input("What's your credit score? "))
 
if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        category = "Excellent - Loan Approved"
        approved = True
    elif 700 <= score < 750:  # chained comparison
        category = "Good - Loan Approved with Review"
        approved = True
    elif 600 <= score < 700:
        category = "Fair - Loan Conditional"
        approved = False  # assumption: conditional is not a full approval
    else:
        category = "Poor - Loan Denied"
        approved = False
 
    if approved:
        print(f"{category}. Interest rate: Low")
    else:
        print(f"{category}. Seek credit improvement.")