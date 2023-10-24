message = "One of Python's strengths is its diverse community."
print(message)

message2 = 'One of Python\'s strengths is its diverse community.'
print(message2)

# exercises
# 1 Personal Message
name = "Eric"
message_to_name = f"Hello {name}, would you like to learn some python today?";
print(message_to_name)

#2 name cases
persons_name = " willy Banker"
persons_name_toLower = persons_name.lower()
persons_name_toUpper = persons_name.upper()
persons_name_toCase = persons_name.title()
print(persons_name_toLower)
print(persons_name_toUpper)
print(persons_name_toCase)

# 3 famous quotes
famous_person = "Albert Einstein"
quote = f"{famous_person} once said, \"A person who never made a mistake never tried anything new\""
print(quote)

# 4 stripping names
name_toStrip_spaces = "   Hugo\t\nBas "
print(name_toStrip_spaces)
name_toStrip_spaces = name_toStrip_spaces.strip()
print(name_toStrip_spaces)