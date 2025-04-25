
print("🎉 Welcome to the Mad Libs Game! 🎉")
print("Please provide the following words:\n")

# User input
name = input("Naam: ")
place = input("Jagah: ")
adjective = input("Adjective (e.g. funny, scary): ")
animal = input("Jaanwar: ")
verb = input("Verb (koi action e.g. run, jump): ")
food = input("Khaana: ")
emotion = input("Emotion (e.g. happy, angry): ")
object_ = input("Koi object (cheez): ")
profession = input("Koi profession (e.g. doctor, singer): ")
celebrity = input("Celebrity ka naam: ")

# All 10 stories with input inserted
stories = [
    f"1️⃣ Ek din {name} gaya {place}, wahan usne ek {adjective} {animal} dekha jo {verb} kar raha tha.",
    f"2️⃣ {name} ne {place} me {food} khaya aur bohot {emotion} mehsoos kiya.",
    f"3️⃣ Ek {adjective} {animal} {name} ke ghar me aaya aur uska {object_} tod diya!",
    f"4️⃣ {name} banna chahta tha ek {profession}, lekin uska dil {celebrity} banne me lag gaya.",
    f"5️⃣ {name} aur ek {animal} ne mil kar {place} me {verb} kiya aur maze kiye.",
    f"6️⃣ {name} ne {place} me ek {adjective} restaurant dhoonda jahan sirf {food} milta tha.",
    f"7️⃣ Jab {name} {place} gaya, to usne dekha {celebrity} ek {animal} ke saath {verb} kar raha tha!",
    f"8️⃣ {name} ne {food} banaya aur usko {animal} ne chura liya. {name} ro pada!",
    f"9️⃣ Ek {adjective} din, {name} aur {celebrity} ne milkar {place} me {object_} se cricket khela.",
    f"🔟 {name} ka sapna tha {profession} banna, lekin uska {object_} usne {verb} karte hue tod diya."
]

# Print all stories one by one
print("\n--- 🎭 Tumhari 10 Mad Libs Stories 🎭 ---\n")
for story in stories:
    print(story + "\n")
