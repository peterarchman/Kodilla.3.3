# Zad 1

shopping_dict = {
  "piekarnia" : ["chleb", "bułki", "pączek"],
  "warzywniak" : ["marchew", "seler", "rukola"]
}

for key in shopping_dict:
  print("Idę do", key, "kupuję następujące rzeczy:", shopping_dict[key])

item_number = len(shopping_dict["piekarnia"]) + len(shopping_dict["warzywniak"])

print("W sumie kupuję", item_number, "produktów.")
