last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Graded subjects
subjects = [
  "physics",
  "calculus",
  "poetry",
  "history"
]

#grade scores
grades = [98, 97, 85, 88]

#2D list made up of subjects and scores
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

#adding new subjects and scores
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#Modifying "visual arts" score
gradebook[5][1] = 98

#Removing "Poetry" score
gradebook[2].remove(85)

#Adding "Pass" string to "Poetry" lists
gradebook[2].append("Pass")
print(gradebook)

#Concatanating Two lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)