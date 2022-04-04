words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text = []

for word in words:
    if word.isdigit():
        if word.replace("+", "").isdigit():
            text.append(f"'{int(word):02}'")
        else:
            text.append(f"'{word[0]} {int(word[1:]):02}'")
    else:
        text.append(word)

print(text)
print(" ".join(text))
