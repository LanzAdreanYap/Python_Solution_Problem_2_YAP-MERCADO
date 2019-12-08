import numpy as np
# Name the function as Cirlce
# This program allows you to determine the center, radius, and a vector [D,E,F] of a circle given three points that ly on the circle
def Circle():
    #Introduction
    print("The General Equation of the Circle is in the Form:")
    print("Ax^2 + Ay^2 + Bx + Cy + G")
    print("")
    print("It can be simplified to:")
    print("x^2 + y^2 + Dx + Ey + F")
    print("")
    print("Where:")
    print("D = B/A")
    print("E = C/A")
    print("F = G/A")
    print("")
    print("This program allows you to determine the following parameters of a circle that lies on three points")
    print("~ Center of the Circle, (h,k)")
    print("~ Radius of the Circle, r")
    print("~ Vector [D,E,F]")
    print("")
    print("To begin with, input three points that ly on the circle")
    # Input the First Point
    print("First Point")
    x1 = float(input("X1: "))
    y1 = float(input("Y1: "))
    # Input the Second Point
    print("Second Point")
    x2 = float(input("X2: "))
    y2 = float(input("Y2: "))
    # Input the Third Point
    print("Third Point")
    x3 = float(input("X3: "))
    y3 = float(input("Y3: "))
    print("")
    # Get the square of the components of each point and store it to a new variable
    X1 = x1**2;
    Y1 = y1**2;
    X2 = x2**2;
    Y2 = y2**2;
    X3 = x3**2;
    Y3 = y3**2;
    # Get the sum of the squares of the component for each point and store it to a new variable
    p1 = X1 + Y1;
    p2 = X2 + Y2;
    p3 = X3 + Y3;
    # Solve for the coefficients A, D, E and F
    # The Following Matrices are Created
    a = np.array([(x1,y1,1),(x2,y2,1),(x3,y3,1)]);
    b = np.array([(p1,y1,1),(p2,y2,1),(p3,y3,1)]);
    c = np.array([(p1,x1,1),(p2,x2,1),(p3,x3,1)]);
    d = np.array([(p1,x1,y1),(p2,x2,y2),(p3,x3,y3)]);
    # Get the determinant of matrix a to get the value of A
    A = np.linalg.det(a);
    # Get the negative of the determinant of matrix b and divide it by A to get the value of D
    D = ((-1)*np.linalg.det(b))/A;
    # Get the determinant of matrix c and divide it by A to get the value of E
    E = np.linalg.det(c)/A;
    # Get the negative of the determinant of matrix d and divide it by A to get the value of F
    F = ((-1)*np.linalg.det(d))/A;
    # x-component(h) and y-component(k) of the center of the circle is solved by
    h = ((-1)*D)/2;
    k = ((-1)*E)/2;
    # The radius(r) of the circle is solved by
    r = ((((D*A)**2)+((E*A)**2)-(4*A*(F*A)))/(4*(A**2)))**(1/2);
    # Create and empty vector and append the values of D,E, and F, respectively
    vector = [];
    vector.append(round(D,2))
    vector.append(round(E,2))
    vector.append(round(F,2))
    # Display the output
    print("Given the three points, the following solved parameters of the circle are:")
    print("Center: (",round(h,2),",",round(k,2),")")
    print("Radius: ", round(r,2))
    print("Vector [D,E,F]: ",vector)
    
