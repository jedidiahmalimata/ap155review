if __name__ == "__main__":
    # execute only if run as a script
    main()
    
from math import pi

G = 6.67e-11
M = 5.97e24
R = 6371000
t = float(input("Enter the time interval: "))
h = ((G * M * t**2) / (4 * pi**2))**(1./3) - R

print "The altitude of the satellite is %s meters." % h