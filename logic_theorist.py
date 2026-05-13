#!/usr/bin/env python3
"""
The Logic Theorist - Python implementation

This is a Python implementation of the historic Logic Theorist AI system
created by Allen Newell and Herbert Simon in the 1950s.
"""

def modus_ponens(implication, antecedent):
    """
    Simple implementation of Modus Ponens theorem proving rule.
    
    Args:
        implication: A string representing an implication (e.g., "A -> B")
        antecedent: A string representing the antecedent (e.g., "A")
    
    Returns:
        The consequent if the rule is applied successfully, None otherwise
    """
    # Parse the implication
    if " -> " in implication:
        premise, conclusion = implication.split(" -> ")
        premise = premise.strip()
        conclusion = conclusion.strip()
        
        # Check if antecedent matches the premise
        if antecedent == premise:
            return conclusion
    
    return None

def main():
    """Main function to run the Logic Theorist implementation."""
    print("Welcome to The Logic Theorist!")
    print("This is a Python implementation of the historic AI system")
    print("that proved mathematical theorems in the 1950s.")
    print()
    print("Features:")
    print("- Implements core theorem proving capabilities")
    print("- Demonstrates early AI reasoning techniques")
    print("- Shows how symbolic AI approaches worked in the 1950s")
    print()
    print("Historical Significance:")
    print("- First AI program to prove mathematical theorems")
    print("- Demonstrated that computers could perform intelligent reasoning")
    print("- Laid the groundwork for modern AI research")
    print("- Showed that complex logical problems could be solved algorithmically")
    print()
    print("This implementation demonstrates basic theorem proving using")
    print("symbolic logic and rule-based reasoning.")
    print()
    print("Example theorem: (A -> B) & A -> B (Modus Ponens)")
    print("Example proof steps:")
    print("1. Given: A -> B (implication)")
    print("2. Given: A (antecedent)")
    print("3. Conclusion: B (consequent)")
    print()
    
    # Demonstrate actual theorem proving
    print("Demonstrating theorem proving:")
    print("-" * 30)
    
    # Example 1: Modus Ponens
    implication = "A -> B"
    antecedent = "A"
    conclusion = modus_ponens(implication, antecedent)
    
    if conclusion:
        print(f"Modus Ponens applied:")
        print(f"  Given: {implication}")
        print(f"  Given: {antecedent}")
        print(f"  Result: {conclusion}")
    else:
        print("Could not apply Modus Ponens")
    
    print()
    print("Note: This is a simplified educational implementation.")
    print("The real Logic Theorist was much more complex and sophisticated.")

if __name__ == "__main__":
    main()
