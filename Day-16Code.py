# Day 16 - Nested Functions
# Topic: BMI Calculator with Nested Checker

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🏋️  Day 16 - BMI Calculator with Nested Function")
    print("🔹 Topic: Nested Functions in Python\n")

# This function determines the BMI of a person by calculating and categorizing that person based on calculated BMI.
def bmi_wrapper(name, height_m, weight_kg):

    # This displays person name
    print(f"\n🧑 Calculating BMI for: {name}")
    
    # This one calculates BMI
    bmi = weight_kg / (height_m ** 2)
    print(f"📏 Height: {height_m} m | ⚖️ Weight: {weight_kg} kg")
    print(f"📊 BMI: {bmi:.2f}")

    # This Nested function is used to determine category of a person based on BMI value. It categorizes into 4 categories based upon bmi value
    def check_bmi_category(bmi_value):
        # If bmi value less than 18.5 then categorized into Underweight.
        if bmi_value < 18.5:
            return "Underweight"
        # If bmi value is b/w 18.5 and 2.9 then categorized into normal.
        elif 18.5 <= bmi_value < 24.9:
            return "Normal"
        # If bmi value is b/w 25 and 29.9 then categorized into Overweight.
        elif 25 <= bmi_value < 29.9:
            return "Overweight"
        # If all of above were not true then categorized into Obese.
        else:
            return "Obese"

    # category variable retrives the category of a person by passing bmi from where it was calculated to nested function
    category = check_bmi_category(bmi)

    # Displays the category of a person
    print(f"🩺 BMI Category: {category}\n")

    # Returns the bmi and category 
    return bmi, category


# main
def main():

    # calls this function to display introduction
    show_intro()

    # calling bmi_wrapper() with different names and values 
    bmi_wrapper("Jay", 1.75, 65)
    bmi_wrapper("Nayak", 1.80, 95)
    bmi_wrapper("Vicky", 1.60, 45)
    bmi_wrapper("Nihar", 1.65, 68)


# Starting point: The script is designed to run when executed directly. The conditional if __name__ == "__main__": main() ensures that main() is called only when the script is run as a standalone program, not when imported as a module.
if __name__ == "__main__":
    main()
