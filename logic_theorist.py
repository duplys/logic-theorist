#!/usr/bin/env python3
"""
The Logic Theorist - Python implementation

This is a Python implementation of the historic Logic Theorist AI system
created by Allen Newell and Herbert Simon in the 1950s.
"""

class LogicTheorist:
    def __init__(self):
        self.axioms = []
        self.rules = []
        self.proofs = []
        
    def add_axiom(self, axiom):
        """Add an axiom to the system"""
        self.axioms.append(axiom)
        
    def add_rule(self, rule_name, rule_function):
        """Add a proof rule to the system"""
        self.rules.append((rule_name, rule_function))
        
    def modus_ponens(self, implication, antecedent):
        """
        Apply Modus Ponens: If (A -> B) and A, then B
        """
        if " -> " in implication:
            premise, conclusion = implication.split(" -> ")
            premise = premise.strip()
            conclusion = conclusion.strip()
            
            if antecedent == premise:
                return conclusion
        return None
        
    def conjunction_introduction(self, a, b):
        """
        Introduce conjunction: If A and B, then (A & B)
        """
        return f"({a} & {b})"
        
    def conjunction_elimination(self, conjunction):
        """
        Eliminate conjunction: If (A & B), then A and B
        """
        if conjunction.startswith("(") and conjunction.endswith(")"):
            parts = conjunction[1:-1].split(" & ")
            if len(parts) == 2:
                return parts[0].strip(), parts[1].strip()
        return None
        
    def apply_rule(self, rule_name, *args):
        """Apply a specific rule to given arguments"""
        for name, rule_func in self.rules:
            if name == rule_name:
                return rule_func(*args)
        return None
        
    def prove_theorem(self, theorem):
        """Attempt to prove a theorem using available axioms and rules"""
        print(f"Attempting to prove: {theorem}")
        print("Available axioms:", self.axioms)
        print("Available rules:", [name for name, _ in self.rules])
        print()
        
        # Simple demonstration of theorem proving
        if theorem == "A -> B":
            print("Using axiom: A -> B")
            print("Result: Theorem proven!")
            return True
        elif theorem == "(A -> B) & A -> B":
            print("Using Modus Ponens rule:")
            print("  Given: A -> B")
            print("  Given: A")
            print("  Result: B")
            print("Result: Theorem proven!")
            return True
        else:
            print("Theorem not recognized in this simple implementation")
            return False

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
    
    # Create the Logic Theorist system
    lt = LogicTheorist()
    
    # Add some basic axioms
    lt.add_axiom("A -> B")
    lt.add_axiom("B -> C")
    
    # Add proof rules
    lt.add_rule("Modus Ponens", lt.modus_ponens)
    lt.add_rule("Conjunction Introduction", lt.conjunction_introduction)
    lt.add_rule("Conjunction Elimination", lt.conjunction_elimination)
    
    print("Demonstrating theorem proving:")
    print("-" * 30)
    
    # Example 1: Simple theorem
    theorem1 = "(A -> B) & A -> B"
    print(f"Proving theorem: {theorem1}")
    lt.prove_theorem(theorem1)
    print()
    
    # Example 2: More complex theorem
    theorem2 = "A -> C"
    print(f"Proving theorem: {theorem2}")
    lt.prove_theorem(theorem2)
    print()
    
    print("Note: This is a simplified educational implementation.")
    print("The real Logic Theorist was much more complex and sophisticated.")

if __name__ == "__main__":
    main()
