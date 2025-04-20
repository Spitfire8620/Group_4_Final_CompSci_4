from itertools import product

# Takes user input to create clothing categories and types of clothing within those categories.
def EnterClosetItems():
    closet = {}
    print("Enter the categories of clothes in your closet (shirts, long sleeves, sweaters, jeans, shoes, etc). Type 'done' when finished:")
    
    while True:
        category = input("\nEnter the clothing category (or 'done'): ").strip().lower()
        if category == 'done':
            break
        if category in closet:
            print(f"You already added '{category}'.")
            continue

        items = input(f"\nEnter outfit items for '{category}' separated by commas: ").strip()
        ItemList = [item.strip() for item in items.split(',') if item.strip()]
        if ItemList:
            closet[category] = ItemList
        else:
            print("No items entered. Skipping category.\n")

    return closet

# Multiplies the different lists and elements to figure out the total number of possible outfit combinations.
def CountOutfits(ClosetDict):
    if not ClosetDict:
        return 0

    TotalOutfits = 1
    for category, items in ClosetDict.items():
        if items:
            TotalOutfits *= len(items)
        else:
            print(f"Warning: No items in {category}. Cannot form complete outfits.")
            return 0

    return TotalOutfits

def ListOutfits(ClosetDict):
    return list(product(*ClosetDict.values()))

# Main program
if __name__ == "__main__":
    print("Outfit Combination Generator\n")
    closet = EnterClosetItems()
    total = CountOutfits(closet)
    
    print(f"\nYou can make {total} different outfits.")

    ShowExamples = input("\nWould you like to see a few example outfits? (y)es/(n)o: ").strip().lower()
    if ShowExamples == 'yes' or 'y':
        examples = ListOutfits(closet)
        print("\nHere are some outfit combinations:")
        for outfit in examples[:min(5, len(examples))]:
            print(" - " + ", ".join(outfit))
