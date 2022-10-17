import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#assumptions:
#The heights of all races, (except Urgals), in Alagaësia follow normal distributions (bell curves), the same way human heights do.
#The standard deviations of these heights can be calculated by scaling from human standard deviations.

x = np.arange(0, 300)

#Using this study: https://ourworldindata.org/human-height#how-has-height-changed-globally
#A mean, male population height of 178 cm results in a standard deviation of 7.59 cm.
#The function estimates new standard deviations by scaling directly from these numbers.
def standard_deviation(mean):
    scaling_sd = 7.59
    scaling_mean = 178
    standard_deviation = (scaling_sd * mean) / scaling_mean
    return standard_deviation

plt.axvline(x = 259, color = 'b', label = 'Nar Garzhvog')
plt.axvline(x = 221.9, color = 'g', label = 'Unlucky Urgal on the verge of being a Kull')

#Kull height: mean = 248 cm, assuming Nar Garzhvog is 8.5 feet = 259 cm and 1 SD (11 cm) above the mean kull height
#This would mean that Nar Garzhvog would be taller than 68% of all kull.
kull_mean = 248
kull_sd = standard_deviation(kull_mean)
y_kull = norm.pdf(x, loc = kull_mean, scale = kull_sd)
plt.plot(x, y_kull, label='Kull')

#Non-kull urgal height: mean = 200 cm, assuming height based on eyeballing official art
urgal_mean = 200
urgal_sd = standard_deviation(urgal_mean)
y_urgal = norm.pdf(x, loc = urgal_mean, scale = urgal_sd)
plt.plot(x, y_urgal, label='Non-kull Urgals')

#Elf height: mean = 190 cm, assuming height based on eyeballing official art
elf_mean = 190
elf_sd = standard_deviation(elf_mean)
y_elf = norm.pdf(x, loc = elf_mean, scale = elf_sd)
plt.plot(x, y_elf, label='Elves')

#Male human height: mean = 165 cm, (using mean height of a man during European Middle Ages instead of modern times) 
human_mean = 165
human_sd = standard_deviation(human_mean)
y_human = norm.pdf(x, loc = human_mean, scale = human_sd)
plt.plot(x, y_human, label='Human men')

#Dwarf height: mean = 110 cm, assuming height based on eyeballing official art
dwarf_mean = 110
dwarf_sd = standard_deviation(dwarf_mean)
y_dwarf = norm.pdf(x, loc = dwarf_mean, scale = dwarf_sd)
plt.plot(x, y_dwarf, label='Dwarves')

plt.xlabel('cm')
plt.title("Probability density functions of heights of all races in Alagaësia")
plt.title("Probability density functions of Urgal heights")
plt.legend()
plt.show()