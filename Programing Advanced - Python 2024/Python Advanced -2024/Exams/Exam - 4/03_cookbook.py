def cookbook(*args):
    cookbook_data = {}
    for recipe, country, ingredient in args:
        if country not in cookbook_data:
            cookbook_data[country] = {}
        
        cookbook_data[country][recipe] = ingredient

        output = []
    for country, recipes in sorted(cookbook_data.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{country} cuisine contains {len(cookbook_data[country])} recipes:")

        for recipe, ingredients in sorted(recipes.items()):
            output.append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(output)