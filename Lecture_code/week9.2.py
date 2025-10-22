"""
1. What is going well:
    - Students overwhelmingly appreciate the class structure — pre-class videos, in-class coding, and homework all work well together.
    - Hands-on coding practice in class is cited as the biggest strength.
    - They value being able to apply what they learn immediately rather than only watching lectures.
    - Many mentioned that content videos and knowledge checks help them come to class prepared.
    - The pacing feels appropriate and allows them time to understand new concepts.
    - Students enjoy walkthrough examples and problem-solving activities that reinforce logic and syntax.
    - Several noted they feel motivated and confident in their learning progress.
    - The quizzes and review games are appreciated as low-stakes opportunities to check understanding.
    - They find the homework manageable and aligned with class content.
    - Students find your teaching style and enthusiasm engaging and effective.
"""

"""
2. What could be going better:
    - The most common concern is that the class sometimes moves too fast, especially during new or complex material.
    - Some want more time to solve problems independently before reviewing them as a group.
    - In-class quizzes cause stress for several students, even though they find them helpful for learning.
    - A few mentioned difficulty with GitHub/Codespaces navigation and setup.
    - Some would like more interactive opportunities, such as volunteers sharing code or class discussions about errors.
    - Midterm feedback included concerns about unclear wording, inconsistent phrasing, and poor code formatting on Canvas.
    - Students requested more review on conceptual or written test questions, not just coding.
    - A few want additional practice problems or small weekly assignments to reinforce material.
    - A handful noted difficulty bridging coding with conceptual understanding, particularly during quizzes.
    - Some admitted personal time-management or study habits were their main barriers, not course design.
"""

"""
3. What is a Python concept you feel solid in:
     - Loops (for and while) were by far the most common area of confidence.
     - Students also feel strong in if/elif/else statements, basic logic, and Boolean operators.
     - Many are confident in lists, ranges, and variable assignment.
     - Some mentioned comfort with functions, though this was rare compared to loops and conditionals.
     - A few highlighted math operations, list slicing, or modifying lists as areas of strength.
     - Overall, students feel solid on foundational Python syntax and control flow, especially concepts introduced early in the semester.
"""

"""
4. What knowledge gaps do you have:
     - The most frequent response was functions (def) — students find them confusing and want more  practice or explanations on how and when to use them.
     - Many mentioned file handling (reading/writing files) as still unclear.
     - A number of students are uncertain about NumPy, arrays, and libraries, wanting more real-world examples or step-by-step practice.
     - Some said they struggle with applying concepts to new problems, even if they understand them individually.
     - A few feel uncertain about when to use specific tools or logic structures (e.g., //, %, or return statements).
     - Several students expressed a desire to see how Python applies to real-world projects.
     - Some reported confusion with nested code and how the computer “reads” code execution.
     - Others said they just need more practice to build speed and confidence, not necessarily new explanations.
     - A small number mentioned wanting to revisit lists and loops for reinforcement.
     - A few are looking ahead and curious about Pandas or more advanced data applications.
"""

# Strings :)

# concatenation
print("hello " + "world")

# var = input("Enter something: ")

print("hello", "world" + " I love " + "python")

fruit = "apple"
print("fruit:", fruit)
fruit *= 20
print("fruit:", fruit)

# string whitespace
example = "\t hello everyone I really really love python so much like I love it SO much\t"
print(example.strip())
print(example.rstrip())
print(example.lstrip())

# capitalization stuff
name = "big blue"
print("capitalize:", name.capitalize())
print("upper:", name.upper())
print("is upper?:", name.isupper())
print("is lower?:",name.islower())
print("lower:",name.lower())
print("is digit?:",name.isdigit())


# get user input
cities = []
for i in range(5):
    city = input("Enter the city you are from: ").lower()
    if city in cities:
        pass
    else:
        cities.append(city)

print("cities:", cities)


stuff = "hello everyone I really really love python so much like I love it SO much"
words = stuff.split(" ")
print(words)
city = "new york"
print(city.title())
