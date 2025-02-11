import pyjokes

# Fetch the joke
joke1 = pyjokes.get_joke(language="en", category="all")

# Display the joke
print(joke1,"\n")

# Different category
joke2 = pyjokes.get_joke(language="en", category="neutral")

# Display the joke
print(joke2,"\n")

# Fetch multiple jokes
jokes = pyjokes.get_jokes(language="en", category="neutral")

for i in range(5):
    print(i+1,".",jokes[i],"\n")
