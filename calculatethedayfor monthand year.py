def days_to_years_months_days(total_days):
    # Calculate years
    years = total_days // 365

    # Calculate the remaining days after extracting years
    remaining_days = total_days % 365

    # Calculate months
    months = remaining_days // 30

    # Calculate the remaining days after extracting months
    days = remaining_days % 30

    return years, months, days

# Example usage with 370 days
total_days = int(input("enter the days:"))
years, months, days = days_to_years_months_days(total_days)

print(f"{total_days} days is approximately {years} years, {months} months, and {days} days.")


